from ..domain.models import ProductData, ProgressCallback
from ..infrastructure.oxylabs_client import OxyLabsClient
from ..infrastructure.data.repositories.product_repository import ProductRepository


class CompetitorService:
    def __init__(self, repo: ProductRepository, client: OxyLabsClient) -> None:
        self.repo = repo
        self.client = client

    def fetch_and_store_competitors(
        self,
        parent_asin: str,
        domain: str,
        geo_location: str,
        pages: int = 2,
        progress_callback: ProgressCallback | None = None,
    ) -> list[ProductData]:
        print("Fetching competitors for product", parent_asin)

        parent = self.repo.get_product(parent_asin)
        if not parent:
            return []

        search_domain = parent.get("amazon_domain", domain)
        search_geo = parent.get("geo_location", geo_location)

        search_categories: list[str] = []
        if parent.get("categories"):
            search_categories.extend(str(cat) for cat in parent["categories"] if cat)
        if parent.get("category_path"):
            search_categories.extend(str(cat) for cat in parent["category_path"] if cat)

        unique_categories = list(
            dict.fromkeys(
                cat.strip()
                for cat in search_categories
                if cat and isinstance(cat, str) and cat.strip()
            )
        )

        all_results: list[ProductData] = []
        for category in unique_categories[:3]:
            search_results = self.client.search_competitors(
                query_title=parent["title"],
                domain=search_domain,
                categories=[category],
                pages=pages,
                geo_location=search_geo,
            )
            all_results.extend(search_results)

        competitor_asins = list(
            dict.fromkeys(
                result.get("asin")
                for result in all_results
                if result.get("asin") and result.get("asin") != parent_asin and result.get("title")
            )
        )

        competitor_details = self.client.scrape_multiple_products(
            competitor_asins[:20],
            geo_location,
            domain,
            progress_callback=progress_callback,
        )

        stored_competitors: list[ProductData] = []
        for competitor in competitor_details:
            competitor["parent_asin"] = parent_asin
            self.repo.insert_product(competitor)
            stored_competitors.append(competitor)

        return stored_competitors

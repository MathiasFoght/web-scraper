import os
import time
from collections.abc import Sequence
from typing import Any
import requests
from dotenv import load_dotenv
from ..domain.utils import (
    clean_product_name,
    extract_content,
    extract_search_results,
    normalize_product,
    normalize_search_result,
)
from ..domain.models import ProductData, ProgressCallback

load_dotenv()

OXYLABS_BASE_URL = "https://realtime.oxylabs.io/v1/queries"


class OxyLabsClient:
    def __init__(self, base_url: str = OXYLABS_BASE_URL) -> None:
        self.base_url = base_url

    def post_query(self, payload: dict[str, Any]) -> dict[str, Any]:
        username = os.getenv("OXYLABS_USERNAME")
        password = os.getenv("OXYLABS_PASSWORD")

        response = requests.post(self.base_url, json=payload, auth=(username, password))
        response.raise_for_status()
        return response.json()

    def scrape_product_details(self, asin: str, geo_location: str, domain: str) -> ProductData:
        payload = {
            "source": "amazon_product",
            "query": asin,
            "geo_location": geo_location,
            "domain": domain,
            "parse": True,
        }

        raw = self.post_query(payload)
        content = extract_content(raw)
        normalized = normalize_product(content)

        if not normalized.get("asin"):
            normalized["asin"] = asin

        normalized["amazon_domain"] = domain
        normalized["geo_location"] = geo_location
        return normalized

    def search_competitors(
        self,
        query_title: str,
        domain: str,
        categories: Sequence[str],
        pages: int = 1,
        geo_location: str = "",
    ) -> list[ProductData]:
        search_title = clean_product_name(query_title)
        results: list[ProductData] = []
        seen_asins: set[str] = set()

        strategies = ["feature", "price_asc", "price_desc", "rating_desc", "avg_rating"]

        for sort_by in strategies:
            for page in range(1, max(1, pages) + 1):
                payload: dict[str, Any] = {
                    "source": "amazon_search",
                    "query": search_title,
                    "parse": True,
                    "domain": domain,
                    "page": page,
                    "sort_by": sort_by,
                    "geo_location": geo_location,
                }

                if categories and categories[0]:
                    payload["refinement"] = {"category": categories[0]}

                content = extract_content(self.post_query(payload))
                items = extract_search_results(content)

                for item in items:
                    result = normalize_search_result(item)
                    if result and result.get("asin") and result["asin"] not in seen_asins:
                        seen_asins.add(result["asin"])
                        results.append(result)

                time.sleep(0.1)

        return results

    def scrape_multiple_products(
        self,
        asins: Sequence[str],
        geo_location: str,
        domain: str,
        progress_callback: ProgressCallback | None = None,
    ) -> list[ProductData]:
        products: list[ProductData] = []
        total = len(asins)
        scraped_count = 0

        for index, asin in enumerate(asins, start=1):
            try:
                product = self.scrape_product_details(asin, geo_location, domain)
                products.append(product)
                scraped_count += 1
            except Exception:
                pass

            # Update progress after each product is processed
            if progress_callback:
                progress_callback(index, total, scraped_count, asin)

        return products

from ..domain.models import ProductData
from ..infrastructure.oxylabs_client import OxyLabsClient
from ..infrastructure.data.repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self, repo: ProductRepository, client: OxyLabsClient) -> None:
        self.repo = repo
        self.client = client

    def scrape_and_store_product(self, asin: str, geo_location: str, domain: str) -> ProductData:
        data = self.client.scrape_product_details(asin, geo_location, domain)
        self.repo.insert_product(data)
        return data

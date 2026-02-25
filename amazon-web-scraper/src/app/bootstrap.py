from dataclasses import dataclass
from ..application.analysis_service import AnalysisService
from ..application.competitor_service import CompetitorService
from ..application.product_service import ProductService
from ..infrastructure.oxylabs_client import OxyLabsClient
from ..infrastructure.data import Database, ProductRepository


@dataclass(frozen=True)
class AppContainer:
    db: Database
    repo: ProductRepository
    product_service: ProductService
    competitor_service: CompetitorService
    analysis_service: AnalysisService


def build_container() -> AppContainer:
    db = Database()
    repo = ProductRepository(db)
    client = OxyLabsClient()

    return AppContainer(
        db=db,
        repo=repo,
        product_service=ProductService(repo=repo, client=client),
        competitor_service=CompetitorService(repo=repo, client=client),
        analysis_service=AnalysisService(repo=repo),
    )

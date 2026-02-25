from typing import Optional

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

from ..domain.models import ProductData
from ..infrastructure.llm_client import analyze_model
from ..infrastructure.data.repositories.product_repository import ProductRepository


class CompetitorAnalysis(BaseModel):
    asin: str
    title: Optional[str]
    price: Optional[float]
    currency: Optional[str]
    rating: Optional[float]
    key_points: list[str] = Field(default_factory=list)


class AnalysisResponse(BaseModel):
    summary: str
    positioning: str
    top_competitors: list[CompetitorAnalysis]
    recommendations: list[str]


class AnalysisService:
    def __init__(self, repo: ProductRepository) -> None:
        self.repo = repo

    def _format_competitors(self, parent_asin: str) -> list[ProductData]:
        competitors = self.repo.search_products({"parent_asin": parent_asin})
        return [
            {
                "asin": competitor["asin"],
                "title": competitor["title"],
                "price": competitor["price"],
                "currency": competitor["currency"],
                "rating": competitor["rating"],
                "amazon_domain": competitor.get("amazon_domain"),
            }
            for competitor in competitors
        ]

    def analyze_competitors(self, asin: str) -> str:
        print("Analyzing competitors for product")

        product = self.repo.get_product(asin)
        competitors = self._format_competitors(asin)

        parser = PydanticOutputParser(pydantic_object=AnalysisResponse)

        template = (
            "You are a market analyst. Given a product and its competitor list, "
            "write a concise analysis. Pay attention to currency and pricing context.\n\n"
            "Product Title: {product_title}\n"
            "Brand: {brand}\n"
            "Price: {currency} {price}\n"
            "Rating: {rating}\n"
            "Categories: {categories}\n"
            "Amazon Domain: {amazon_domain}\n\n"
            "Competitors (JSON): {competitors}\n\n"
            "IMPORTANT: All prices should be displayed with their correct currency symbol. "
            "When comparing prices, ensure you're using the same currency context.\n\n"
            "{format_instructions}"
        )

        prompt = PromptTemplate(
            template=template,
            input_variables=[
                "product_title",
                "brand",
                "price",
                "rating",
                "categories",
                "amazon_domain",
                "competitors",
            ],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        chain = prompt | analyze_model() | parser
        result = chain.invoke(
            {
                "product_title": product["title"] if product else asin,
                "brand": product.get("brand") if product else None,
                "price": product.get("price") if product else None,
                "currency": product.get("currency") if product else "",
                "rating": product.get("rating") if product else None,
                "categories": product.get("categories") if product else None,
                "amazon_domain": product.get("amazon_domain") if product else "com",
                "competitors": competitors,
            }
        )

        lines: list[str] = [
            "Summary:\n" + result.summary,
            "\nPositioning:\n" + result.positioning,
            "\nCompetitors:",
        ]

        for competitor in result.top_competitors[:5]:
            points = "; ".join(competitor.key_points) if competitor.key_points else ""
            currency = competitor.currency if competitor.currency else ""
            price_str = f"{currency} {competitor.price}" if currency else f"${competitor.price}"
            lines.append(
                f"- {competitor.asin} | {competitor.title} | {price_str} | {competitor.rating} | {points}"
            )

        if result.recommendations:
            lines.append("\nRecommendations:")
            for recommendation in result.recommendations:
                lines.append(f"- {recommendation}")

        return "\n".join(lines)

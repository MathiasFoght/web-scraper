from dotenv import load_dotenv
from .repositories.product_repository import ProductRepository
from .db import Database
from pydantic import BaseModel, Field
from typing import List, Optional
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

db = Database()
repo = ProductRepository(db)

# Data model for the competitor analysis
class CompetitorAnalysis(BaseModel):
     asin: str
     title: Optional[str]
     price: Optional[float]
     currency: Optional[str]
     rating: Optional[float]
     key_points: List[str] = Field(default_factory=list)

# Data model for the LLM output
class AnalysisResponse(BaseModel):
    summary: str
    positioning: str
    top_competitors: List[CompetitorAnalysis]
    recommendations: List[str]

def format_competitors(parent_asin):
    competitors = repo.search_products({"parent_asin": parent_asin})
    return [
        {
            "asin": c["asin"],
            "title": c["title"],
            "price": c["price"],
            "currency": c["currency"],
            "rating": c["rating"],
            "amazon_domain": c.get("amazon_domain")
        }

        for c in competitors
    ]

def analyze_competitors(asin):
    print('Analyzing competitors for: ', asin, '\n\n')
    product = repo.get_product(asin)
    competitors = format_competitors(asin)

    parser = PydanticOutputParser(pydantic_object=AnalysisResponse)

    AI_template = (
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
        template=AI_template,
        input_variables=["product_title", "brand", "price", "rating", "categories", "amazon_domain", "competitors"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )

    llm_setup = ChatOpenAI(model="gpt-4", temperature=0, max_tokens=1000, max_retries=3) #Temp. is set to 0 to ensure more deterministic output.
    # Chain for the analysis
    chain = prompt | llm_setup | parser
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
    
    lines = [
        "Summary:\n" + result.summary,
        "\nPositioning:\n" + result.positioning,
        "\nCompetitors:"
    ]

    for c in result.top_competitors[:5]: #Show only top 5 comp. in summary
        points = "; ".join(c.key_points) if c.key_points else ""
        currency = c.currency if c.currency else ""
        price_str = f"{currency} {c.price}" if currency else f"${c.price}"
        lines.append(f"- {c.asin} | {c.title} | {price_str} | {c.rating} | {points}")

    if result.recommendations:
        lines.append("\nRecommendations:")
        for r in result.recommendations:
            lines.append(f"- {r}")
    return "\n".join(lines)

import re
from collections.abc import Mapping
from typing import Any

from ..domain.models import ProductData


def extract_content(payload: Any) -> Any:
    if isinstance(payload, dict):
        if "results" in payload and isinstance(payload["results"], list) and payload["results"]:
            first_result = payload["results"][0]
            if isinstance(first_result, dict) and "content" in first_result:
                return first_result["content"] or {}
        if "content" in payload:
            return payload.get("content", {})

    return payload


def normalize_product(content: Mapping[str, Any]) -> ProductData:
    category_path: list[str] = []
    if content.get("category_path"):
        category_path = [cat.strip() for cat in content["category_path"] if cat]

    return {
        "asin": content.get("asin"),
        "url": content.get("url"),
        "brand": content.get("brand"),
        "price": content.get("price"),
        "stock": content.get("stock"),
        "title": content.get("title"),
        "rating": content.get("rating"),
        "images": content.get("images", []),
        "categories": content.get("category", []) or content.get("categories", []),
        "category_path": category_path,
        "currency": content.get("currency"),
        "buybox": content.get("buybox", []),
        "product_overview": content.get("product_overview", []),
    }


def clean_product_name(title: str) -> str:
    if "--" in title:
        title = title.split("--")[0]
    if "|" in title:
        title = title.split("|")[0]
    return title.strip()


def extract_search_results(content: Any) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    if not isinstance(content, dict):
        return items

    if "results" in content:
        results = content["results"]
        if isinstance(results, dict):
            if "organic" in results:
                items.extend(results["organic"])
            if "paid" in results:
                items.extend(results["paid"])
        elif "products" in content and isinstance(content["products"], list):
            items.extend(content["products"])

        return items
    return items


def normalize_search_result(item: Mapping[str, Any]) -> ProductData | None:
    asin = item.get("asin") or item.get("product_asin")
    title = item.get("title")

    if not (asin or title):
        return None

    return {
        "asin": asin,
        "title": title,
        "category": item.get("category"),
        "price": item.get("price"),
        "rating": item.get("rating"),
    }


def parse_numeric_price(value: Any) -> float | None:
    if isinstance(value, (int, float)):
        return float(value)
    if not isinstance(value, str):
        return None

    stripped = value.strip()
    if not stripped:
        return None

    cleaned = re.sub(r"[^0-9,.-]", "", stripped)
    if not cleaned:
        return None

    if "," in cleaned and "." in cleaned:
        cleaned = cleaned.replace(",", "")
    elif "," in cleaned and "." not in cleaned:
        cleaned = cleaned.replace(",", ".")

    try:
        return float(cleaned)
    except ValueError:
        return None

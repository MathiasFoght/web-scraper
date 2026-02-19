import os
from dotenv import load_dotenv
import requests

load_dotenv()

OXYLABS_BASE_URL = "https://realtime.oxylabs.io/v1/queries"

# Extract content from different payload formats
def extract_content(payload):
    if isinstance(payload, dict):
        if "results" in payload and isinstance(payload["results"], list) and payload["results"]:
            first_result = payload["results"][0]
            if isinstance(first_result, dict) and "content" in first_result:
                return first_result["content"] or {}
        if "content" in payload:
            return payload.get("content", {})

    return payload



# Func. to post query to OxyLabs
def post_query(payload):
    username = os.getenv("OXYLABS_USERNAME")
    password = os.getenv("OXYLABS_PASSWORD")

    response = requests.post(OXYLABS_BASE_URL, json=payload, auth=(username, password))
    response.raise_for_status()
    response_data = response.json()

    return response_data

# Func. to normalize different product formats into a base structure
def normalize_product(content):
    category_path = []
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
        "product_overview": content.get("product_overview", [])
    }

def scrape_product_details(asin, geo_location, domain):
    payload = {
        "source": "amazon_product",
        "query": asin,
        "geo_location": geo_location,
        "domain": domain,
        "parse": True
    }

    raw = post_query(payload)
    content = extract_content(raw)
    normalized = normalize_product(content)

    if not normalized.get("asin"):
        normalized["asin"] = asin

    normalized["amazon_domain"] = domain
    normalized["geo_location"] = geo_location
    return normalized


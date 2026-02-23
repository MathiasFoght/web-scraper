from .db import Database
from .client import scrape_product_details, search_competitors, scrape_multiple_products
from .repositories.product_repository import ProductRepository

db = Database()
repo = ProductRepository(db)

# Func. to scrape product details and store
def scrape_and_store_product(asin, geo_location, domain):
    print('Scraping product: ', asin)
    data = scrape_product_details(asin, geo_location, domain)
    repo.insert_product(data)
    return data


# Func. to fetch competitors and store
def fetch_and_store_competitors(parent_asin, domain, geo_location, pages=2, progress_callback=None):
    print('Fetching competitors for: ', parent_asin)
    parent = repo.get_product(parent_asin)
    if not parent:
        return []

    search_domain = parent.get("amazon_domain", domain)
    search_geo = parent.get("geo_location", geo_location)

    search_categories = []
    if parent.get("categories"):
        search_categories.extend(str(cat) for cat in parent["categories"] if cat)
    if parent.get("category_path"):
        search_categories.extend((str(cat) for cat in parent["categories_path"] if cat))

    search_categories = list(set(
        cat.strip()
        for cat in search_categories
        if cat and isinstance(cat, str) and cat.strip()
    ))

    all_results = []
    for category in search_categories[:3]:
        search_results = search_competitors(
            query_title=parent["title"],
            domain=search_domain,
            categories=[category],
            pages=pages,
            geo_location=search_geo
        )
        all_results.extend(search_results)

    competitors_asins = list(set(
        r.get("asin") for r in all_results
        if r.get("asin") and r.get("asin") != parent_asin and r.get("title")
    ))

    parent_details = scrape_multiple_products(
        competitors_asins[:20], # Set a max of 20 competitors to be scraped per product
        geo_location,
        domain,
        progress_callback=progress_callback,
    )

    stored_competitors = []
    for competitor in parent_details:
        competitor["parent_asin"] = parent_asin
        repo.insert_product(competitor)
        stored_competitors.append(competitor)

    return stored_competitors

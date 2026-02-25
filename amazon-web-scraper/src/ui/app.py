import streamlit as st

from ..app import build_container
from ..domain.models import ProductData
from .components import (
    render_competitor_summary,
    render_hero,
    render_inputs,
    render_products_section,
)
from .styles import apply_styles


def _fetch_competitors_with_progress(
    selected_asin: str,
    domain: str,
    geo: str,
    competitor_service,
) -> list[ProductData]:
    progress_text = st.empty()
    progress_bar = st.progress(0)

    def on_progress(processed: int, total: int, scraped_count: int, _asin: str) -> None:
        if total <= 0:
            progress_text.info("No products to scrape.")
            progress_bar.progress(0)
            return

        ratio = processed / total
        progress_bar.progress(min(max(ratio, 0.0), 1.0))
        progress_text.info(f"Scraped {scraped_count}/{total} products")

    with st.spinner("Searching and scraping competitors..."):
        competitors = competitor_service.fetch_and_store_competitors(
            selected_asin,
            domain,
            geo,
            progress_callback=on_progress,
        )

    progress_bar.empty()
    progress_text.empty()
    return competitors


def initialize() -> None:
    st.set_page_config(page_title="Web Scraper", layout="wide")
    apply_styles()
    render_hero()

    container = build_container() # Build dependencies
    repo = container.repo
    repo.init_schema()

    asin, geo, domain = render_inputs()

    # Scrape
    if st.button("Scrape Product") and asin:
        with st.spinner("Scraping product..."):
            container.product_service.scrape_and_store_product(asin, geo, domain)
        st.success("Product scraped successfully.")

    products = repo.get_all_products()
    render_products_section(products, repo)

    selected_asin = st.session_state.get("analyzing_asin")
    if not selected_asin:
        return

    st.markdown("---")
    st.markdown(f"## Competitor Analysis for `{selected_asin}`")
    existing_competitors = repo.search_products({"parent_asin": selected_asin})

    if not existing_competitors:
        competitors = _fetch_competitors_with_progress(
            selected_asin,
            domain,
            geo,
            container.competitor_service,
        )
        st.success(f"Found {len(competitors)} competitors.")
        render_competitor_summary(competitors)
    else:
        st.info(f"Using {len(existing_competitors)} competitors from database.")
        render_competitor_summary(existing_competitors)

    # Refresh
    if st.button("Refresh competitors"):
        competitors = _fetch_competitors_with_progress(
            selected_asin,
            domain,
            geo,
            container.competitor_service,
        )
        st.success(f"Found {len(competitors)} competitors.")
        render_competitor_summary(competitors)

    # Generate AI analysis for selected product
    if st.button("Analyze with AI", type="primary"):
        with st.spinner("Generating analysis..."):
            analysis = container.analysis_service.analyze_competitors(selected_asin)
        st.markdown(analysis)

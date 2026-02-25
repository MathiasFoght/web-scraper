import csv
import io
from collections.abc import Sequence
from datetime import date
from typing import Any

import streamlit as st
from openpyxl import Workbook
from ..domain.utils import parse_numeric_price

CSV_COLUMNS = [
    "asin",
    "title",
    "brand",
    "price",
    "currency",
    "rating",
    "amazon_domain",
    "geo_location",
    "url",
    "created_at",
]
ProductData = dict[str, Any]

def _csv_value(value: Any) -> str | int | float | bool:
    if value is None:
        return ""
    if isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


def _csv_rows(products: Sequence[ProductData]) -> list[dict[str, str | int | float | bool]]:
    rows: list[dict[str, str | int | float | bool]] = []
    for product in products:
        row = {}
        for column in CSV_COLUMNS:
            row[column] = _csv_value(product.get(column))
        rows.append(row)
    return rows


def _products_to_csv_bytes(products: Sequence[ProductData]) -> bytes:
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=CSV_COLUMNS)
    writer.writeheader()
    writer.writerows(_csv_rows(products))
    return buffer.getvalue().encode("utf-8")


def _products_to_xlsx_bytes(products: Sequence[ProductData]) -> bytes:
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Products"
    sheet.append(CSV_COLUMNS)

    for row in _csv_rows(products):
        sheet.append([row[column] for column in CSV_COLUMNS])

    buffer = io.BytesIO()
    workbook.save(buffer)
    return buffer.getvalue()


def _build_export_file(products: Sequence[ProductData], export_format: str) -> tuple[bytes, str, str]:
    if export_format == "XLSX":
        return (
            _products_to_xlsx_bytes(products),
            "xlsx",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )

    return (_products_to_csv_bytes(products), "csv", "text/csv")


@st.dialog("Export products")
def _render_export_dialog(
    page_products: Sequence[ProductData],
    all_products: Sequence[ProductData],
    page: int,
    today: str,
) -> None:
    export_format = st.selectbox("Format", ["XLSX", "CSV"], index=1, key="export_format")
    export_scope = st.selectbox(
        "Scope",
        ["Current page", "All products"],
        index=0,
        key="export_scope",
    )

    selected_products = page_products if export_scope == "Current page" else all_products
    scope_label = f"page_{page + 1}" if export_scope == "Current page" else "all"
    file_data, ext, mime = _build_export_file(selected_products, export_format)

    st.caption(f"Rows to export: {len(selected_products)}")
    st.download_button(
        label="Download",
        data=file_data,
        file_name=f"products_{scope_label}_{today}.{ext}",
        mime=mime,
        key=f"download_export_{scope_label}_{ext}",
    )


def render_hero() -> None:
    st.markdown(
        """
        <div class="hero">
          <h2 style="margin:0;">Amazon Product Intelligence</h2>
          <p>Scrape products, identify competitors, and generate AI-driven competitor insights.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_inputs() -> tuple[str, str, str]:
    input_col, _ = st.columns([1, 2.2])
    with input_col:
        asin = st.text_input("ASIN", placeholder="e.g., B08N5WRWNW")
        geo = st.text_input("ZIP/Postal Code", placeholder="e.g., EU")
        domain = st.selectbox("Domain", ["com", "ca", "co.uk", "de", "fr", "it", "ae"])
    return asin.strip(), geo.strip(), domain


def _format_price(product: ProductData) -> str:
    price = product.get("price", "--")
    currency = product.get("currency", "")
    if isinstance(price, (int, float)):
        return f"{currency}{price:,.2f}" if currency else f"{price:,.2f}"
    return str(price)


def _format_money(value: float | None, currency: str = "") -> str:
    if value is None:
        return "--"
    if currency:
        return f"{currency}{value:,.2f}"
    return f"{value:,.2f}"


def _build_price_history_series(
    raw_history: Sequence[ProductData],
) -> tuple[list[dict[str, Any]], str, int]:
    points: list[dict[str, Any]] = []
    skipped: int = 0
    currency: str = ""

    for item in raw_history:
        numeric_price = parse_numeric_price(item.get("price"))
        if numeric_price is None:
            skipped += 1
            continue

        if not currency and item.get("currency"):
            currency = str(item.get("currency"))

        timestamp = item.get("scraped_at")
        timestamp_label = (
            timestamp.strftime("%Y-%m-%d %H:%M")
            if hasattr(timestamp, "strftime")
            else str(timestamp)
        )

        points.append(
            {
                "timestamp": timestamp,
                "timestamp_label": timestamp_label,
                "price": numeric_price,
            }
        )

    return points, currency, skipped


def _render_price_history_card(product: ProductData, repo: Any) -> None:
    asin = product.get("asin")
    if not asin:
        st.caption("No ASIN available for price history.")
        return

    with st.expander("Price history"):
        days = st.selectbox(
            "Window (days)",
            [7, 30, 90],
            index=1,
            key=f"history_window_{asin}",
        )

        raw_history = repo.get_price_history(asin, days=days)
        points, currency, skipped = _build_price_history_series(raw_history)

        if not points:
            st.caption("No valid numeric price data in this period.")
            return

        if skipped > 0:
            st.caption(f"Ignored {skipped} snapshots with non-numeric prices.")

        st.line_chart(points, x="timestamp_label", y="price")

        latest_price = points[-1]["price"]
        if len(points) == 1:
            st.metric("Latest price", _format_money(latest_price, currency))
            st.caption("Not enough points to determine trend.")
            return

        first_price = points[0]["price"]
        delta = latest_price - first_price
        if delta > 0:
            trend = "Increasing"
        elif delta < 0:
            trend = "Decreasing"
        else:
            trend = "Unchanged"

        st.metric(
            f"Trend ({days}d)",
            f"{trend} - {_format_money(latest_price, currency)}",
            f"{delta:+,.2f}" if not currency else f"{currency}{delta:+,.2f}",
        )


def render_product_card(product: ProductData, repo: Any) -> None:
    with st.container(border=True):
        col_image, col_content = st.columns([1, 2.2])

        images = product.get("images", [])
        if images:
            col_image.image(images[0], width=150)
        else:
            col_image.caption("No image available")

        with col_content:
            title = product.get("title") or product.get("asin")
            st.markdown(f"### {title}")

            m1, m2, m3 = st.columns(3)
            m1.metric("Price", _format_price(product))
            m2.metric("Brand", product.get("brand", "--"))
            m3.metric("Rating", product.get("rating", "--"))

            domain_info = f"amazon.{product.get('amazon_domain', 'com')}"
            geo_info = product.get("geo_location", "--")
            st.markdown(
                f'<p class="subtle">Domain: {domain_info} | Geo Location: {geo_info}</p>',
                unsafe_allow_html=True,
            )

            url = product.get("url")
            if url:
                st.markdown(f"[See product]({url})")

            if st.button("Analyze competitors", key=f"analyze_{product['asin']}"):
                st.session_state["analyzing_asin"] = product["asin"]

            _render_price_history_card(product, repo)


def render_products_section(products: Sequence[ProductData], repo: Any) -> None:
    if not products:
        return

    st.markdown("## Scraped Products")

    items_per_page = 8
    total_pages = (len(products) + items_per_page - 1) // items_per_page

    pagination_col, _ = st.columns([0.6, 10.4])
    with pagination_col:
        page = st.number_input("Page", min_value=1, max_value=total_pages, value=1) - 1

    start_index = page * items_per_page
    end_index = min(start_index + items_per_page, len(products))
    st.caption(f"Showing {start_index + 1}-{end_index} of {len(products)} products")

    page_products = products[start_index:end_index]
    today = date.today().isoformat()

    if st.button("Export", key="open_export_dialog"):
        _render_export_dialog(page_products, products, page, today)

    for product in page_products:
        render_product_card(product, repo)


def render_competitor_summary(competitors: Sequence[ProductData]) -> None:
    if not competitors:
        st.caption("No competitors to show.")
        return

    st.markdown("### Competitor Snapshot")
    for competitor in competitors:
        price = competitor.get("price")
        currency = competitor.get("currency", "")
        if isinstance(price, (int, float)):
            price_str = f"{currency} {price:,.2f}" if currency else f"{price:,.2f}"
        else:
            price_str = str(price) if price is not None else "--"

        title = competitor.get("title", competitor.get("asin", "Unknown"))
        st.markdown(f"- **{title}**  \n  Price: `{price_str}`")

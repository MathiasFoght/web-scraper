import streamlit as st
from src.oxylabs_client import scrape_product_details

def render_header():
    st.title("Web Scraper")
    st.caption("Enter your ASIN to get product insights.")

def render_inputs():
    asin = st.text_input("ASIN", placeholder="e.g., B08N5WRWNW")
    geo = st.text_input("ZIP/Postal Code", placeholder="e.g., US")
    domain = st.selectbox("Domain", [
        "com", "ca", "co.uk", "de", "fr", "it", "ae"
    ])
    return asin.strip(), geo.strip(), domain

def main():
    st.set_page_config(page_title="Web Scraper", page_icon=":robot:")
    render_header()
    asin, geo, domain = render_inputs()

    if st.button("Scrape product") and asin:
        with st.spinner("Scraping product..."):
            st.write(f"Scrape")
            product = scrape_product_details(asin, geo, domain)
            st.success("Product scraped successfully!")
            st.write(product)

if __name__ == "__main__":
    main()
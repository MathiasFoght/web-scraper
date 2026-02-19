# Web Scraper API

[**Web Scraper API**](https://oxylabs.io/products/scraper-api/web) is an **all-in-one web data collection platform**. It covers every stage of web scraping, from crawling URLs and bypassing IP blocks to precise data parsing and delivery to your preferred cloud storage. Extract data from **search engines**, **e-commerce sites**, **travel platforms**, and **any other website.**

## Getting started

**Create your API user credentials**: Sign up for a free trial or purchase the product in the [**Oxylabs dashboard**](https://dashboard.oxylabs.io/en/registration) to create your API user credentials (`USERNAME` and `PASSWORD`).

{% hint style="warning" %}
If you need more than one API user for your account, please contact our [**customer support**](mailto:support@oxylabs.io) or message our 24/7 live chat support.
{% endhint %}

### Request samples

Below, you'll find sample cURL requests. For examples in other programming languages, please refer to the relevant sections: [**Amazon**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/targets/amazon), [**Google**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/targets/google), [**Other Websites**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/targets/generic-target).

{% tabs %}
{% tab title="Amazon" %}

```bash
curl 'https://realtime.oxylabs.io/v1/queries' \
--user "USERNAME:PASSWORD" \
-H "Content-Type: application/json" \
-d '{
        "source": "amazon_product",
        "query": "B07FZ8S74R",
        "geo_location": "90210",
        "parse": true
    }'
```

{% endtab %}

{% tab title="Google" %}

```bash
curl 'https://realtime.oxylabs.io/v1/queries' \
--user 'USERNAME:PASSWORD' \
-H 'Content-Type: application/json' \
-d '{
        "source": "google_search",
        "query": "adidas",
        "geo_location": "California,United States",
        "parse": true
    }'
```

{% endtab %}

{% tab title="Other" %}

```bash
curl 'https://realtime.oxylabs.io/v1/queries' \
--user 'USERNAME:PASSWORD' \
-H 'Content-Type: application/json' \
-d '{
        "source": "universal",
        "url": "https://sandbox.oxylabs.io/"
    }'
```

{% endtab %}
{% endtabs %}

We use synchronous [**Realtime**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods/realtime) integration method in our examples. If you would like to use [**Proxy Endpoint**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods/proxy-endpoint) or asynchronous [**Push-Pull**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods/push-pull) integration, refer to the [**integration methods**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods) section.

{% file src="<https://63892162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzrXw45naRpCZ0Ku9AjY1%2Fuploads%2F27TnfuHtFbnGzuppRbXk%2Famazon_product%20output%20example.json?alt=media&token=eafce580-c356-41d7-89b0-37159f0842ed>" %}

{% file src="<https://63892162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzrXw45naRpCZ0Ku9AjY1%2Fuploads%2FpkEoNmfcQTO8G6qT8ihd%2FGeneric%20URL%20output%20example.json?alt=media&token=10267f8e-64e3-4477-84ab-6136389a6c61>" %}

### Request parameter values

1. <mark style="background-color:green;">**source**</mark> - This parameter sets the scraper that will be used to process your request.
2. <mark style="background-color:green;">**URL**</mark> or <mark style="background-color:green;">**query**</mark> - Provide the `URL` or `query` for the type of page you want to scrape. Refer to the table below and the corresponding target sub-pages for detailed guidance on when to use each parameter.
3. Optionally, you can include additional parameters such as `geo_location`, `user_agent_type`, `parse` (find the list of our parsers [**here**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/features/result-processing-and-storage/dedicated-parsers)), `render` and more to customize your scraping request. Read more: [**Features**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/features).

\- mandatory parameter

### Scraping with URLs or parametrized inputs

Oxylabs support two general groups of inputs - URLs and parametrized inputs like queries, product or video IDs. [Generic targets](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/targets/generic-target) which do not have a dedicated source can be scraped with `universal` source.

<table><thead><tr><th width="217">Target</th><th width="246">Source (Scraping URL)</th><th>Source (Using Query, Product or Video ID)</th></tr></thead><tbody><tr><td><a href="web-scraper-api/targets/amazon"><strong>Amazon</strong></a></td><td><code>amazon</code></td><td><p><code>amazon_product</code>,</p><p><code>amazon_search</code>,</p><p><code>amazon_pricing</code>,</p><p><code>amazon_sellers</code>,</p><p><code>amazon_bestsellers</code></p></td></tr><tr><td><a href="web-scraper-api/targets/google"><strong>Google</strong></a></td><td><code>google</code></td><td><p><code>google_search</code>,</p><p><code>google_ads</code>,</p><p><code>google_ai_mode</code>,</p><p><code>google_lens</code>,</p><p><code>google_maps</code>,</p><p><code>google_travel_hotels</code>,</p><p><code>google_trends_explore</code>,</p><p><code>google_shopping_product</code>,</p><p><code>google_shopping_search</code></p></td></tr><tr><td><a href="web-scraper-api/targets/bing"><strong>Bing</strong></a></td><td><code>bing</code></td><td><code>bing_search</code></td></tr><tr><td><a href="web-scraper-api/targets/youtube"><strong>YouTube</strong></a></td><td><code>universal</code></td><td><p><code>youtube_search</code>,</p><p><code>youtube_search_max</code>,</p><p><code>youtube_video_trainability</code>,</p><p><code>youtube_download</code>,</p><p><code>youtube_transcript</code>,</p><p><code>youtube_subtitles</code>,</p><p><code>youtube_metadata</code>,</p><p><code>youtube_channel</code>,</p><p><code>youtube_autocomplete</code></p></td></tr><tr><td><a href="web-scraper-api/targets/chatgpt"><strong>ChatGPT</strong></a></td><td><code>universal</code></td><td><code>chatgpt</code></td></tr><tr><td><a href="web-scraper-api/targets/perplexity"><strong>Perplexity</strong></a></td><td><code>universal</code></td><td><code>perplexity</code></td></tr><tr><td><a href="web-scraper-api/targets/walmart"><strong>Walmart</strong></a></td><td><code>walmart</code></td><td><p><code>walmart_search</code>,</p><p><code>walmart_product</code></p></td></tr><tr><td><a href="web-scraper-api/targets/tiktok"><strong>TikTok</strong></a></td><td><code>universal</code></td><td><p><code>tiktok_shop_search</code>,</p><p><code>tiktok_shop_product</code></p></td></tr><tr><td><a href="web-scraper-api/targets/ebay"><strong>eBay</strong></a></td><td><code>ebay</code></td><td><p><code>ebay_search</code>,</p><p><code>ebay_product</code></p></td></tr><tr><td><a href="web-scraper-api/targets/etsy"><strong>Etsy</strong></a></td><td><code>etsy</code></td><td><p><code>etsy_search</code>,</p><p><code>etsy_product</code></p></td></tr><tr><td><a href="web-scraper-api/targets/north-american-e-commerce/bestbuy"><strong>Best Buy</strong></a></td><td><code>universal</code></td><td><p><code>bestbuy_search</code>,</p><p><code>bestbuy_product</code></p></td></tr><tr><td><a href="web-scraper-api/targets/north-american-e-commerce/bedbathandbeyond"><strong>Bed Bath &#x26; Beyond</strong></a></td><td><code>bedbathandbeyond</code></td><td><code>bedbathandbeyond_search</code>,<br><code>bedbathandbeyond_product</code></td></tr><tr><td><a href="web-scraper-api/targets/north-american-e-commerce/bodega-aurrera"><strong>Bodega Aurrerá</strong></a></td><td><code>bodegaaurrera</code></td><td><code>bodegaaurrera_search</code>,<br><code>bodegaaurrera_product</code></td></tr><tr><td><a href="web-scraper-api/targets/north-american-e-commerce/instacart"><strong>Instacart</strong></a></td><td><code>instacart</code></td><td><code>instacart_search</code>,<br><code>instacart_product</code></td></tr><tr><td><a href="web-scraper-api/targets/north-american-e-commerce/kroger"><strong>Kroger</strong></a></td><td><code>kroger</code></td><td><p><code>kroger_search</code>,</p><p><code>kroger_product</code></p></td></tr><tr><td><a href="web-scraper-api/targets/north-american-e-commerce/lowes"><strong>Lowe's</strong></a></td><td><code>lowes</code></td><td><p><code>lowes_search</code>,</p><p><code>lowes_product</code></p></td></tr><tr><td><a href="web-scraper-api/targets/north-american-e-commerce/publix"><strong>Publix</strong></a></td><td><code>publix</code></td><td><code>publix_search</code>,<br><code>publix_product</code></td></tr><tr><td><a href="web-scraper-api/targets/north-american-e-commerce/target"><strong>Target</strong></a></td><td><code>target</code></td><td><p><code>target_search</code>,</p><p><code>target_product</code>,</p><p><code>target_category</code></p></td></tr><tr><td><a href="web-scraper-api/targets/north-american-e-commerce/grainger"><strong>Grainger</strong></a></td><td><code>grainger</code></td><td><code>grainger_search</code>,<br><code>grainger_product</code></td></tr><tr><td><a href="web-scraper-api/targets/north-american-e-commerce/costco"><strong>Costco</strong></a></td><td><code>costco</code></td><td><p><code>costco_search</code>,</p><p><code>costco_product</code></p></td></tr><tr><td><a href="web-scraper-api/targets/north-american-e-commerce/menards"><strong>Menards</strong></a></td><td><code>menards</code></td><td><code>menards_search</code>,<br><code>menards_product</code></td></tr><tr><td><a href="web-scraper-api/targets/north-american-e-commerce/petco/petco"><strong>Petco</strong></a></td><td><code>universal</code></td><td><code>petco_search</code></td></tr><tr><td><a href="web-scraper-api/targets/north-american-e-commerce/staples"><strong>Staples</strong></a></td><td><code>universal</code></td><td><code>staples_search</code></td></tr><tr><td><a href="web-scraper-api/targets/european-e-commerce/allegro"><strong>Allegro</strong></a></td><td><code>universal</code></td><td><p><code>allegro_search</code>,</p><p><code>allegro_product</code></p></td></tr><tr><td><a href="web-scraper-api/targets/european-e-commerce/idealo"><strong>Idealo</strong></a></td><td><code>universal</code></td><td><code>idealo_search</code></td></tr><tr><td><a href="web-scraper-api/targets/european-e-commerce/mediamarkt"><strong>MediaMarkt</strong></a></td><td><code>mediamarkt</code></td><td><code>mediamarkt_search</code>,<br><code>mediamarkt_product</code></td></tr><tr><td><a href="web-scraper-api/targets/european-e-commerce/cdiscount"><strong>Cdiscount</strong></a></td><td><code>cdiscount</code></td><td><code>cdiscount_search</code>,<br><code>cdiscount_product</code></td></tr><tr><td><a href="web-scraper-api/targets/asian-e-commerce/alibaba"><strong>Alibaba</strong></a></td><td><code>alibaba</code></td><td><code>alibaba_search</code>,<br><code>alibaba_product</code></td></tr><tr><td><a href="web-scraper-api/targets/asian-e-commerce/aliexpress"><strong>AliExpress</strong></a></td><td><code>aliexpress</code></td><td><code>aliexpress_search</code>,<br><code>aliexpress_product</code></td></tr><tr><td><a href="web-scraper-api/targets/asian-e-commerce/indiamart"><strong>IndiaMART</strong></a></td><td><code>indiamart</code></td><td><code>indiamart_search</code>,<br><code>indiamart_product</code></td></tr><tr><td><a href="web-scraper-api/targets/asian-e-commerce/avnet"><strong>Avnet</strong></a></td><td><code>universal</code></td><td><code>avnet_search</code></td></tr><tr><td><a href="web-scraper-api/targets/asian-e-commerce/lazada"><strong>Lazada</strong></a></td><td><code>lazada</code></td><td><code>lazada_search</code>,<br><code>lazada_product</code></td></tr><tr><td><a href="web-scraper-api/targets/asian-e-commerce/rakuten/rakuten"><strong>Rakuten</strong></a></td><td><code>universal</code></td><td><code>rakuten_search</code></td></tr><tr><td><a href="web-scraper-api/targets/asian-e-commerce/tokopedia/tokopedia"><strong>Tokopedia</strong></a></td><td><code>universal</code></td><td><code>tokopedia_search</code></td></tr><tr><td><a href="web-scraper-api/targets/asian-e-commerce/flipkart"><strong>Flipkart</strong></a></td><td><code>flipkart</code></td><td><code>flipkart_search</code>,<br><code>flipkart_product</code></td></tr><tr><td><a href="web-scraper-api/targets/latin-american-e-commerce/mercado-libre/mercadolibre"><strong>MercadoLibre</strong></a></td><td><code>universal</code></td><td><code>mercadolibre_search</code></td></tr><tr><td><a href="web-scraper-api/targets/latin-american-e-commerce/mercado-livre/mercadolivre"><strong>Mercado Livre</strong></a></td><td><code>universal</code></td><td><code>mercadolivre_search</code></td></tr><tr><td><a href="web-scraper-api/targets/latin-american-e-commerce/magazineluiza"><strong>Magazine Luiza</strong></a></td><td><code>magazineluiza</code></td><td><code>magazineluiza_search</code>,<br><code>magazineluiza_product</code></td></tr><tr><td><a href="web-scraper-api/targets/latin-american-e-commerce/falabella"><strong>Falabella</strong></a></td><td><code>falabella</code></td><td><code>falabella_search</code>,<br><code>falabella_product</code></td></tr><tr><td><a href="web-scraper-api/targets/latin-american-e-commerce/dcard"><strong>Dcard</strong></a></td><td><code>universal</code></td><td><code>dcard_search</code></td></tr><tr><td><a href="web-scraper-api/targets/real-estate/airbnb"><strong>Airbnb</strong></a></td><td><code>airbnb</code></td><td><code>airbnb_product</code></td></tr><tr><td><a href="web-scraper-api/targets/real-estate/zillow"><strong>Zillow</strong></a></td><td><code>zillow</code></td><td>Using <code>query</code> parameter is not supported</td></tr><tr><td><a href="web-scraper-api/targets/generic-target"><strong>Other Websites</strong></a></td><td><code>universal</code></td><td>Using <code>query</code> parameter is not supported</td></tr></tbody></table>

{% hint style="info" %}
If you need any assistance in making your first request, feel free to contact us via the 24/7 available live chat.
{% endhint %}

## Testing via Scraper APIs Playground

Try [**Web Scraper API**](https://oxylabs.io/products/scraper-api/web) and [**OxyCopilot**](https://oxylabs.io/products/scraper-api/ai-web-scraper-copilot) in the [**Scraper APIs Playground**](https://dashboard.oxylabs.io/?route=/api-playground).

{% embed url="<https://www.youtube.com/watch?v=kDhknxrod6U>" %}

{% embed url="<https://youtu.be/9JoF8_5r5HY?si=61c3Zkx6FrH06PVa>" %}

## Testing via Postman

Get started with our API using Postman, a handy tool for making HTTP requests. Download our [**Web Scraper API Postman collection**](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzrXw45naRpCZ0Ku9AjY1%2Fuploads%2FMeGA0TZQMcAFHoVhRSQi%2FWeb%20Scraper%20API.new_postman_collection.json?alt=media\&token=9f51d41b-6604-4eef-b6c1-5024cf52c5bf) and import it. This collection includes examples that demonstrate the functionality of the scraper. Customize the examples to your needs or start scraping right away.

For step-by-step instructions, watch our video tutorial below. If you're new to Postman, check out this short [**guide**](https://developers.oxylabs.io/guides-for-scraper-apis/using-postman).

{% embed url="<https://www.youtube.com/watch?v=WOD0mZnu-j0>" %}

{% hint style="info" %}
*All information herein is provided on an "as is" basis and for informational purposes only. We make no representation and disclaim all liability with respect to your use of any information contained on this page. Before engaging in scraping activities of any kind you should consult your legal advisors and carefully read the particular website's terms of service or receive a scraping license.*
{% endhint %}

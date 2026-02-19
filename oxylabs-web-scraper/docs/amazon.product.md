# Product

The `amazon_product` data source is designed to retrieve Amazon product pages.

## Request samples

In the samples below, we make a request to retrieve product page for ASIN `B08Y72CH1F` on `amazon.nl` marketplace. In case the ASIN provided is a parent ASIN, we ask Amazon to return a product page of an automatically-selected variation. API will return parsed results.

{% tabs %}
{% tab title="cURL" %}

```bash
curl 'https://realtime.oxylabs.io/v1/queries' \
--user 'USERNAME:PASSWORD' \
-H 'Content-Type: application/json' \
-d '{
        "source": "amazon_product",
        "domain": "nl",
        "query": "B08Y72CH1F",
        "parse": true,
        "context": [
            {
                "key": "autoselect_variant",
                "value": true
            }
        ]
    }'
```

{% endtab %}

{% tab title="Python" %}

```python
import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'amazon_product',
    'domain': 'nl',
    'query': 'B08Y72CH1F',
    'parse': True,
    'context': [
        {'key': 'autoselect_variant', 'value': True}
    ],
}


# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('USERNAME', 'PASSWORD'),
    json=payload,
)

# Print prettified response to stdout.
pprint(response.json())
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const https = require("https");

const username = "USERNAME";
const password = "PASSWORD";
const body = {
    source: "amazon_product",
    domain: "nl",
    query: "B08Y72CH1F",
    parse: true,
    context: [
        { key: "autoselect_variant", value: true },
    ],
};

const options = {
    hostname: "realtime.oxylabs.io",
    path: "/v1/queries",
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        Authorization:
            "Basic " + Buffer.from(`${username}:${password}`).toString("base64"),
    },
};

const request = https.request(options, (response) => {
    let data = "";

    response.on("data", (chunk) => {
        data += chunk;
    });

    response.on("end", () => {
        const responseData = JSON.parse(data);
        console.log(JSON.stringify(responseData, null, 2));
    });
});

request.on("error", (error) => {
    console.error("Error:", error);
});

request.write(JSON.stringify(body));
request.end();
```

{% endtab %}

{% tab title="HTTP" %}

```http
https://realtime.oxylabs.io/v1/queries?source=amazon_product&domain=nl&query=B08Y72CH1F&parse=true&context[0][key]=autoselect_variant&context[0][value]=true&access_token=12345abcde
```

{% endtab %}

{% tab title="PHP" %}

```php
<?php

$params = array(
    'source' => 'amazon_product',
    'domain' => 'nl',
    'query' => 'B08Y72CH1F',
    'parse' => true,
    'context' => [
        ['key' => 'autoselect_variant', 'value' => true]
    ]
);

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, "https://realtime.oxylabs.io/v1/queries");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($params));
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_USERPWD, "USERNAME" . ":" . "PASSWORD");

$headers = array();
$headers[] = "Content-Type: application/json";
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

$result = curl_exec($ch);
echo $result;

if (curl_errno($ch)) {
    echo 'Error:' . curl_error($ch);
}
curl_close($ch);
```

{% endtab %}

{% tab title="Golang" %}

```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	const Username = "USERNAME"
	const Password = "PASSWORD"

	payload := map[string]interface{}{
		"source": "amazon_product",
		"domain": "nl",
		"query":  "B08Y72CH1F",
		"parse":  true,
		"context": []map[string]interface{}{
			{"key": "autoselect_variant", "value": true},
		},
	}

	jsonValue, _ := json.Marshal(payload)

	client := &http.Client{}
	request, _ := http.NewRequest("POST",
		"https://realtime.oxylabs.io/v1/queries",
		bytes.NewBuffer(jsonValue),
	)

	request.SetBasicAuth(Username, Password)
	response, _ := client.Do(request)

	responseText, _ := ioutil.ReadAll(response.Body)
	fmt.Println(string(responseText))
}

```

{% endtab %}

{% tab title="C#" %}

```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Json;
using System.Threading.Tasks;

namespace OxyApi
{
    class Program
    {
        static async Task Main()
        {
            const string Username = "USERNAME";
            const string Password = "PASSWORD";

            var parameters = new {
                source = "amazon_product",
                domain = "nl",
                query = "B08Y72CH1F",
                parse = true,
                context = new dynamic [] {
                    new { key = "autoselect_variant", value = true },
                }
            };

            var client = new HttpClient();

            Uri baseUri = new Uri("https://realtime.oxylabs.io");
            client.BaseAddress = baseUri;

            var requestMessage = new HttpRequestMessage(HttpMethod.Post, "/v1/queries");
            requestMessage.Content = JsonContent.Create(parameters);

            var authenticationString = $"{Username}:{Password}";
            var base64EncodedAuthenticationString = Convert.ToBase64String(System.Text.ASCIIEncoding.UTF8.GetBytes(authenticationString));
            requestMessage.Headers.Add("Authorization", "Basic " + base64EncodedAuthenticationString);

            var response = await client.SendAsync(requestMessage);
            var contents = await response.Content.ReadAsStringAsync();

            Console.WriteLine(contents);
        }
    }
}
```

{% endtab %}

{% tab title="Java" %}

```java
package org.example;

import okhttp3.*;
import org.json.JSONArray;
import org.json.JSONObject;
import java.util.concurrent.TimeUnit;

public class Main implements Runnable {
    private static final String AUTHORIZATION_HEADER = "Authorization";
    public static final String USERNAME = "USERNAME";
    public static final String PASSWORD = "PASSWORD";
    public void run() {
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("source", "amazon_product");
        jsonObject.put("domain", "nl");
        jsonObject.put("query", "B08Y72CH1F");
        jsonObject.put("parse", true);
        jsonObject.put("context", new JSONArray().put(
                new JSONObject()
                        .put("key", "autoselect_variant")
                        .put("value", true)
        ));

        Authenticator authenticator = (route, response) -> {
            String credential = Credentials.basic(USERNAME, PASSWORD);

            return response
                    .request()
                    .newBuilder()
                    .header(AUTHORIZATION_HEADER, credential)
                    .build();
        };

        var client = new OkHttpClient.Builder()
                .authenticator(authenticator)
                .readTimeout(180, TimeUnit.SECONDS)
                .build();

        var mediaType = MediaType.parse("application/json; charset=utf-8");
        var body = RequestBody.create(jsonObject.toString(), mediaType);
        var request = new Request.Builder()
                .url("https://realtime.oxylabs.io/v1/queries")
                .post(body)
                .build();

        try (var response = client.newCall(request).execute()) {
            if (response.body() != null) {
                try (var responseBody = response.body()) {
                    System.out.println(responseBody.string());
                }
            }
        } catch (Exception exception) {
            System.out.println("Error: " + exception.getMessage());
        }

        System.exit(0);
    }

    public static void main(String[] args) {
        new Thread(new Main()).start();
    }
}
```

{% endtab %}

{% tab title="JSON" %}

```json
{
    "source": "amazon_product", 
    "domain": "nl", 
    "query": "B08Y72CH1F",
    "parse": true, 
    "context": [
        {
            "key": "autoselect_variant", 
            "value": true
        }
    ]
}
```

{% endtab %}
{% endtabs %}

We use synchronous [**Realtime**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods/realtime) integration method in our examples. If you would like to use [**Proxy Endpoint**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods/proxy-endpoint) or asynchronous [**Push-Pull**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods/push-pull) integration, refer to the [**integration methods**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods) section.

## Request parameter values

### Generic

Basic setup and customization options for scraping Amazon product pages.

<table><thead><tr><th width="222">Parameter</th><th width="350.3333333333333">Description</th><th>Default Value</th></tr></thead><tbody><tr><td><mark style="background-color:green;"><strong>source</strong></mark></td><td>Sets the scraper.</td><td><code>amazon_product</code></td></tr><tr><td><mark style="background-color:green;"><strong>query</strong></mark></td><td>10-symbol ASIN code.</td><td>-</td></tr><tr><td><code>render</code></td><td>Enables JavaScript rendering when set to <code>html</code>. <a href="../../features/js-rendering-and-browser-control/javascript-rendering"><strong>More info</strong></a><strong>.</strong></td><td>-</td></tr><tr><td><code>parse</code></td><td>Returns parsed data when set to <code>true</code>. Explore output <a href="#output-data-dictionary"><strong>data dictionary</strong></a>.</td><td><code>false</code></td></tr><tr><td><code>callback_url</code></td><td>URL to your callback endpoint. <a href="../../../integration-methods/push-pull#callback"><strong>More info</strong></a>.</td><td>-</td></tr><tr><td><code>user_agent_type</code></td><td>Device type and browser. The full list can be found <a href="../../features/http-context-and-job-management/user-agent-type"><strong>here</strong></a>.</td><td><code>desktop</code></td></tr></tbody></table>

&#x20;    \- mandatory parameter

### Localization

Adapt results to specific geographical locations, domains, languages.

| Parameter      | Description                                                                                                                                                                                                          | Default Value |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `geo_location` | The *Deliver to* location. See our guide to using this parameter [**here**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/features/localization/e-commerce-localization)**.**                     | -             |
| `domain`       | Domain localization for Amazon. The full list of available domains can be found [**here**](https://developers.oxylabs.io/scraping-solutions/features/localization/domain-locale-results-language#domain).            | `com`         |
| `locale`       | `Accept-Language` header value, which sets the interface language of the Amazon page. [**More info**](https://developers.oxylabs.io/scraping-solutions/features/localization/domain-locale-results-language#locale). | -             |

{% hint style="warning" %}
**IMPORTANT:** On most page types, Amazon tailors the returned results based on the delivery location of their customers. Therefore, we advise using the `geo_location` parameter to set your preferred delivery location. You can read more about using `geo_location` with Amazon [**here**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/features/localization/e-commerce-localization).
{% endhint %}

### Other

Additional advanced settings and controls for specialized requirements.

<table><thead><tr><th>Parameter</th><th width="259.3333333333333">Description</th><th>Default Value</th></tr></thead><tbody><tr><td><code>context</code>:<br><code>autoselect_variant</code></td><td>To get accurate pricing/buybox data, set this parameter to <code>true</code> (which tells us to append the <code>th=1&#x26;psc=1</code> URL parameters to the end of the product URL). To get an accurate representation of the parent ASIN's product page, omit this parameter or set it to <code>false</code>.</td><td><code>false</code></td></tr><tr><td><code>context</code>:<br><code>currency</code></td><td>Sets the currency. Check the available values <a href="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzrXw45naRpCZ0Ku9AjY1%2Fuploads%2FNNybEQaVnTrc9ymR1NGE%2Fcurrency_new.json?alt=media&#x26;token=a77440f9-50a5-4e07-9993-b2db2144800b"><strong>here</strong></a>.</td><td>Depends on the marketplace. Check the default values <a href="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzrXw45naRpCZ0Ku9AjY1%2Fuploads%2FNNybEQaVnTrc9ymR1NGE%2Fcurrency_new.json?alt=media&#x26;token=a77440f9-50a5-4e07-9993-b2db2144800b"><strong>here</strong></a>.</td></tr></tbody></table>

#### Code example

```json
{
    "source": "amazon_product",
    "domain": "de",
    "query": "B0CW1QC1V1",
    "parse": true,
    "context": [
        {
            "key": "currency",
            "value": "AUD"
        }
    ]
}
```

## Structured data

Web Scraper API is capable of extracting either an HTML or JSON object that contains Amazon product results, offering structured data on various elements of the results page.

<details>

<summary><code>amazon_product</code> structured output</summary>

```json
{
    "url": "https://www.amazon.in/dp/B073GZNWL1",
    "page": 1,
    "page_type": "Product",
    "asin": "B073GZNWL1",
    "asin_in_url": "B073GZNWL1",
    "title": "Pampers Large Size Diapers Pants (128 Count)",
    "manufacturer": "Pampers",
    "product_name": "Pampers Large Size Diapers Pants (128 Count)",
    "description": "Size: Large | Unit Count: 128 New Pampers baby dry pants style diapers have 3 revolutionary extra absorb channels, that help distribute wetness evenly throughout the pants diapers, so wetness doesn't collect in one place. Their magic gel layer locks wetness inside and offers up to 12 hours of dryness to help your baby sleep soundly all night.",
    "bullet_points": "Revolutionary 3 extra absorb channels that help distribute wetness evenly\nThese diaper pants have magic gel that locks wetness away for up to 12 hours of dryness\nFlexible waist band on these diaper pants adapts to baby's movements for comfortable fit\nBreathable soft belt and leg cuffs to help air circulate and keep your baby's skin fresh\nBaby lotion that moisturizes and nourishes your baby's skin to protect it from diaper rash and irritation",
    "category": [
        {
            "ladder": [
                {
                    "name": "Baby",
                    "url": "/Baby/b/ref=dp_bc_1?ie=UTF8&node=1571274031"
                },
                ...
                {
                    "name": "Diaper Pants",
                    "url": "/Training-Diapers/b/ref=dp_bc_4?ie=UTF8&node=1953352031"
                }
            ]
        }
    ],
    "variation": [
        {
            "asin": "B06XRGX8FC",
            "selected": false,
            "dimensions": {
                "Size": "Large",
                "Unit Count": "68"
            }
        },
        ...
        {
            "asin": "B01CFYRJTI",
            "selected": false,
            "dimensions": {
                "Size": "Small",
                "Unit Count": "42"
            }
        }
    ],
    "rating": 4.3,
    "price": 1299.0,
    "price_upper": 1299.0,
    "price_sns": 1299.6,
    "price_initial": 1999.0,
    "price_shipping": 0.0,
    "price_buybox": 1368.0,
    "deal_type": "Deal Price",
    "coupon": "",
    "is_prime_pantry": false,
    "is_prime_eligible": true,
    "is_addon_item": false,
    "currency": "INR",
    "discount_end": "2017-11-30T16:30:02+00:00",
    "stock": "In stock.",
    "other_sellers": "New & Open Box (50) from $46.61",
    "reviews_count": 13270,
    "top_review": "Baby feels comfortable wearing pampers during playtime as well as sleeping time. Induce far lesser rashes than any other brands in this range. Each diaper functions well for minimum 5 HRS depending upon pee frequency. Received original product with latest manufacturing date. I appreciate Amazon for maintaining high quality of product as well as services.Read more",
    "answered_questions_count": 152,
    "pricing_count": 4,
    "pricing_url": "https://www.amazon.in/gp/offer-listing/B073GZNWL1/ref=dp_olp_new?ie=UTF8&condition=new",
    "pricing_str": "4 offers from 1,368.00",
    "featured_merchant": {
        "name": "Cloudtail India",
        "seller_id": "AT95IG9ONZD7S",
        "link": "/gp/help/seller/at-a-glance.html/ref=dp_merchant_link?ie=UTF8&seller=AT95IG9ONZD7S&isAmazonFulfilled=1",
        "is_amazon_fulfilled": true,
        "shipped_from": "Amazon"
    },
    "sales_rank": [
        {
            "rank": 11,
            "ladder": [
                {
                    "url": "https://www.amazon.in/gp/bestsellers/baby/ref=pd_dp_ts_baby_1",
                    "name": "Baby Products"
                }
            ]
        },
        {
            "rank": 10,
            "ladder": [
                {
                    "url": "https://www.amazon.in/gp/bestsellers/baby/ref=pd_zg_hrsr_baby_1_1",
                    "name": "Baby Products"
                },
                ...
                {
                    "url": "https://www.amazon.in/gp/bestsellers/baby/1953352031/ref=pd_zg_hrsr_baby_1_4_last",
                    "name": "Diaper Pants"
                }
            ]
        }
    ],
    "sns_discounts": [],
    "developer_info": {},
    "images": [
        "https://images-na.ssl-images-amazon.com/images/I/81%2B12fymboL._SL1500_.jpg",
        ...
        "https://images-na.ssl-images-amazon.com/images/I/71vYb-QJA8L._SL1500_.jpg"
    ],
    "has_videos": false,
    "delivery": [],
    "parse_status_code": 12000,
    "rating_stars_distribution": [
        {
            "rating": 5,
            "percentage": 69
        },
        ...
    ],
    "lightning_deal": {
        "percent_claimed": "13%",
        "price_text": "1,299.00  (Save 35%)",
        "expires": "Ends in  06h 44m 39s"
    },
    "max_quantity": 2,
    "amazon_choice": true,
    "ads": [
        {
            "type": "sponsored_products",
            "location": "carousel",
            "title": "Johnson's Baby Skincare Wipes, 2*80 cloth wipes (Pack of 2, Rs. 60 off)",
            "asin": "B00EZQ5DD4",
            "images": [
                "https://images-eu.ssl-images-amazon.com/images/I/411DD3w9xLL._AC_SR150,150_.jpg"
            ],
            "pos": 1,
            "rating": 4.5,
            "reviews_count": 1864,
            "is_prime_eligible": true,
            "price": 310.0,
            "price_upper": 310.0
        },
        ...
        {
            "type": "sponsored_products_bottom",
            "location": "carousel",
            "title": "Pampers Extra Small Size Premium New Born Care Diaper Pants (24 Count)",
            "asin": "B01CFX8ELQ",
            "images": [
                "https://images-eu.ssl-images-amazon.com/images/I/51Iz8Ua9s5L._AC_SR150,150_.jpg"
            ],
            "pos": 1,
            "rating": 4.5,
            "reviews_count": 4881,
            "is_prime_eligible": true,
            "price": 221.0,
            "price_upper": 221.0
        },
        ...
        {
            "type": "organic_also_viewed",
            "location": "carousel",
            "title": "Mee Mee Caring Baby Wet Wipes with Aloe Vera (72 pcs) (Pack of 3)",
            "asin": "B00DRE0LQY",
            "images": [
                "https://images-na.ssl-images-amazon.com/images/I/61mtV3nCAjL._AC_UL160_SR120,160_.jpg"
            ],
            "pos": 1,
            "rating": 4.2,
            "reviews_count": 4243,
            "is_prime_eligible": true,
            "price": 275.0,
            "price_upper": 275.0
        },
        ...
        {
            "type": "organic_also_viewed",
            "location": "carousel",
            "title": "Pampers New Baby Diapers (24 Count)",
            "asin": "B00AWMBLZ4",
            "images": [
                "https://images-na.ssl-images-amazon.com/images/I/81dt5zb3ybL._AC_UL160_SR160,160_.jpg"
            ],
            "pos": 12,
            "rating": 4.1,
            "reviews_count": 9176,
            "is_prime_eligible": true,
            "price": 284.0,
            "price_upper": 284.0
        }
    ],
    "parent_asin": "B0752ZNPBR"
}
```

</details>

## Output data dictionary

Navigate through the details using the right-side navigation or scrolling down the page.

{% hint style="info" %}
In the following sections, parsed JSON code snippets are shortened where more than one item for the result type is available.
{% endhint %}

#### HTML example

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfZfOFjFbSOaxVdAZ1xbMzSesn5V_Rhyrt9CTLQzVHkm-3qNDH9kblqmSKaEvVaMrxagZOaoXsxnSjG_TLZX_mlsSbeIKkBpqMeniQYAY6bex0ol7-sbLpP1LxNqaPK1Rs4zEJT5QuBo15VqF1oHiRUZxg?key=6Frx2zsHA3l2U3hK0m1qkw" alt=""><figcaption></figcaption></figure>

#### JSON Structure

The table below presents a detailed list of each Amazon product page element we parse, including its description, data type, and whether the element is always present in the layout or optional depending on the product you choose to scrape. The table also includes some metadata.

<table><thead><tr><th width="233">Key</th><th width="301">Description</th><th width="107">Type</th><th>Layout</th></tr></thead><tbody><tr><td><code>url</code></td><td>The URL of the Amazon product.</td><td>string</td><td><br></td></tr><tr><td><code>page</code></td><td>The current page number.</td><td>integer</td><td><br></td></tr><tr><td><code>page_type</code></td><td>Identifies the type of the Amazon page.</td><td>string</td><td><br></td></tr><tr><td><code>asin</code></td><td>Amazon Standard Identification Number.</td><td>string</td><td><br></td></tr><tr><td><code>asin_in_url</code></td><td>Extracts the Amazon Standard Identification Number from the URL.</td><td>string</td><td><br></td></tr><tr><td><code>title</code></td><td>The title of the product.</td><td>string</td><td><br></td></tr><tr><td><code>manufacturer</code></td><td>The name of the manufacturer of the product.</td><td>string</td><td><br></td></tr><tr><td><code>product_name</code></td><td>The name of the product.</td><td>string</td><td><br></td></tr><tr><td><code>description</code></td><td>The description of the product, parsed from the 'Product description' section.</td><td>string</td><td><br></td></tr><tr><td><code>bullet_points</code></td><td>The bullet point items parsed from the 'About this product' section.</td><td>string</td><td>optional</td></tr><tr><td><code>category</code></td><td>A list containing the more details on the category of the Amazon product.</td><td>array</td><td>optional</td></tr><tr><td><code>variation</code></td><td>A list containing more details on the variations of the Amazon product.</td><td>array</td><td>optional</td></tr><tr><td><code>rating</code></td><td>The rating of the product.</td><td>integer</td><td><br></td></tr><tr><td><code>price</code></td><td>The price of the product.</td><td>float</td><td><br></td></tr><tr><td><code>price_upper</code></td><td>The upper limit of the price.</td><td>float</td><td>optional</td></tr><tr><td><code>price_sns</code></td><td>Identifies if product is a part of 'Subscribe &#x26; Save' program.</td><td>float</td><td><br></td></tr><tr><td><code>price_initial</code></td><td>The original, non-discounted price of a product.</td><td>float</td><td><br></td></tr><tr><td><code>price_shipping</code></td><td>The price of the shipping.</td><td>float</td><td>optional</td></tr><tr><td><code>price_buybox</code></td><td>The price of the product as visible in the buybox.</td><td>float</td><td><br></td></tr><tr><td><code>deal_type</code></td><td>Identifies the category of promotional offer.</td><td>string</td><td>optional</td></tr><tr><td><code>coupon</code></td><td>Indicates any digital discounts available.</td><td>string</td><td>optional</td></tr><tr><td><code>is_prime_eligible</code></td><td>Indicates whether the product is eligible for Amazon Prime.</td><td>boolean</td><td><br></td></tr><tr><td><code>is_addon_item</code></td><td>Indicates whether a product is available for purchase only when included in orders meeting a minimum value threshold.</td><td>boolean</td><td>optional</td></tr><tr><td><code>currency</code></td><td>The currency in which the price is denominated.</td><td>string</td><td><br></td></tr><tr><td><code>discount_end</code></td><td>Indicates the final date on which a promotional discount for an Amazon product is valid till.</td><td>string</td><td>optional</td></tr><tr><td><code>stock</code></td><td>Indicates the inventory level of the product.</td><td>string</td><td><br></td></tr><tr><td><code>reviews_count</code></td><td>The count of reviews for the product.</td><td>integer</td><td><br></td></tr><tr><td><code>reviews</code></td><td>A list of reviews with their respective details.</td><td>array</td><td></td></tr><tr><td><code>answered_questions_count</code></td><td>The total number of customer questions about an Amazon product that have been answered.</td><td>integer</td><td>optional</td></tr><tr><td><code>pricing_count</code></td><td>The count of offers for the product.</td><td>integer</td><td>optional</td></tr><tr><td><code>pricing_url</code></td><td>The URL to retrieve Amazon product offer listings.</td><td>string</td><td>optional</td></tr><tr><td><code>pricing_str</code></td><td>A string representation of the pricing details for an Amazon product. This attribute includes information on the current price, any discounts, promotions, and special offers</td><td>string</td><td>optional</td></tr><tr><td><code>featured_merchant</code></td><td>A list of details on the primary seller or vendor highlighted for an Amazon product.</td><td>object</td><td>optional</td></tr><tr><td><code>sales_rank</code></td><td>A list of information about the ranking position of an Amazon product within its respective category based on its sales performance.</td><td>array</td><td>optional</td></tr><tr><td><code>sns_discounts</code></td><td>Indicates any discounts available as part of the 'Subscribe &#x26; Save' program.</td><td>array</td><td><br></td></tr><tr><td><code>developer_info</code></td><td>Information related to the developer or manufacturer of an Amazon product.</td><td>object</td><td>optional</td></tr><tr><td><code>images</code></td><td>A list of URLs indicating the product images.</td><td>array</td><td><br></td></tr><tr><td><code>product_overview</code></td><td>A list of key attributes and their descriptions for the product, providing essential details about the product's characteristics.</td><td>array</td><td>optional</td></tr><tr><td><code>store_url</code></td><td>The URL of the seller's store web page.</td><td>string</td><td>optional</td></tr><tr><td><code>has_videos</code></td><td>Indicates if the product has any videos.</td><td>boolean</td><td><br></td></tr><tr><td><code>delivery</code></td><td>A list of information on the delivery options.</td><td>object</td><td>optional</td></tr><tr><td><code>brand</code></td><td>The brand of the product.</td><td>string</td><td>optional</td></tr><tr><td><code>item_form</code></td><td>Specifies the physical form or type of the product, detailing how it is packaged or delivered for use.</td><td>string</td><td>optional</td></tr><tr><td><code>sales_volume</code></td><td>The quantity of units sold within a specific timeframe.</td><td>string</td><td>optional</td></tr><tr><td><code>other_sellers</code></td><td>Details of other sellers listing the product, including the count of sellers, starting price among them, and basic shipping information.</td><td>string</td><td>optional</td></tr><tr><td><code>rating_stars_distribution</code></td><td>A list of details on the ratings of the product.</td><td>array</td><td>optional</td></tr><tr><td><code>buybox</code></td><td>A list of details on the product's pricing.</td><td>array</td><td>optional</td></tr><tr><td><code>lightning_deal</code></td><td>Indicates whether there is a time-limited promotional offer available for the product.</td><td>object</td><td>optional</td></tr><tr><td><code>product_details</code></td><td>A list of information on the details of the product.</td><td>object</td><td>optional</td></tr><tr><td><code>product_dimensions</code></td><td>The dimensions of the product.</td><td>string</td><td>optional</td></tr><tr><td><code>max_quantity</code></td><td>The maximum number of units of an Amazon product that a customer is allowed to purchase in a single order.</td><td>integer</td><td>optional</td></tr><tr><td><code>warranty_and_support</code></td><td>A list of details on the warranty of the product.</td><td>object</td><td>optional</td></tr><tr><td><code>discount.percentage</code></td><td>The percentage reduction applied to the original price of an Amazon product.</td><td>integer</td><td>optional</td></tr><tr><td><code>amazon_choice</code></td><td>Indicates if the product has the Amazon's Choice badge.</td><td>boolean</td><td>optional</td></tr><tr><td><code>coupon_discount_percentage</code></td><td>Indicates the percentage reduction amount applicable with a coupon.</td><td>integer</td><td>optional</td></tr><tr><td><code>parent_asin</code></td><td>The primary identifier for Amazon product family which a product is attributed to.</td><td>string</td><td>optional</td></tr><tr><td><code>created_at</code></td><td>The timestamp when the scraping job was created.</td><td>timestamp</td><td><br></td></tr><tr><td><code>updated_at</code></td><td>The timestamp when the scraping job was finished.</td><td>timestamp<br></td><td><br></td></tr><tr><td><code>job_id</code></td><td>The ID of the job associated with the scraping job.</td><td>string</td><td><br></td></tr><tr><td><code>status_code</code></td><td>The status code of the scraping job. You can see the scraper status codes described <a href="../../../response-codes#api"><strong>here</strong></a>.</td><td>integer</td><td><br></td></tr><tr><td><code>parse_status_code</code></td><td>The status code of the parsing job. You can see the parser status codes described <a href="../../../response-codes#parsers"><strong>here</strong></a>.</td><td>integer</td><td><br></td></tr></tbody></table>

### Category

This field shows the hierarchical structure of product categories for an Amazon product. Each category in the ladder is an object with a name and URL, representing the path from the broadest category to the most specific subcategory.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdK4sTM7yRyVzp0Ie1eZ312F-n0B5ew61C2GK_yeX5KKQQpwUvFCaIlSVlQW1zlVialMLnErf1wqcdCpdKgVB4a1lLz1XhjbtSIgmcOQWZBlr8PYPD107e5yb-iJhb6t_GIQXhRmccljF1zC5BEsLZQSfob?key=6Frx2zsHA3l2U3hK0m1qkw" alt="" width="375"><figcaption></figcaption></figure>

```json
 "category": [
        {
            "ladder": [
                {
                    "name": "Office Products",
                    "url": "/office-products-supplies-electronics-furniture/b/ref=dp_bc_aui_C_1/133-6156367-1346746?ie=UTF8&node=1064954"
                },
                {
                    "name": "Office & School Supplies",
                    "url": "/Office-Supplies/b/ref=dp_bc_aui_C_2/133-6156367-1346746?ie=UTF8&node=1069242"
                },
                {
                    "name": "Paper",
                    "url": "/b/ref=dp_bc_aui_C_3/133-6156367-1346746?ie=UTF8&node=1069664"
                },
                {
                    "name": "Notebooks & Writing Pads",
                    "url": "/Notebooks-Writing-Pads/b/ref=dp_bc_aui_C_4/133-6156367-1346746?ie=UTF8&node=1069756"
                },
                {
                    "name": "Hardcover Executive Notebooks",
                    "url": "/Hardcover-Executive-Notebooks/b/ref=dp_bc_aui_C_5/133-6156367-1346746?ie=UTF8&node=490755011"
                }
            ]
        }
    ],
```

<table><thead><tr><th>Key (category)</th><th width="352">Description</th><th>Type</th></tr></thead><tbody><tr><td><code>ladder</code></td><td>A list containing breadcrumbs of the Amazon product.</td><td>array</td></tr><tr><td><code>ladder.name</code></td><td>The name of the breadcrumb/category of the Amazon product.</td><td>string</td></tr><tr><td><code>ladder.url</code></td><td>The URL of the breadcrumb/category.</td><td>string</td></tr></tbody></table>

### Ads

This field contains information about ads displayed on an Amazon product page. Each ad is represented as an object with details such as type, location, title, ASIN, images, position, rating, reviews count, Prime eligibility, and price.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdxp_sgouBLpzRZ77q730hJJan57OYKkoY_5hemT2kOR_7tWwO0IoHGd41UFoITH3I10mHbtvypEUaehf7t4pgNnEGbaV8phw0-r92ih2-Y_y5a4HAU1SOvwd2t6l_bxI4O85p8c9OS_1yyEmoFEbxWgSOo?key=6Frx2zsHA3l2U3hK0m1qkw" alt="" width="563"><figcaption></figcaption></figure>

```json
...                   
  "ads": [
        {
            "type": "organic_also_viewed",
            "location": "carousel",
            "title": "Camkix Tangentbordsrengöringssats – 1 x miniborste, 1 x rengöringsborste, 1 x tangentbordslockborttagare, 1 x luftfläkt och 1 x rengöringsduk – även för bärbara datorer, kameralinser, glasögon – hem och kontor",
            "asin": "B07SRV9HQ4",
            "images": [
                "https://images-eu.ssl-images-amazon.com/images/I/81t5eLB69SL._AC_UL160_SR160,160_.jpg"
            ],
            "pos": 1,
            "rating": 4.3,
            "reviews_count": 840,
            "is_prime_eligible": false,
            "price": 134.99,
            "price_upper": 134.99
        },
...
]
...
```

<table><thead><tr><th width="224">Key (ads)</th><th width="372">Description</th><th>Type</th></tr></thead><tbody><tr><td><code>type</code></td><td>The type of the Amazon ad.</td><td>string</td></tr><tr><td><code>location</code></td><td>The name of the Amazon ad placement.</td><td>string</td></tr><tr><td><code>title</code></td><td>The title of the product.</td><td>string</td></tr><tr><td><code>asin</code></td><td>Amazon Standard Identification Number.</td><td>string</td></tr><tr><td><code>images</code></td><td>The URL of the product image/images.</td><td>string</td></tr><tr><td><code>pos</code></td><td>A unique indicator denoting the position of an ad in regards to all available ads results.</td><td>integer</td></tr><tr><td><code>rating</code></td><td>The rating of the product.</td><td>integer</td></tr><tr><td><code>reviews_count</code></td><td>The count of reviews for the product.</td><td>integer</td></tr><tr><td><code>is_prime_eligible</code></td><td>Indicates whether the product is eligible for Amazon Prime.</td><td>boolean</td></tr><tr><td><code>price</code></td><td>The price of the product.</td><td>float</td></tr><tr><td><code>price_upper</code></td><td>The upper limit of the price if applicable.</td><td>float</td></tr></tbody></table>

### Rating Stars Distribution

This field contains the distribution of star ratings for a product. Each object represents a star rating and the percentage of total reviews that gave this rating.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcn5S9A_dM-Lv0NYIxZ26LjXsQwB08jjaiOLL2MFWqqNG3LvFq0YvmSxztIlD1uHjPDUu171MCzsrS50TiMDkPpNXF6wxF_lMVxu8UGpYtOVwMDRgTbo_vGl64K_hpDpXkNCAJNCaNb4KsqH-Arx7jEvw?key=6Frx2zsHA3l2U3hK0m1qkw" alt="" width="375"><figcaption></figcaption></figure>

```json
...
 "rating_stars_distribution": [
        {
            "rating": 5,
            "percentage": 87
        },
        {
            "rating": 4,
            "percentage": 8
        },
        {
            "rating": 3,
            "percentage": 2
        },
        {
            "rating": 2,
            "percentage": 1
        },
        {
            "rating": 1,
            "percentage": 2
        }
    ],
...

```

<table><thead><tr><th>Key (rating_stars_distribution)</th><th width="338">Description</th><th>Type</th></tr></thead><tbody><tr><td><code>rating</code></td><td>Indicates the rating number (scale from 5 to 1).</td><td>integer</td></tr><tr><td><code>percentage</code></td><td>Indicates the percentage rate for the specific rating.</td><td>string</td></tr></tbody></table>

### Reviews

Contains customer reviews for the product, with each review represented as an object containing relevant details.

<figure><img src="https://63892162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzrXw45naRpCZ0Ku9AjY1%2Fuploads%2FxPyFxE7sapivIEkXsiPZ%2FScreenshot%202024-11-18%20at%2017.25.56.png?alt=media&#x26;token=35068517-f443-44b4-9bfa-6a5b929d4718" alt="" width="551"><figcaption></figcaption></figure>

```json
"reviews": [
    {
        "id": "R22S287L9EGVTJ",
        "title": "5.0 out of 5 stars Good keyboard",
        "author": "JeffreyK",
        "rating": 5,
        "content": "Keyboard has been good so far. No problems. I read about the issue where the keyboard would spam keys. I think this is an issue with either messy macros and setting the actuation to low. I notice that sometimes, some of the keys are pressed around 0.2 mm without me pressing them. Might be the weight of the keycaps.If this is the case, if the actuation was set to 0.2mm, it would continuously register that press. Since I put my actuation at 1.4mm, it isn't a problem. However, I've only had the keyboard for a week. No issues so far.I'm used to tactile switches like MX Browns. The issue with linear switches like this one, is that sometimes I accidentally press keys because I can't feel the actuation of the keys. With these, since I can set their actuation. Accidental key press is not a problem. The rapid trigger is also pretty awesome. In games like Valorant/CS 2, it allows me to counterstrafe more consistently and quickly. I can juke right on the spot quickly. With a normal mech keyboard, it's not always spot on and consistent like that. Read more",
        "timestamp": "Reviewed in the United States May 9, 2024",
        "profile_id": "AH6T74ODE6XN2YQULBDPYJW7LNUQ",
        "is_verified": false,
        "review_from": "Top reviews from the United States"
    },
...
```

<table><thead><tr><th width="230">Key (reviews)</th><th width="399">Description</th><th>Type</th></tr></thead><tbody><tr><td><code>id</code></td><td>An alphanumeric identification for the Amazon Review.</td><td>string</td></tr><tr><td><code>title</code></td><td>The rating and the title of the review.</td><td>string</td></tr><tr><td><code>author</code></td><td>The user by whom the review has been submitted.</td><td>string</td></tr><tr><td><code>rating</code></td><td>The star rating assigned when submitting the review, typically between 1 and 5.</td><td>integer</td></tr><tr><td><code>content</code></td><td>The full text of the review content.</td><td>string</td></tr><tr><td><code>timestamp</code></td><td>The date and location of the review, formatted as provided by Amazon.</td><td>string</td></tr><tr><td><code>profile_id</code></td><td>Unique identifier for the review author's profile, used to link to their Amazon profile.</td><td>string</td></tr><tr><td><code>is_verified</code></td><td>Indicates whether the review is from a verified purchase.</td><td>boolean</td></tr><tr><td><code>review_from</code></td><td>Provides additional context about the review's origin (e.g., location-specific reviews or top reviews).</td><td>string</td></tr><tr><td><code>helpful_count</code> (optional)</td><td>Number of helpful votes received for the review.</td><td>integer</td></tr><tr><td><code>product_attributes</code> (optional)</td><td>Identifies the characteristics of the product.</td><td>string</td></tr></tbody></table>

### Variations

This field contains information about different variations of a product, such as color, size, style, etc. Each variation is represented as an object with details including ASIN, selection status, dimensions (attributes like color, size, style), and a tooltip image URL.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXcdyaS6IpS2iBt2vh-DnjB2s3dY-5cXIHFJgo979WpKtEznbMjWA9KlHYZD0saQRRqfGKfvm3obeU21QUiUleA8PsA9cNRQKndluRbtmqNiNBMzBXAeSBKalIlIbd69A4_clyW3QqJmEHjRHwOKqTmhZSye?key=6Frx2zsHA3l2U3hK0m1qkw" alt="" width="563"><figcaption></figcaption></figure>

```json
 ...
"variation": [
        {
            "asin": "B07RM6QYWC",
            "selected": false,
            "dimensions": {
                "Color": "Ocean Blue",
                "Size": "128GB",
                "Style": "Verizon"
            },
            "tooltip_image": "https://m.media-amazon.com/images/I/41zzpCgao9L._SS36_.jpg"
        },
...

```

<table><thead><tr><th width="221">Key (variations)</th><th width="314">Description</th><th width="113">Type</th><th>Layout</th></tr></thead><tbody><tr><td><code>asin</code></td><td>The Amazon Standard Identification Number of product variant.</td><td>array</td><td><br></td></tr><tr><td><code>selected</code></td><td>Identifies the selected product variant.</td><td>boolean</td><td><br></td></tr><tr><td><code>dimensions</code></td><td>The dimensions of the variant product.</td><td>object</td><td>optional</td></tr><tr><td><code>dimensions.size</code></td><td>The size of the variant product.</td><td>string</td><td>optional</td></tr><tr><td><code>dimensions.color</code></td><td>The color of the variant product.</td><td>string</td><td>optional</td></tr><tr><td><code>dimensions.style</code></td><td>The style of the variant product.</td><td>string</td><td>optional</td></tr><tr><td><code>dimensions.unit count</code></td><td>The standard unit count of the variant product.</td><td>string</td><td>optional</td></tr><tr><td><code>tooltip_image</code></td><td>The URL of the variant image.</td><td>string</td><td>optional</td></tr></tbody></table>

### Warranty and Support

This field contains information about the warranty and support options for the product. It includes a description of the product warranty and links to obtain warranty information.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeRe9qQgXsdQtDWUtHepG_gPwe_lsddFN3p8T38W9OK2wAUhS5UQL_r3VnImSEUUfM1ungUxJtcfph-Bl_WJzF2pMmw83UfqNk65G4Ev76fuiOXdYrA0UXf6F-e80JWV-DhSW4zlFkKGTF_jtH97JblBKKM?key=6Frx2zsHA3l2U3hK0m1qkw" alt="" width="563"><figcaption></figcaption></figure>

```json
...
 "warranty_and_support": {
        "description": "Product Warranty: For warranty information about this product, please click here",
        "links": [
            {
                "title": "click here",
                "url": "/gp/feature.html/ref=dp_warranty_request_3P?docId=1002406021"
            }
        ]
    },
...
```

<table><thead><tr><th width="205">Key (warranty_and_support)</th><th width="397">Description</th><th>Type</th></tr></thead><tbody><tr><td><code>description</code></td><td>The description of the warranty available for the product.</td><td>string</td></tr><tr><td><code>links</code></td><td>A list containing more information on the warranty of the product.</td><td>array</td></tr><tr><td><code>links.title</code></td><td>The title of the warranty.</td><td>string</td></tr><tr><td><code>links.url</code></td><td>A URL containing more information on the warranty of the product.</td><td>string</td></tr></tbody></table>

### Featured Merchant

This field provides information about the featured merchant selling the product. It includes details such as the merchant's name, seller ID, link to the merchant's page, whether the product is Amazon fulfilled, and the shipping origin.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfnw74lgnMoekfj4gORU5v3OMfi8t07KqvTutlCjmvs4mjcsvyhF4lfGcnXoUcyDzl4QK4hkQUZzzJFB2AS3Hn6Q8gB8gCJoMJhn8rYb4_g37i32zJgZTd33qMHZPHq4H3SuXgKc6md6CYuQHxKhvOesedU?key=6Frx2zsHA3l2U3hK0m1qkw" alt="" width="188"><figcaption></figcaption></figure>

```json
... 
 "featured_merchant": {
        "name": "LYTEK LLC",
        "seller_id": "A2OL0VKAHK1LYK",
        "link": "/gp/help/seller/at-a-glance.html/ref=dp_merchant_link?ie=UTF8&seller=A2OL0VKAHK1LYK&isAmazonFulfilled=1",
        "is_amazon_fulfilled": true,
        "shipped_from": "Amazon"
    },
...
```

<table><thead><tr><th width="254">Key(featured_merchant)</th><th width="322">Description</th><th>Type</th></tr></thead><tbody><tr><td><code>name</code></td><td>The name of the primary seller.</td><td>string</td></tr><tr><td><code>seller_id</code></td><td>The ID of the seller.</td><td>string</td></tr><tr><td><code>link</code></td><td>The URL of the Amazon seller page.</td><td>string</td></tr><tr><td><code>is_amazon_fulfilled</code></td><td>Indicates whether a product is fulfilled by Amazon's own logistics network</td><td>boolean</td></tr><tr><td><code>shipped_from</code> (optional)</td><td>Indicates the shipping location.</td><td>string</td></tr></tbody></table>

### Sales Rank

This field provides information about the sales rank of the product within specific categories on Amazon. Each object represents a sales rank entry, including the rank itself and the category ladder, showing the hierarchy of categories leading to the ranked category.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeF-77XJS7SjDIqPMKqibsSLLVIMJ0ccoHimn32eBYB91kgq_EaYAkFLsaGJ4qBPzm9Rlt0TtlVCd-HgkPMEmBjUQMVwO6OfC76PCuFWcU-1fUs8qQoWirbY_3SM3qurHBy4FKQqjkqteL_Ml8FUkEkJYEI?key=6Frx2zsHA3l2U3hK0m1qkw" alt=""><figcaption></figcaption></figure>

```json
...
"sales_rank": [
        {
            "rank": 1366,
            "ladder": [
                {
                    "url": "/gp/bestsellers/office-products/ref=pd_zg_ts_office-products",
                    "name": "Office Products "
                }
            ]
        },
        {
            "rank": 18,
            "ladder": [
                {
                    "url": "/gp/bestsellers/office-products/490755011/ref=pd_zg_hrsr_office-products",
                    "name": "Hardcover Executive Notebooks"
                }
            ]
        }
    ],
...
```

<table><thead><tr><th>Key(sales_rank)</th><th width="376">Description</th><th>Type</th></tr></thead><tbody><tr><td><code>rank</code></td><td>Indicates the ranking position.</td><td>integer</td></tr><tr><td><code>ladder</code></td><td>A list of more detailed information on the category the product has been ranked in.</td><td>array</td></tr><tr><td><code>ladder.url</code></td><td>The URL to the relevant Bestsellers category page.</td><td>string</td></tr><tr><td><code>ladder.name</code></td><td>Indicates the category which the product has been ranked in.</td><td>string</td></tr></tbody></table>

### Delivery

This field provides information about delivery options for the product, such as the fastest delivery method and estimated arrival dates.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXc7xIMuzh_ifIyliSjqUyxf-S_ZzmFmx14ehEe3Ezbf2LarOVdGOYtoriq_gZWMAOnMZHL436DiBBeBzPif64z4wUtAH_2iJYtORulBb9Q4_MI9L-6IrxTZxRFq440lAESMZ4_SeQLLmvZkUyCa25_Nuqoy?key=6Frx2zsHA3l2U3hK0m1qkw" alt="" width="188"><figcaption></figcaption></figure>

```json
...
    "delivery": [
        {
            "type": "Fastest delivery",
            "date": {
                "from": null,
                "by": "Thursday, Jan 28"
            }
        }
    ],
...
```

<table><thead><tr><th>Key (delivery)</th><th width="357">Description</th><th>Type</th></tr></thead><tbody><tr><td><code>type</code></td><td>Indicates the type of the delivery.</td><td>string</td></tr><tr><td><code>date</code></td><td>A list of information on the delivery date.</td><td>object</td></tr><tr><td><code>date.from</code></td><td>The shipping location.</td><td>string</td></tr><tr><td><code>date.by</code></td><td>The estimated delivery date.</td><td>string</td></tr></tbody></table>

### Buy Box

The "buy box" section on an Amazon product page where customers can directly purchase items. This field provides essential information for buyers, including the product price, stock availability, delivery options, and estimated arrival dates.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXflQBjJQXgVIeLfTgTRQwPX_RFvm2umWb27Gbc_faJJDgpPtXe7iIoyhsScxJE9UYuPoorJ8r0vrLBy_aFKAeanR2Wg6pmJMVwepbr3g5eC5-Madbcjp8RjsTMnO2JPaEjYMA0lU0TAXmXW-TM-AlaQHk2H?key=6Frx2zsHA3l2U3hK0m1qkw" alt="" width="188"><figcaption></figcaption></figure>

```json
...
"buybox": [
    {
        "price": 199.99,
        "stock": "Only 1 left in stock - order soon.",
        "delivery_type": "Delivery",
        "delivery_details": [
            {
                "date": {
                    "by": "Thursday, June 6",
                    "from": null
                },
                "type": "FREE delivery"
            },
            {
                "date": {
                    "by": "Tuesday, June 4",
                    "from": null
                },
                "type": "Or fastest delivery"
            }
        ]
    },
...
```

<table><thead><tr><th width="264">Key (buybox)</th><th width="279">Description</th><th width="93">Type</th><th>Layout</th></tr></thead><tbody><tr><td><code>name</code></td><td>The name of the pricing option.</td><td>string</td><td>optional</td></tr><tr><td><code>stock</code></td><td>The inventory level of the product.</td><td>string</td><td>optional</td></tr><tr><td><code>delivery_type</code></td><td>Indicates the type of the delivery.</td><td>string</td><td>optional</td></tr><tr><td><code>delivery_details</code></td><td>A list of details on the delivery of the product.</td><td>array</td><td>optional</td></tr><tr><td><code>date</code></td><td>A list of details on the delivery date.</td><td>object</td><td>optional</td></tr><tr><td><code>delivery_details.by</code></td><td>The estimated delivery date.</td><td>string</td><td>optional</td></tr><tr><td><code>delivery_details.from</code></td><td>The shipping location of the product.</td><td>string</td><td>optional</td></tr><tr><td><code>delivery_details.type</code></td><td>The type of the delivery</td><td>string</td><td>optional</td></tr><tr><td><code>condition</code></td><td>The condition of the product.</td><td>string</td><td>optional</td></tr><tr><td><code>price</code></td><td>The price of the product.</td><td>float</td><td><br></td></tr></tbody></table>

### Lightning Deal

This field provides details about a lightning deal on Amazon, offering a discounted price for a limited time. Lightning deals are time-limited promotions with significant discounts on specific products, available for a few hours in limited quantities. Customers must act quickly as deals expire once the allocated time or inventory runs out. Details include the percentage claimed, discounted price, and time remaining before the deal expires.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXd0clhk0XWfT1yJJ7ozVFOEPQ3pi1F65Yjpz6H-ZksvBMrRrnMuld8Ab0k-o-DFK-oxNU16oaU6jMaTYRliU_YbLqK1mD3ZADdz-lBFdzaU8QsVSaM7438mQZiJ4N5sjnrFcvGCl32KPV94oaKGhx5ibOc?key=6Frx2zsHA3l2U3hK0m1qkw" alt="" width="375"><figcaption></figcaption></figure>

```json
...
"lightning_deal": {
        "percent_claimed": "0%",
        "price_text": "10,999.00  (Save 52%)",
        "expires": "Ends in  06h 30m 56s"
    },
...
```

<table><thead><tr><th width="212">Key(lightning_deal)</th><th width="409">Description</th><th>Type</th></tr></thead><tbody><tr><td><code>percent_claimed</code></td><td>The discounted amount compared to the default price.</td><td>string</td></tr><tr><td><code>price_text</code></td><td>The discounted product price.</td><td>string</td></tr><tr><td><code>expires</code></td><td>Indicates the ending date of the lightning deal offer.</td><td>string</td></tr></tbody></table>

### Product Overview

This section provides a structured summary of various key attributes related to a product.

<figure><img src="https://63892162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzrXw45naRpCZ0Ku9AjY1%2Fuploads%2F4XY0tWQmB76dSUs3OJKd%2FScreenshot%202024-07-12%20at%2010.47.07.png?alt=media&#x26;token=4f025487-086a-4e34-9e2e-2c1555803136" alt=""><figcaption></figcaption></figure>

```json
...
"product_overview": [
    {
        "title": "Material",
        "description": "Rubber"
    },
    {
        "title": "Vehicle Service Type",
        "description": "Passenger Car"
    },
    {
        "title": "Auto Part Position",
        "description": "Unknown"
    },
    {
        "title": "Fit Type",
        "description": "Universal Fit"
    }
],
...
```

<table><thead><tr><th width="251">Key(product_overview)</th><th width="351">Description</th><th>Type</th></tr></thead><tbody><tr><td><code>product_overview</code></td><td>A list of key attributes and their descriptions for the product.</td><td>Array</td></tr><tr><td><code>title</code></td><td>The title of the product attribute.</td><td>string</td></tr><tr><td><code>description</code></td><td>The detailed description of the product attribute.</td><td>string</td></tr></tbody></table>

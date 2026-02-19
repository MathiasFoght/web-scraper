# Search

The `amazon_search` source is designed to retrieve Amazon search result pages. To see the response example with retrieved data, download [**this** **sample output**](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiwDdoZGfMbUe5cRL2417%2Fuploads%2Fyg8tdLTqrajAxhtjiuR5%2Famazon_search.json?alt=media\&token=f02b1ceb-70f6-45cd-9f7c-7247196b2bd6) file in HTML format or check structured data output [**here**](#structured-data).

{% hint style="info" %}
Explore output [**data dictionary**](#data-dictionary) for each Amazon Search feature, offering a brief description, screenshot, parsed JSON code snippet, and a table defining each parsed field. Navigate through the details using the right-side navigation or scrolling down the page.
{% endhint %}

## Request samples

In the code examples below, we make a request to retrieve a result from `amazon.com`, which includes `2` search results pages, starting from page `#2` , for the search term `nirvana tshirt`. Additionally, the search is be limited to category ID: `16391693031` and the prices are displayed in `USD` currency.

{% tabs %}
{% tab title="cURL" %}

```bash
curl 'https://realtime.oxylabs.io/v1/queries' \
--user 'USERNAME:PASSWORD' \
-H 'Content-Type: application/json' \
-d '{
        "source": "amazon_search",
        "domain": "com",
        "query": "nirvana tshirt",
        "start_page": 2,
        "pages": 2,
        "parse": true,
        "context": [
                {"key": "category_id", "value": "16391693031"},
                {"key": "currency", "value": "USD"},
                {"key": "refinements", "value": ["p_123:256097"]},
                {"key": "sort_by", "value": "featured"}
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
    'source': 'amazon_search',
    'domain': 'com',
    'query': 'nirvana tshirt',
    'start_page': 2,
    'pages': 2,
    'parse': True,
    'context': [
        {'key': 'category_id', 'value': 16391693031},
        {'key': 'currency', 'value': 'USD'},
        {"key": "refinements", "value": ["p_123:256097"]},
        {"key": "sort_by", "value": "featured"}
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
    source: "amazon_search",
    domain: "com",
    query: "nirvana tshirt",
    start_page: 2, 
    pages: 2,
    parse: true,
    sort_by: "featured",
    refinements: "p_123:256097",
    context: [
        { key: "category_id", value: "16391693031" },
        { key: "currency", value: "USD" },
        {"key": "refinements", "value": ["p_123:256097"]},
        {"key": "sort_by", "value": "featured"},
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
https://realtime.oxylabs.io/v1/queries?source=amazon_search&domain=com&query=nirvana%20tshirt&start_page=2&pages=2&sort_by=featured&refinements[0]=p_123:256097&parse=true&context[0][key]=category_id&context[0][value]=16391693031&context[1][key]=currency&context[1][value]=USD&access_token=12345abcde
```

{% endtab %}

{% tab title="PHP" %}

```php
<?php

$params = array(
    'source' => 'amazon_search',
    'domain' => 'com',
    'query' => 'nirvana tshirt',
    'start_page' => 2, 
    'pages' => 2,
    'parse' => true,
    'sort_by' => 'featured',
    'refinements' => 'p_123:256097',
    'context' => [
        ['key' => 'category_id', 'value' => 16391693031],
        ['key' => 'currency', 'value' => 'USD'],
        ['key': 'refinements', 'value': ['p_123:256097']],
        ['key' => 'sort_by', 'value' => 'featured']    
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
		"source":     "amazon_search",
		"domain":     "com",
		"query":      "nirvana tshirt",
		"start_page": 2,
		"pages":      2,
		"parse":      true,
		"sort_by":    "featured",
        	"refinements":"p_123:256097",
		"context": []map[string]interface{}{
			{"key": "category_id", "value": 16391693031},
			{"key": "currency", "value": "USD"},
			{"key": "refinements", "value": []string{"p_123:256097"}},
                	{"key": "sort_by", "value": "featured"},
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
                source = "amazon_search",
                domain = "com",
                query = "nirvana tshirt",
                start_page = 2,
                pages = 2,
                parse = true,
                sort_by: "featured",
                refinements: "p_123:256097",
                context = new dynamic [] {
                    new { key = "category_id", value = 16391693031 },
                    new { key = "currency", value = "USD" },
                    new { key = "refinements", value = new object[] {"p_123:256097"}}, 
                    new { key = "sort_by", value = "featured"}
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
        jsonObject.put("source", "amazon_search");
        jsonObject.put("domain", "com");
        jsonObject.put("query", "nirvana tshirt");
        jsonObject.put("start_page", 2);
        jsonObject.put("pages", 2);
        jsonObject.put("parse", true);
        jsonObject.put("sort_by", "featured");
        jsonObject.put("refinements", "p_123:256097");
        jsonObject.put("context", new JSONArray()
                .put(new JSONObject()
                        .put("key", "category_id")
                        .put("value", "16391693031"))
                .put(new JSONObject()
                        .put("key", "currency")
                        .put("value", "USD"))
                .put(new JSONObject()
                        .put("key", "refinements")
                        .put("value", new JSONArray()
                                .put("p_123:256097"))
                .put(new JSONObject()
                        .put("key", "sort_by")
                        .put("value", "featured"))
        );

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
    "source": "amazon_search", 
    "domain": "com", 
    "query": "nirvana tshirt", 
    "start_page": 2, 
    "pages": 2,
    "parse": true,
    "sort_by": "featured",
    "refinements": "p_123:256097",
    "context": [
        {"key": "category_id", "value": "16391693031"},
        {"key": "currency", "value": "USD"},
        {"key": "refinements", "value": ["p_123:256097"]},
        {"key": "sort_by", "value": "featured"}
    ]
}
```

{% endtab %}
{% endtabs %}

We use synchronous [**Realtime**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods/realtime) integration method in our examples. If you would like to use [**Proxy Endpoint**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods/proxy-endpoint) or asynchronous [**Push-Pull**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods/push-pull) integration, refer to the [**integration methods**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods) section.

## Request parameter values

### Generic

Basic setup and customization options for scraping Amazon search results.

<table><thead><tr><th width="222">Parameter</th><th width="350.3333333333333">Description</th><th>Default Value</th></tr></thead><tbody><tr><td><mark style="background-color:green;"><strong>source</strong></mark></td><td>Sets the scraper.</td><td><code>amazon_search</code></td></tr><tr><td><mark style="background-color:green;"><strong>query</strong></mark></td><td>The keyword or phrase to search for.</td><td>-</td></tr><tr><td><code>render</code></td><td>Enables JavaScript rendering when set to <code>html</code>. <a href="../../features/js-rendering-and-browser-control/javascript-rendering"><strong>More info</strong></a><strong>.</strong></td><td>-</td></tr><tr><td><code>parse</code></td><td>Returns parsed data when set to <code>true</code>. Explore output <a href="#output-data-dictionary"><strong>data dictionary</strong></a>.</td><td><code>false</code></td></tr><tr><td><code>callback_url</code></td><td>URL to your callback endpoint. <a href="../../../integration-methods/push-pull#callback"><strong>More info</strong></a>.</td><td>-</td></tr><tr><td><code>user_agent_type</code></td><td>Device type and browser. The full list can be found <a href="../../features/http-context-and-job-management/user-agent-type"><strong>here</strong></a>.</td><td><code>desktop</code></td></tr><tr><td><code>context</code>:<br><code>currency</code></td><td>Sets the currency. Check the available values <a href="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzrXw45naRpCZ0Ku9AjY1%2Fuploads%2FIAHLazcDOwZSiZ6s8IJt%2FAmazon_search_currency_values.json?alt=media&#x26;token=b72b5c4d-3820-42a6-8e74-78ea6b44e93f"><strong>here</strong></a>.</td><td>-</td></tr></tbody></table>

\- mandatory parameter

### Localization

Adapt results to specific geographical locations, domains, languages.

| Parameter      | Description                                                                                                                                                                                                          | Default Value |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `geo_location` | The *Deliver to* location. See our guide to using this parameter [**here**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/features/localization/e-commerce-localization)**.**                     | -             |
| `domain`       | Domain localization for Bestbuy. The full list of available domains can be found [**here**](https://developers.oxylabs.io/scraping-solutions/features/localization/domain-locale-results-language#domain).           | `com`         |
| `locale`       | `Accept-Language` header value, which sets the interface language of the Amazon page. [**More info**](https://developers.oxylabs.io/scraping-solutions/features/localization/domain-locale-results-language#locale). | -             |

{% hint style="warning" %}
**IMPORTANT:** On most page types, Amazon tailors the returned results based on the delivery location of their customers. Therefore, we advise using the `geo_location` parameter to set your preferred delivery location. You can read more about using `geo_location` with Amazon [**here**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/features/localization/e-commerce-localization).
{% endhint %}

### Pagination

Controls for managing the pagination and retrieval of search results.

<table><thead><tr><th width="222">Parameter</th><th width="350.3333333333333">Description</th><th width="167">Default Value</th></tr></thead><tbody><tr><td><code>start_page</code></td><td>Starting page number.</td><td><code>1</code></td></tr><tr><td><code>pages</code></td><td>Number of pages to retrieve.</td><td><code>1</code></td></tr></tbody></table>

### Sorting and filtering

Controls for sorting and filtering of search result pages.

<table><thead><tr><th width="222">Parameter</th><th width="350.3333333333333">Description</th><th>Default Value</th></tr></thead><tbody><tr><td><code>sort_by</code></td><td>Sets the sorting type of the search results page according to one of possible values in Amazon:<br><code>"most_recent"</code>, <code>"price_low_to_high"</code>, <code>"price_high_to_low"</code>, <code>"featured"</code>, <code>"average_review"</code>, <code>"bestsellers"</code>.</td><td>-</td></tr><tr><td><code>refinements</code></td><td><p>A <strong>list</strong> of Amazon search refinement parameters used to apply specific filters to search results. These parameters correspond to Amazon's dynamic filtering options (e.g., brand, price range, features) and follow Amazon's internal parameter format such as <code>p_123:256097</code> or <code>p_n_feature_twenty-eight_browse-bin:98209020031</code>.</p><p>Since filtering options vary by category and are dynamically generated by Amazon, the recommended workflow is:</p><ol><li>First, scrape the target Amazon search page with <code>parse: true</code> to discover available refinement options</li><li>Extract the desired filter parameters from the parsed response</li><li>Use those parameters in subsequent requests via the <code>refinements</code> field to apply specific filters</li></ol></td><td>-</td></tr><tr><td><code>context</code>:<br><code>category_id</code></td><td>Search for items in a particular Amazon node (product category).</td><td>-</td></tr><tr><td><code>context</code>:<br><code>merchant_id</code></td><td>Search for items sold by a particular seller.</td><td>-</td></tr></tbody></table>

## Structured data

<details>

<summary><code>amazon_search</code> structured output</summary>

```json
{
    "results": [
        {
            "content": {
                "url": "https://www.amazon.com/s?k=nirvana tshirt&page=1",
                "page": 1,
                "query": "nirvana tshirt",
                "results": {
                    "paid": [
                        {
                            "url": "https://aax-us-iad.amazon.com/x/c/JJkmeNPKYs4EvHZJpsz-T1AAAAGXMHRJBgEAAAH2AQBvbm9fdHhuX2JpZDYgICBvbm9fdHhuX2ltcDIgICBfRRHN/https://www.amazon.com/INTO-AM-Islands-Graphic-T-Shirt/dp/B085G65YJT/ref=sxin_16_sbv_search_btf?content-id=amzn1.sym.8aea4788-5372-43c5-bde7-3d239eb02a51:amzn1.sym.8aea4788-5372-43c5-bde7-3d239eb02a51&cv_ct_cx=nirvana+tshirt&keywords=nirvana+tshirt&pd_rd_i=B085G65YJT&pd_rd_r=9f683f75-043c-422e-9698-1ffbddaa9797&pd_rd_w=SfvTj&pd_rd_wg=l2Cej&pf_rd_p=8aea4788-5372-43c5-bde7-3d239eb02a51&pf_rd_r=N19WZRDBC10WN96NMY59&qid=1748864616&sbo=RZvfv//HxDF+O5021pAnSA==&sr=1-1-5190daf0-67e3-427c-bea6-c72c1df98776",
                            "asin": "B085G65YJT",
                            "price": 28.95,
                            "title": "INTO THE AM Cool Graphic T-Shirts for Men S - 4XL Premium Quality Unique Graphic Art Tees",
                            "rating": 4.7,
                            "rel_pos": 1,
                            "currency": "USD",
                            "is_video": true,
                            "url_image": "https://aax-us-iad.amazon.com/e/loi/imp?b=JJkmeNPKYs4EvHZJpsz-T1AAAAGXMHRJBgEAAAH2AQBvbm9fdHhuX2JpZDYgICBvbm9fdHhuX2ltcDIgICBfRRHN",
                            "best_seller": false,
                            "price_upper": 28.95,
                            "is_sponsored": true,
                            "manufacturer": "",
                            "sales_volume": "200+ bought in past month",
                            "pricing_count": 1,
                            "reviews_count": 5852,
                            "is_amazons_choice": false
                        },
                        {
                            "url": "https://aax-us-iad.amazon.com/x/c/JMnK9Qagwna73uV43C4lDLQAAAGXMHRJDAEAAAH2AQBvbm9fdHhuX2JpZDIgICBvbm9fdHhuX2ltcDIgICDCKsJB/https://www.amazon.com/Aelfric-Eden-Oversized-Streetwear-Contrast/dp/B0C9CJ19Y6/ref=sxbs_sbv_search_btf?content-id=amzn1.sym.2f0a8989-0b67-47e7-b61e-9e3ef9908602:amzn1.sym.2f0a8989-0b67-47e7-b61e-9e3ef9908602&cv_ct_cx=nirvana+tshirt&keywords=nirvana+tshirt&pd_rd_i=B0C9CJ19Y6&pd_rd_r=40b9a7b4-20ca-4a75-abe7-6286f347b215&pd_rd_w=5ELrT&pd_rd_wg=wOCbD&pf_rd_p=2f0a8989-0b67-47e7-b61e-9e3ef9908602&pf_rd_r=N19WZRDBC10WN96NMY59&qid=1748864616&sbo=RZvfv//HxDF+O5021pAnSA==&sr=1-1-a61ee601-6e56-4862-a8a2-1d3da5a5406f",
                            "asin": "B0C9CJ19Y6",
                            "price": 27.95,
                            "title": "Aelfric Eden Oversized T Shirt Men 90s Shirt Unisex Streetwear Contrast Color Graphic Tees Casual Vintage Summer Tops",
                            "rating": 4.4,
                            "rel_pos": 2,
                            "currency": "USD",
                            "is_video": true,
                            "url_image": "https://aax-us-iad.amazon.com/e/loi/imp?b=JMnK9Qagwna73uV43C4lDLQAAAGXMHRJDAEAAAH2AQBvbm9fdHhuX2JpZDIgICBvbm9fdHhuX2ltcDIgICDCKsJB",
                            "best_seller": false,
                            "price_upper": 27.95,
                            "is_sponsored": true,
                            "manufacturer": "",
                            "sales_volume": "100+ bought in past month",
                            "pricing_count": 1,
                            "reviews_count": 208,
                            "is_amazons_choice": false,
                            "price_strikethrough": 34.95
                        }
                    ],
                    "organic": [
                        {
                            "pos": 1,
                            "url": "/GrayceTM-Your-Design-Here-T-Shirt/dp/B0CM2QJ9T5/ref=sr_1_1?dib=eyJ2IjoiMSJ9.O-FB6EEDsdPVK-dDjnAjiLlABO3haXmG0Ye9gCbshKVw0OWrVB47JhGYhPq7F7MzaLGou3AMkkEdlPW5Mkhwt-e6JGysd341BMG1IYmLXEpj1QyjcYqT_zzzL0wN79w9kQVymSCL3Lug015qP8nQgawRG7vCiiEaxopHm7t6S7xQ6AJDE1CyNY-jdJGDxhZh2pEi-iwRD3EwWHjpVXp05mtZj-Bd17TYuOZDpm1NnufLGo_St6XVM_PT0mborUpyPozmWQpJ2YXO_xiK78MlJMkQSoDaXAzQIMgY4bGnSh8.6B1hR7mitilEdXMf_edFJkoOBTtAB_yELeTYf3B2vsk&dib_tag=se&keywords=nirvana+tshirt&qid=1748864616&sr=8-1",
                            "asin": "B0CM2QJ9T5",
                            "price": 23,
                            "title": "Nirvana™ in Utero Angel Splatter T-Shirt - by Nirvana™ Splatter (US, Alpha",
                            "rating": 4.6,
                            "currency": "USD",
                            "is_prime": true,
                            "url_image": "https://m.media-amazon.com/images/I/81MkKdYZFtL._AC_UL320_.jpg",
                            "best_seller": false,
                            "price_upper": 23,
                            "is_sponsored": false,
                            "manufacturer": "",
                            "sales_volume": "50+ bought in past month",
                            "pricing_count": 1,
                            "reviews_count": 297,
                            "is_amazons_choice": true,
                            "shipping_information": "FREE delivery Sat, Jun 7 on $35 of items shipped by AmazonOr fastest delivery Tomorrow, Jun 3"
                        },
                        {
                            "pos": 2,
                            "url": "/Nirvana-Smile-Sided-T-Shirt-Large/dp/B07BQ5JCP4/ref=sr_1_2?dib=eyJ2IjoiMSJ9.O-FB6EEDsdPVK-dDjnAjiLlABO3haXmG0Ye9gCbshKVw0OWrVB47JhGYhPq7F7MzaLGou3AMkkEdlPW5Mkhwt-e6JGysd341BMG1IYmLXEpj1QyjcYqT_zzzL0wN79w9kQVymSCL3Lug015qP8nQgawRG7vCiiEaxopHm7t6S7xQ6AJDE1CyNY-jdJGDxhZh2pEi-iwRD3EwWHjpVXp05mtZj-Bd17TYuOZDpm1NnufLGo_St6XVM_PT0mborUpyPozmWQpJ2YXO_xiK78MlJMkQSoDaXAzQIMgY4bGnSh8.6B1hR7mitilEdXMf_edFJkoOBTtAB_yELeTYf3B2vsk&dib_tag=se&keywords=nirvana+tshirt&qid=1748864616&sr=8-2",
                            "asin": "B07BQ5JCP4",
                            "price": 17.99,
                            "title": "mens T-shirt",
                            "rating": 4.6,
                            "currency": "USD",
                            "is_prime": false,
                            "url_image": "https://m.media-amazon.com/images/I/613zyJBaYpL._AC_UL320_.jpg",
                            "best_seller": false,
                            "price_upper": 17.99,
                            "is_sponsored": false,
                            "manufacturer": "",
                            "sales_volume": "100+ bought in past month",
                            "pricing_count": 1,
                            "reviews_count": 1831,
                            "is_amazons_choice": false,
                            "price_strikethrough": 18.96,
                            "shipping_information": "FREE delivery Wed, Jun 4"
                        },

                        {"...": "..."},

                        {
                            "pos": 47,
                            "url": "/FEA-novelty-shirts-White-Small/dp/B00WHWF4BE/ref=sr_1_47?dib=eyJ2IjoiMSJ9.O-FB6EEDsdPVK-dDjnAjiLlABO3haXmG0Ye9gCbshKVw0OWrVB47JhGYhPq7F7MzaLGou3AMkkEdlPW5Mkhwt-e6JGysd341BMG1IYmLXEpj1QyjcYqT_zzzL0wN79w9kQVymSCL3Lug015qP8nQgawRG7vCiiEaxopHm7t6S7xQ6AJDE1CyNY-jdJGDxhZh2pEi-iwRD3EwWHjpVXp05mtZj-Bd17TYuOZDpm1NnufLGo_St6XVM_PT0mborUpyPozmWQpJ2YXO_xiK78MlJMkQSoDaXAzQIMgY4bGnSh8.6B1hR7mitilEdXMf_edFJkoOBTtAB_yELeTYf3B2vsk&dib_tag=se&keywords=nirvana+tshirt&qid=1748864616&sr=8-47",
                            "asin": "B00WHWF4BE",
                            "price": 24.97,
                            "title": "Men's Kurt Cobain Smoking Black and White Photo T-Shirt",
                            "rating": 4.5,
                            "currency": "USD",
                            "is_prime": false,
                            "url_image": "https://m.media-amazon.com/images/I/81vV8Jrk4WS._AC_UL320_.jpg",
                            "best_seller": false,
                            "price_upper": 24.97,
                            "is_sponsored": false,
                            "manufacturer": "",
                            "pricing_count": 1,
                            "reviews_count": 141,
                            "is_amazons_choice": false,
                            "price_strikethrough": 30,
                            "shipping_information": "FREE delivery Tue, Jun 10 Or fastest delivery Tomorrow, Jun 3"
                        },
                        {
                            "pos": 48,
                            "url": "/Old-Glory-Nirvana-Serpent-T-Shirt/dp/B00E5PYAAW/ref=sr_1_48?dib=eyJ2IjoiMSJ9.O-FB6EEDsdPVK-dDjnAjiLlABO3haXmG0Ye9gCbshKVw0OWrVB47JhGYhPq7F7MzaLGou3AMkkEdlPW5Mkhwt-e6JGysd341BMG1IYmLXEpj1QyjcYqT_zzzL0wN79w9kQVymSCL3Lug015qP8nQgawRG7vCiiEaxopHm7t6S7xQ6AJDE1CyNY-jdJGDxhZh2pEi-iwRD3EwWHjpVXp05mtZj-Bd17TYuOZDpm1NnufLGo_St6XVM_PT0mborUpyPozmWQpJ2YXO_xiK78MlJMkQSoDaXAzQIMgY4bGnSh8.6B1hR7mitilEdXMf_edFJkoOBTtAB_yELeTYf3B2vsk&dib_tag=se&keywords=nirvana+tshirt&qid=1748864616&sr=8-48",
                            "asin": "B00E5PYAAW",
                            "price": 28.73,
                            "title": "Unisex-Adult Standard Men's Serpent T-Shirt",
                            "rating": 4.3,
                            "currency": "USD",
                            "is_prime": true,
                            "url_image": "https://m.media-amazon.com/images/I/81IlxTvYqOL._AC_UL320_.jpg",
                            "best_seller": false,
                            "price_upper": 28.73,
                            "is_sponsored": false,
                            "manufacturer": "",
                            "pricing_count": 1,
                            "reviews_count": 67,
                            "is_amazons_choice": false,
                            "shipping_information": "FREE delivery Sat, Jun 7 on $35 of items shipped by AmazonOr fastest delivery Tomorrow, Jun 3"
                        }
                    ],
                    "suggested": [],
                    "amazons_choices": [
                        {
                            "pos": 1,
                            "url": "/GrayceTM-Your-Design-Here-T-Shirt/dp/B0CM2QJ9T5/ref=sr_1_1?dib=eyJ2IjoiMSJ9.O-FB6EEDsdPVK-dDjnAjiLlABO3haXmG0Ye9gCbshKVw0OWrVB47JhGYhPq7F7MzaLGou3AMkkEdlPW5Mkhwt-e6JGysd341BMG1IYmLXEpj1QyjcYqT_zzzL0wN79w9kQVymSCL3Lug015qP8nQgawRG7vCiiEaxopHm7t6S7xQ6AJDE1CyNY-jdJGDxhZh2pEi-iwRD3EwWHjpVXp05mtZj-Bd17TYuOZDpm1NnufLGo_St6XVM_PT0mborUpyPozmWQpJ2YXO_xiK78MlJMkQSoDaXAzQIMgY4bGnSh8.6B1hR7mitilEdXMf_edFJkoOBTtAB_yELeTYf3B2vsk&dib_tag=se&keywords=nirvana+tshirt&qid=1748864616&sr=8-1",
                            "asin": "B0CM2QJ9T5",
                            "price": 23,
                            "title": "Nirvana™ in Utero Angel Splatter T-Shirt - by Nirvana™ Splatter (US, Alpha",
                            "rating": 4.6,
                            "currency": "USD",
                            "is_prime": true,
                            "url_image": "https://m.media-amazon.com/images/I/81MkKdYZFtL._AC_UL320_.jpg",
                            "best_seller": false,
                            "price_upper": 23,
                            "is_sponsored": false,
                            "manufacturer": "",
                            "sales_volume": "50+ bought in past month",
                            "pricing_count": 1,
                            "reviews_count": 297,
                            "is_amazons_choice": true,
                            "shipping_information": "FREE delivery Sat, Jun 7 on $35 of items shipped by AmazonOr fastest delivery Tomorrow, Jun 3"
                        }
                    ]
                },
                "refinements": {
                    "color": [
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_size_browse-vebin%3A2343349011&dc&qid=1748864616&rnid=2343347011&ref=sr_nr_p_n_size_browse-vebin_1&ds=v1%3A8MCORV9QCm%2BH5b7ulOMu7B0ghalXVBgcoGNzfhxLE5g",
                            "name": "Apply Black filter to narrow results",
                            "value": "n:7141123011,p_n_size_browse-vebin/2343349011",
                            "refinement_display_name": "Color"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_size_browse-vebin%3A2343350011&dc&qid=1748864616&rnid=2343347011&ref=sr_nr_p_n_size_browse-vebin_2&ds=v1%3AOFz5cj5PaTTRP920t2kR0tGTu4nyT%2BLJXcNsBbOTgFg",
                            "name": "Apply Blues filter to narrow results",
                            "value": "n:7141123011,p_n_size_browse-vebin/2343350011",
                            "refinement_display_name": "Color"
                        },

                        {"...": "..."},

                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_size_browse-vebin%3A2343362011&dc&qid=1748864616&rnid=2343347011&ref=sr_nr_p_n_size_browse-vebin_15&ds=v1%3AeZJyT7zQlzqxiJfRM%2BRLS7Jf80Unficl2Mz62UVeAKA",
                            "name": "Apply Silvers filter to narrow results",
                            "value": "n:7141123011,p_n_size_browse-vebin/2343362011",
                            "refinement_display_name": "Color"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_size_browse-vebin%3A2343357011&dc&qid=1748864616&rnid=2343347011&ref=sr_nr_p_n_size_browse-vebin_16&ds=v1%3AYMvGxdEOBiH6QtXt263L2vr7NzbjOzzuewrPrPbTkRA",
                            "name": "Apply Multi filter to narrow results",
                            "value": "n:7141123011,p_n_size_browse-vebin/2343357011",
                            "refinement_display_name": "Color"
                        }
                    ],
                    "brands": [
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_123%3A798807&dc&qid=1748864616&rnid=85457740011&ref=sr_nr_p_123_1&ds=v1%3AfygVTnGpUJLn%2BVb3YcdcTSAqK309ypqSOBtOKESw0c8",
                            "name": "Nirvana",
                            "value": "n:7141123011,p_123/798807",
                            "refinement_display_name": "Brands"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_123%3A380467&dc&qid=1748864616&rnid=85457740011&ref=sr_nr_p_123_2&ds=v1%3AUU%2F0B%2ByCPdS92Wo7wJixAbW0AuOE3jRaN2PsGjz7WEU",
                            "name": "FEA",
                            "value": "n:7141123011,p_123/380467",
                            "refinement_display_name": "Brands"
                        }
                    ],
                    "gender": [
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_thirty-two_browse-bin%3A121075132011&dc&qid=1748864616&rnid=121075130011&ref=sr_nr_p_n_feature_thirty-two_browse-bin_1&ds=v1%3AhTSIVZAGR96X%2BjPFNt5j6hiX5eVHjDDW1jU6iP3Jhjs",
                            "name": "Men",
                            "value": "n:7141123011,p_n_feature_thirty-two_browse-bin/121075132011",
                            "refinement_display_name": "Gender"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_thirty-two_browse-bin%3A121075131011&dc&qid=1748864616&rnid=121075130011&ref=sr_nr_p_n_feature_thirty-two_browse-bin_2&ds=v1%3Ajd2dN0GNlSpcrja6BA%2F%2BLxEnpxZwmdTK27y1q%2FEIbd0",
                            "name": "Women",
                            "value": "n:7141123011,p_n_feature_thirty-two_browse-bin/121075131011",
                            "refinement_display_name": "Gender"
                        },

                        {"...": "..."},

                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_thirty-two_browse-bin%3A121833111011&dc&qid=1748864616&rnid=121075130011&ref=sr_nr_p_n_feature_thirty-two_browse-bin_5&ds=v1%3AqREbh9MU2eAbWN89P7%2Fh69NQWwYc0tgmhFk%2FxSdzqZw",
                            "name": "Babies",
                            "value": "n:7141123011,p_n_feature_thirty-two_browse-bin/121833111011",
                            "refinement_display_name": "Gender"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_thirty-two_browse-bin%3A121833112011&dc&qid=1748864616&rnid=121075130011&ref=sr_nr_p_n_feature_thirty-two_browse-bin_6&ds=v1%3ABG%2B0BrcafOQT5ikKOaz9g2JtHJecsI7maRRd%2FMkT7Js",
                            "name": "Unisex",
                            "value": "n:7141123011,p_n_feature_thirty-two_browse-bin/121833112011",
                            "refinement_display_name": "Gender"
                        }
                    ],
                    "seller": [
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_6%3AATVPDKIKX0DER&dc&qid=1748864616&rnid=2661622011&ref=sr_nr_p_6_1&ds=v1%3Aps9qZhfHIbvTmH1BIbjiOP2pW0bwPnvE73Nz9akjuQ8",
                            "name": "Amazon.com",
                            "value": "n:7141123011,p_6/ATVPDKIKX0DER",
                            "refinement_display_name": "Seller"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_6%3AA3R27QEC0NUQ1F&dc&qid=1748864616&rnid=2661622011&ref=sr_nr_p_6_2&ds=v1%3Azt9v4DrawMVlTpqGuzeuXN7tvnMeStihU0ZMkd4gQD8",
                            "name": "CMhin",
                            "value": "n:7141123011,p_6/A3R27QEC0NUQ1F",
                            "refinement_display_name": "Seller"
                        },
                        
                        {"...": "..."},

                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_6%3AA20NP16MA9JUJI&dc&qid=1748864616&rnid=2661622011&ref=sr_nr_p_6_5&ds=v1%3ACRakCwn%2Fv5VuxfSJ8CAt%2BNC1yzFCLnck1YG7xMcygPA",
                            "name": "Paradiso Clothing",
                            "value": "n:7141123011,p_6/A20NP16MA9JUJI",
                            "refinement_display_name": "Seller"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_6%3AAPV6T4RKTKPW0&dc&qid=1748864616&rnid=2661622011&ref=sr_nr_p_6_6&ds=v1%3A7yMM6uWYvODCcPBqgkrO4e25BjFQ8xkl7c0P%2FwW%2F2KA",
                            "name": "Dress Code Clothing",
                            "value": "n:7141123011,p_6/APV6T4RKTKPW0",
                            "refinement_display_name": "Seller"
                        }
                    ],
                    "fit_type": [
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_four_browse-bin%3A43549681011&dc&qid=1748864616&rnid=23931923011&ref=sr_nr_p_n_feature_four_browse-bin_1&ds=v1%3AzqrXSjvaAvTP6xEbg0S57QOfWWxyncJ7AQpLQFhk%2Bqs",
                            "name": "Regular Fit",
                            "value": "n:7141123011,p_n_feature_four_browse-bin/43549681011",
                            "refinement_display_name": "Fit Type"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_four_browse-bin%3A43549679011&dc&qid=1748864616&rnid=23931923011&ref=sr_nr_p_n_feature_four_browse-bin_2&ds=v1%3AJL5P02F4OERcbbIwYopVoH%2B6g%2FLySK5lA1H5Tzpa4A4",
                            "name": "Classic Fit",
                            "value": "n:7141123011,p_n_feature_four_browse-bin/43549679011",
                            "refinement_display_name": "Fit Type"
                        },

                        {"...": "..."},

                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_four_browse-bin%3A43549683011&dc&qid=1748864616&rnid=23931923011&ref=sr_nr_p_n_feature_four_browse-bin_6&ds=v1%3AeU79GBHlWaX%2FgnhB%2BSc2%2B6MuDSIqzHis9sEQYfNFjqI",
                            "name": "Skinny Fit",
                            "value": "n:7141123011,p_n_feature_four_browse-bin/43549683011",
                            "refinement_display_name": "Fit Type"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_four_browse-bin%3A43549674011&dc&qid=1748864616&rnid=23931923011&ref=sr_nr_p_n_feature_four_browse-bin_7&ds=v1%3AQhYrAVv9VYYPwSgxdTeMtKSKfE0RM6LqqK3CQ%2B6KNDI",
                            "name": "Slim Fit",
                            "value": "n:7141123011,p_n_feature_four_browse-bin/43549674011",
                            "refinement_display_name": "Fit Type"
                        }
                    ],
                    "department": [
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A9056987011&dc&qid=1748864616&rnid=2941120011&ref=sr_nr_n_1&ds=v1%3Afa442VHW%2BJAV%2B5IPgsCbLti4Xk6AF56Qd3EcfR0Qr7A",
                            "name": "Men's Novelty T-Shirts",
                            "value": "n:9056987011",
                            "refinement_display_name": "Department"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7147441011&dc&qid=1748864616&rnid=2941120011&ref=sr_nr_n_2&ds=v1%3A8BMugiL9HimXeuTsYjZRS%2BSxvQGJ7FwwaUaPsKzTDSg",
                            "name": "Men's Fashion",
                            "value": "n:7147441011",
                            "refinement_display_name": "Department"
                        },

                        {"...": "..."},

                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A9057094011&dc&qid=1748864616&rnid=2941120011&ref=sr_nr_n_7&ds=v1%3AZyfNiaGEDgK38L6duSLUxX5sLh4vyppGQEAZ0BFD5%2BM",
                            "name": "Boys' Novelty T-Shirts",
                            "value": "n:9057094011",
                            "refinement_display_name": "Department"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A9057040011&dc&qid=1748864616&rnid=2941120011&ref=sr_nr_n_8&ds=v1%3AgOZDlyTmOBu1O16ye7xsN6CsGTcU%2FzEF57b917BkaBc",
                            "name": "Girls' Novelty T-Shirts",
                            "value": "n:9057040011",
                            "refinement_display_name": "Department"
                        }
                    ],
                    "delivery_day": [
                        {
                            "link": "/s?k=nirvana+tshirt&rh=p_90%3A8308921011&dc&qid=1748864616&rnid=8308919011&ref=sr_nr_p_90_1&ds=v1%3AoMnfELDJ60%2FbmTStO2hs0H%2Bszc7WFhJTu6j%2BAiGPWMY",
                            "name": "Get It by Tomorrow",
                            "value": "p_90/8308921011",
                            "refinement_display_name": "Delivery Day"
                        }
                    ],
                    "amazon_fashion": [
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_eighteen_browse-bin%3A14630392011&dc&qid=1748864616&rnid=14630382011&ref=sr_nr_p_n_feature_eighteen_browse-bin_1&ds=v1%3AcCqpPQL6QNOT01i%2BtZ8Bw4rCJCbhDy6L2uR6kKKYiCU",
                            "name": "Top Brands",
                            "value": "n:7141123011,p_n_feature_eighteen_browse-bin/14630392011",
                            "refinement_display_name": "Amazon Fashion"
                        }
                    ],
                    "apparel_pattern": [
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_twelve_browse-bin%3A23575358011&dc&qid=1748864616&rnid=23575341011&ref=sr_nr_p_n_feature_twelve_browse-bin_1&ds=v1%3AB5i2mxzmGKnEEiHc4vKwstzELxQ9mxWEljgyfcGfmfc",
                            "name": "Solid",
                            "value": "n:7141123011,p_n_feature_twelve_browse-bin/23575358011",
                            "refinement_display_name": "Apparel Pattern"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_twelve_browse-bin%3A23575351011&dc&qid=1748864616&rnid=23575341011&ref=sr_nr_p_n_feature_twelve_browse-bin_2&ds=v1%3AdgosYQiNEz5ebIx4MRlbQmr08wHcaIfbhp9oAei5lQY",
                            "name": "Letter Print",
                            "value": "n:7141123011,p_n_feature_twelve_browse-bin/23575351011",
                            "refinement_display_name": "Apparel Pattern"
                        },

                        {"...": "..."},

                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_twelve_browse-bin%3A23575361011&dc&qid=1748864616&rnid=23575341011&ref=sr_nr_p_n_feature_twelve_browse-bin_15&ds=v1%3ANBWlmAdI1SXnguOOYdLVyZL8j6ms5fUBi6ExVassJYE",
                            "name": "Polka Dots",
                            "value": "n:7141123011,p_n_feature_twelve_browse-bin/23575361011",
                            "refinement_display_name": "Apparel Pattern"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_twelve_browse-bin%3A23575364011&dc&qid=1748864616&rnid=23575341011&ref=sr_nr_p_n_feature_twelve_browse-bin_16&ds=v1%3AcLAQbq04evAinUdOhcW1dMvOsyeGBhKga4E4zB2qp%2Bk",
                            "name": "Striped",
                            "value": "n:7141123011,p_n_feature_twelve_browse-bin/23575364011",
                            "refinement_display_name": "Apparel Pattern"
                        }
                    ],
                    "deals_discounts": [
                        {
                            "link": "/s?k=nirvana+tshirt&rh=p_n_deal_type%3A23566065011&dc&qid=1748864616&rnid=23566063011&ref=sr_nr_p_n_deal_type_1&ds=v1%3AcHaW51xbr1JJ5OXaie29xcbUrdZsvyqXkOn3ZcF1rP4",
                            "name": "All Discounts",
                            "value": "p_n_deal_type/23566065011",
                            "refinement_display_name": "Deals & Discounts"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=p_n_deal_type%3A23566064011&dc&qid=1748864616&rnid=23566063011&ref=sr_nr_p_n_deal_type_2&ds=v1%3AXKMStmu9KGYbBLcWxe2jyNxOvoAL4a7kK6bawUJb43s",
                            "name": "Today's Deals",
                            "value": "p_n_deal_type/23566064011",
                            "refinement_display_name": "Deals & Discounts"
                        }
                    ],
                    "customer_reviews": [
                        {
                            "link": "/s?k=nirvana+tshirt&rh=p_72%3A2661618011&dc&qid=1748864616&rnid=2661617011&ref=sr_nr_p_72_1&ds=v1%3Ay7a3VMhMk%2BMcmtLrol%2Bc5%2BcWqP55q2vnfKNI651RSLA",
                            "name": "4 Stars",
                            "value": "p_72/2661618011",
                            "refinement_display_name": "Customer Reviews"
                        }
                    ],
                    "shirt_neck_style": [
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_nineteen_browse-bin%3A2359340011&dc&qid=1748864616&rnid=2359337011&ref=sr_nr_p_n_feature_nineteen_browse-bin_1&ds=v1%3ABe1C13%2FyqrO%2FRn9y8j3jZqtmke2jSB%2F32Xm4Qaf6rm8",
                            "name": "Crew Neck",
                            "value": "n:7141123011,p_n_feature_nineteen_browse-bin/2359340011",
                            "refinement_display_name": "Shirt Neck Style"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_nineteen_browse-bin%3A2359351011&dc&qid=1748864616&rnid=2359337011&ref=sr_nr_p_n_feature_nineteen_browse-bin_2&ds=v1%3AhPJYnc4vSyyBno1Skn%2FBU1gzmUJC3ENBckEQaiCchdY",
                            "name": "V Neck",
                            "value": "n:7141123011,p_n_feature_nineteen_browse-bin/2359351011",
                            "refinement_display_name": "Shirt Neck Style"
                        },

                        {"...": "..."},

                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_nineteen_browse-bin%3A2359348011&dc&qid=1748864616&rnid=2359337011&ref=sr_nr_p_n_feature_nineteen_browse-bin_8&ds=v1%3A7XYh4uAdEXbPhmkvxLV4xJkZ8fsst%2BlmkeDRxq9KAv8",
                            "name": "Scoop Neck",
                            "value": "n:7141123011,p_n_feature_nineteen_browse-bin/2359348011",
                            "refinement_display_name": "Shirt Neck Style"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_nineteen_browse-bin%3A6053176011&dc&qid=1748864616&rnid=2359337011&ref=sr_nr_p_n_feature_nineteen_browse-bin_9&ds=v1%3AINHvhr6AhMt2GhSKcJ2y%2F%2BggCvF6cAUji1EWw0cDZ48",
                            "name": "Sweetheart Neck",
                            "value": "n:7141123011,p_n_feature_nineteen_browse-bin/6053176011",
                            "refinement_display_name": "Shirt Neck Style"
                        }
                    ],
                    "care_instructions": [
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_twenty-two_browse-bin%3A120826545011&dc&qid=1748864616&rnid=120826542011&ref=sr_nr_p_n_feature_twenty-two_browse-bin_1&ds=v1%3AraAIj31wfPgcOHUex4pvKWdSQ1fCDurvq1GQhRyO6nk",
                            "name": "Dry Clean Only",
                            "value": "n:7141123011,p_n_feature_twenty-two_browse-bin/120826545011",
                            "refinement_display_name": "Care Instructions"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_twenty-two_browse-bin%3A120826544011&dc&qid=1748864616&rnid=120826542011&ref=sr_nr_p_n_feature_twenty-two_browse-bin_2&ds=v1%3AaQHkyIOhuTHWb5BJdJN1CdivWy69K4qGgfyD4tO9cEE",
                            "name": "Hand Wash Only",
                            "value": "n:7141123011,p_n_feature_twenty-two_browse-bin/120826544011",
                            "refinement_display_name": "Care Instructions"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_twenty-two_browse-bin%3A120826543011&dc&qid=1748864616&rnid=120826542011&ref=sr_nr_p_n_feature_twenty-two_browse-bin_3&ds=v1%3ABmHnpmujlA%2FzvvDwYiJGnm0rCBF7ewyWOOq2cqT8b6Q",
                            "name": "Machine Wash",
                            "value": "n:7141123011,p_n_feature_twenty-two_browse-bin/120826543011",
                            "refinement_display_name": "Care Instructions"
                        }
                    ],
                    "clothing_material": [
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_material_browse%3A31310053011&dc&qid=1748864616&rnid=31310038011&ref=sr_nr_p_n_material_browse_1&ds=v1%3AiXxq9nmpVxgAkVTPVFK03JwsKbIcOMPXlL5%2FGXkwrnc",
                            "name": "Cotton",
                            "value": "n:7141123011,p_n_material_browse/31310053011",
                            "refinement_display_name": "Clothing Material"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_material_browse%3A31310042011&dc&qid=1748864616&rnid=31310038011&ref=sr_nr_p_n_material_browse_2&ds=v1%3ANrOHaaoSUx%2Bm66vztvoKGtWcTTxVlIn4sVQ%2BJl82Yb8",
                            "name": "Polyester",
                            "value": "n:7141123011,p_n_material_browse/31310042011",
                            "refinement_display_name": "Clothing Material"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_material_browse%3A31310052011&dc&qid=1748864616&rnid=31310038011&ref=sr_nr_p_n_material_browse_3&ds=v1%3AeAU9j9jJnh2lYQ%2FC8jxXybpweh%2B%2B7hI004wbAhCDDik",
                            "name": "Silk",
                            "value": "n:7141123011,p_n_material_browse/31310052011",
                            "refinement_display_name": "Clothing Material"
                        }
                    ],
                    "mens_clothing_size": [
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_pt_nav_size_men_international_size%3A2475466011&dc&qid=1748864616&rnid=2475465011&ref=sr_nr_p_n_pt_nav_size_men_international_size_1&ds=v1%3AVdGjhQztI61wby3dzMDgySmp75ZNJ2kWuc6BPB9eVw4",
                            "name": "XS",
                            "value": "n:7141123011,p_n_pt_nav_size_men_international_size/2475466011",
                            "refinement_display_name": "Men's Clothing Size"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_pt_nav_size_men_international_size%3A2475467011&dc&qid=1748864616&rnid=2475465011&ref=sr_nr_p_n_pt_nav_size_men_international_size_2&ds=v1%3AXpx6Y1rQhkM4eAY3r%2F9v9Ys1stqldQl%2Fiz2yOMeAViQ",
                            "name": "S",
                            "value": "n:7141123011,p_n_pt_nav_size_men_international_size/2475467011",
                            "refinement_display_name": "Men's Clothing Size"
                        },

                        {"...": "..."},

                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_pt_nav_size_men_international_size%3A2475473011&dc&qid=1748864616&rnid=2475465011&ref=sr_nr_p_n_pt_nav_size_men_international_size_8&ds=v1%3AtwaGT16HYbkNZT%2Bqs5KgSMg5SzwdI5H4AZWs%2FLaXUl8",
                            "name": "4XL",
                            "value": "n:7141123011,p_n_pt_nav_size_men_international_size/2475473011",
                            "refinement_display_name": "Men's Clothing Size"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_pt_nav_size_men_international_size%3A2475474011&dc&qid=1748864616&rnid=2475465011&ref=sr_nr_p_n_pt_nav_size_men_international_size_9&ds=v1%3A6PR%2FvaJAeuHJCv%2FM51A2T1yrYAgNbahAxrsqKYxCHHw",
                            "name": "5XL",
                            "value": "n:7141123011,p_n_pt_nav_size_men_international_size/2475474011",
                            "refinement_display_name": "Men's Clothing Size"
                        }
                    ],
                    "novelty_apparel_theme": [
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_pt_nav_size_boy_size_three%3A17051383011&dc&qid=1748864616&rnid=9214012011&ref=sr_nr_p_n_pt_nav_size_boy_size_three_1&ds=v1%3AYlXPRNSAKU%2BCbzUV%2FMxgYyKz8ZBnS1PGNiru8ZI%2FAm0",
                            "name": "Music & Band",
                            "value": "n:7141123011,p_n_pt_nav_size_boy_size_three/17051383011",
                            "refinement_display_name": "Novelty Apparel Theme"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_pt_nav_size_boy_size_three%3A9214016011&dc&qid=1748864616&rnid=9214012011&ref=sr_nr_p_n_pt_nav_size_boy_size_three_2&ds=v1%3Ar3FztVvfWRxmmUcoCmtKLcEKjwhMxLjSVJAFOKo8wrw",
                            "name": "Birthday",
                            "value": "n:7141123011,p_n_pt_nav_size_boy_size_three/9214016011",
                            "refinement_display_name": "Novelty Apparel Theme"
                        },

                        {"...": "..."},
                        
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_pt_nav_size_boy_size_three%3A9214033011&dc&qid=1748864616&rnid=9214012011&ref=sr_nr_p_n_pt_nav_size_boy_size_three_11&ds=v1%3AxqbyjrYpDi%2BHM5ouDo0svzbzbfA2nEkZJApctFwc1zo",
                            "name": "Sports",
                            "value": "n:7141123011,p_n_pt_nav_size_boy_size_three/9214033011",
                            "refinement_display_name": "Novelty Apparel Theme"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_pt_nav_size_boy_size_three%3A9214036011&dc&qid=1748864616&rnid=9214012011&ref=sr_nr_p_n_pt_nav_size_boy_size_three_12&ds=v1%3AKVlqXERw5qoj5pXgcJEkjUJWnuawh8StP%2Fm9KpiLYkY",
                            "name": "Workout",
                            "value": "n:7141123011,p_n_pt_nav_size_boy_size_three/9214036011",
                            "refinement_display_name": "Novelty Apparel Theme"
                        }
                    ],
                    "special_clothing_size": [
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_shoe_width_browse-vebin%3A492380011&dc&qid=1748864616&rnid=492378011&ref=sr_nr_p_n_shoe_width_browse-vebin_1&ds=v1%3Ae1OmG4%2Beq2j3OENwIPXY9%2B9UDTomVbqmk6EhNDEDP4U",
                            "name": "Big & Tall",
                            "value": "n:7141123011,p_n_shoe_width_browse-vebin/492380011",
                            "refinement_display_name": "Special Clothing Size"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_shoe_width_browse-vebin%3A13130370011&dc&qid=1748864616&rnid=492378011&ref=sr_nr_p_n_shoe_width_browse-vebin_2&ds=v1%3AuurkT4ukFDHZYkSOwVLKitpyo7KtWRx%2FRS75JVMzlEk",
                            "name": "Juniors",
                            "value": "n:7141123011,p_n_shoe_width_browse-vebin/13130370011",
                            "refinement_display_name": "Special Clothing Size"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_shoe_width_browse-vebin%3A492383011&dc&qid=1748864616&rnid=492378011&ref=sr_nr_p_n_shoe_width_browse-vebin_3&ds=v1%3AFXJaclj%2Futfvh2Hw5bw2oTmT8%2B19J%2FPi%2FK4KxN37Bb8",
                            "name": "Petite",
                            "value": "n:7141123011,p_n_shoe_width_browse-vebin/492383011",
                            "refinement_display_name": "Special Clothing Size"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_shoe_width_browse-vebin%3A492379011&dc&qid=1748864616&rnid=492378011&ref=sr_nr_p_n_shoe_width_browse-vebin_4&ds=v1%3AEjyz7l3j2UYzVjF0LLEPAHyptbSvZT4y6rDMrKsTtkc",
                            "name": "Plus Size",
                            "value": "n:7141123011,p_n_shoe_width_browse-vebin/492379011",
                            "refinement_display_name": "Special Clothing Size"
                        }
                    ],
                    "more_sustainable_products": [
                        {
                            "link": "/s?k=nirvana+tshirt&rh=p_n_cpf_eligible%3A21512497011&dc&qid=1748864616&rnid=21512496011&ref=sr_nr_p_n_cpf_eligible_1&ds=v1%3Aee09XDMEzcb5nr%2B%2BBRZtuH4IEQ2DPIG4NA4yGD0h8eA",
                            "name": "Climate Pledge Friendly",
                            "value": "p_n_cpf_eligible/21512497011",
                            "refinement_display_name": "More-sustainable Products"
                        }
                    ],
                    "sleeve_length_description": [
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_browse-bin%3A368722011&dc&qid=1748864616&rnid=368720011&ref=sr_nr_p_n_feature_browse-bin_1&ds=v1%3AXK3qIuzyjPpC8K8HWc8f2047vsLWD%2FzSCSAm0MHvYm4",
                            "name": "Short Sleeve",
                            "value": "n:7141123011,p_n_feature_browse-bin/368722011",
                            "refinement_display_name": "Sleeve Length Description"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_browse-bin%3A368723011&dc&qid=1748864616&rnid=368720011&ref=sr_nr_p_n_feature_browse-bin_2&ds=v1%3AyyeKkTJN%2FNGVfHUBv9sdsjozwuNj4XJFKOYZJL9sDRI",
                            "name": "Long Sleeve",
                            "value": "n:7141123011,p_n_feature_browse-bin/368723011",
                            "refinement_display_name": "Sleeve Length Description"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_browse-bin%3A370089011&dc&qid=1748864616&rnid=368720011&ref=sr_nr_p_n_feature_browse-bin_3&ds=v1%3AaDjT%2FQqFbxiNzrJQRzyetEs5mao6AtfGjaw9jvWsuNs",
                            "name": "Sleeveless",
                            "value": "n:7141123011,p_n_feature_browse-bin/370089011",
                            "refinement_display_name": "Sleeve Length Description"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_browse-bin%3A50382011&dc&qid=1748864616&rnid=368720011&ref=sr_nr_p_n_feature_browse-bin_4&ds=v1%3ALLf5i8JY%2BSCr5zPfqXRTOZpB2SP%2FxbW1rnjii3N4d%2FI",
                            "name": "3/4 Sleeve",
                            "value": "n:7141123011,p_n_feature_browse-bin/50382011",
                            "refinement_display_name": "Sleeve Length Description"
                        },
                        {
                            "link": "/s?k=nirvana+tshirt&rh=n%3A7141123011%2Cp_n_feature_browse-bin%3A23575156011&dc&qid=1748864616&rnid=368720011&ref=sr_nr_p_n_feature_browse-bin_5&ds=v1%3AJ5do%2BFqSczzFN8D7Lj9LrPmRswiryxemP3hl8TguNGc",
                            "name": "Half Sleeve",
                            "value": "n:7141123011,p_n_feature_browse-bin/23575156011",
                            "refinement_display_name": "Sleeve Length Description"
                        }
                    ],
                    "eligible_for_free_shipping": [
                        {
                            "link": "/s?k=nirvana+tshirt&rh=p_76%3A2661625011&dc&qid=1748864616&rnid=2661623011&ref=sr_nr_p_76_1&ds=v1%3AUM%2F5e8hRJoxxFO9n6pN7bfOYlX1Rou%2FS8MQuiQKbjAQ",
                            "name": "Free Shipping by Amazon",
                            "value": "p_76/2661625011",
                            "refinement_display_name": "Eligible for Free Shipping"
                        }
                    ]
                },
                "last_visible_page": 7,
                "parse_status_code": 12000
            },
            "created_at": "2025-06-02 11:43:35",
            "updated_at": "2025-06-02 11:43:37",
            "page": 1,
            "url": "https://www.amazon.com/s?k=nirvana%20tshirt&page=1",
            "job_id": "7335269853705561089",
            "is_render_forced": false,
            "status_code": 200,
            "parser_type": "",
            "parser_preset": null
        }
    ],
    "job": {
        "callback_url": null,
        "client_id": 100420,
        "context": [
            {
                "key": "force_headers",
                "value": false
            },
            {
                "key": "force_cookies",
                "value": false
            },
            {
                "key": "hc_policy",
                "value": true
            },
            {
                "key": "category_id",
                "value": null
            },
            {
                "key": "merchant_id",
                "value": null
            },
            {
                "key": "check_empty_geo",
                "value": null
            },
            {
                "key": "safe_search",
                "value": true
            },
            {
                "key": "currency",
                "value": null
            },
            {
                "key": "sort_by",
                "value": null
            },
            {
                "key": "refinements",
                "value": null
            },
            {
                "key": "min_price",
                "value": null
            },
            {
                "key": "max_price",
                "value": null
            }
        ],
        "created_at": "2025-06-02 11:43:35",
        "domain": "com",
        "geo_location": null,
        "id": "7335269853705561089",
        "limit": 10,
        "locale": null,
        "pages": 1,
        "parse": true,
        "parser_type": null,
        "parser_preset": null,
        "parsing_instructions": null,
        "browser_instructions": null,
        "render": null,
        "xhr": false,
        "url": null,
        "query": "nirvana tshirt",
        "source": "amazon_search",
        "start_page": 1,
        "status": "done",
        "storage_type": null,
        "storage_url": null,
        "subdomain": "www",
        "content_encoding": "utf-8",
        "updated_at": "2025-06-02 11:43:37",
        "user_agent_type": "desktop",
        "session_info": null,
        "statuses": [],
        "client_notes": null,
        "_links": [
            {
                "rel": "self",
                "href": "http://data.oxylabs.io/v1/queries/7335269853705561089",
                "method": "GET"
            },
            {
                "rel": "results",
                "href": "http://data.oxylabs.io/v1/queries/7335269853705561089/results",
                "method": "GET"
            },
            {
                "rel": "results-content",
                "href_list": [
                    "http://data.oxylabs.io/v1/queries/7335269853705561089/results/1/content"
                ],
                "method": "GET"
            },
            {
                "rel": "results-html",
                "href": "http://data.oxylabs.io/v1/queries/7335269853705561089/results?type=raw",
                "method": "GET"
            },
            {
                "rel": "results-content-html",
                "href_list": [
                    "http://data.oxylabs.io/v1/queries/7335269853705561089/results/1/content?type=raw"
                ],
                "method": "GET"
            },
            {
                "rel": "results-parsed",
                "href": "http://data.oxylabs.io/v1/queries/7335269853705561089/results?type=parsed",
                "method": "GET"
            },
            {
                "rel": "results-content-parsed",
                "href_list": [
                    "http://data.oxylabs.io/v1/queries/7335269853705561089/results/1/content?type=parsed"
                ],
                "method": "GET"
            }
        ]
    }
}
```

{% hint style="info" %}
The output sample is shortened.
{% endhint %}

</details>

## Output data dictionary

API returns a HTML or JSON object that contains the search results retrieved from the Amazon.

#### HTML example

<figure><img src="https://63892162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzrXw45naRpCZ0Ku9AjY1%2Fuploads%2FonQ5S0yktQXOgtmB2bsZ%2Famazon_search.png?alt=media&#x26;token=fe7fdabc-f46a-47a6-b69f-80a71bf33be1" alt=""><figcaption></figcaption></figure>

#### JSON structure

All search results are contained within the `results` JSON array. Each search result includes a combination of `paid`, `organic`, `suggested`, `amazons_choices`,`instant_recommendations` listings. Additionally, variations may be present, and they are captured within the `variations` key, providing details about different types or categories of products, such as various models, editions, or versions.

<table><thead><tr><th width="277.6666666666667">Key</th><th width="302">Description</th><th>Type</th></tr></thead><tbody><tr><td><code>url</code></td><td>The URL of the Amazon search page.</td><td>string</td></tr><tr><td><code>page</code></td><td>The current page number.</td><td>integer</td></tr><tr><td><code>pages</code></td><td>The total number of pages.</td><td>integer</td></tr><tr><td><code>query</code></td><td>The search query used.</td><td>string</td></tr><tr><td><code>results</code></td><td>A dictionary containing the results of the search.</td><td>object</td></tr><tr><td><code>results.paid</code></td><td>A list of sponsored products with their respective details.</td><td>array</td></tr><tr><td><code>results.organic</code></td><td>A list of organic products with their respective details.</td><td>array</td></tr><tr><td><code>results.suggested</code></td><td>A list of suggested products with their respective details.</td><td>array</td></tr><tr><td><code>results.amazons_choices</code></td><td>A list of Amazon's choices with their respective details.</td><td>array</td></tr><tr><td><code>refinements</code></td><td>A list of refinements available on this search page.</td><td>array</td></tr><tr><td><code>parse_status_code</code></td><td>The status code of the parsing job. You can see the parser status codes described <a href="https://github.com/oxylabs/gitbook-public-english/blob/master/scraping-solutions/web-scraper-api/targets/amazon/broken-reference/README.md"><strong>here</strong></a>.</td><td>integer</td></tr><tr><td><code>total_results_count</code></td><td>The total number of results found for the search query.</td><td>integer</td></tr><tr><td><code>created_at</code></td><td>The timestamp when the scraping job was created.</td><td>string</td></tr><tr><td><code>updated_at</code></td><td>The timestamp when the scraping job was finished.</td><td>string</td></tr><tr><td><code>job_id</code></td><td>The ID of the job associated with the scraping job.</td><td>string</td></tr><tr><td><code>status_code</code></td><td>The status code of the scraping job. You can see the scraper status codes described <a href="../../response-codes"><strong>here</strong></a>.</td><td>integer</td></tr><tr><td><code>parser_type</code></td><td>The type of parser used for parsing the data.</td><td>string</td></tr></tbody></table>

{% hint style="info" %}
In the following sections, parsed JSON code snippets are shortened where more than one item for the result type is available.
{% endhint %}

### Paid

The `paid` section of the search results refers to inline ad content that is displayed within the Amazon search results.

<figure><img src="https://63892162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzrXw45naRpCZ0Ku9AjY1%2Fuploads%2FIsZJcLJYnrbAVInPmDg1%2Fimage.png?alt=media&#x26;token=edf75c51-0558-4ef4-96bb-45356ac96c5c" alt=""><figcaption></figcaption></figure>

```json
...
"paid": [
    {
        "pos": 1,
        "url": "/sspa/click?ie=UTF8&spc=MTo3ODk3NzcxNTI0MDAzNjk1OjE3MDEwODYyODI6c3BfYXRmOjMwMDA5Mjg4ODc1NTcwMjo6MDo6&url=/IOGEAR-KeyMander-Controller-Crossover-GE1337P2/dp/B08541QCKJ/ref=sr_1_1_sspa?keywords=nintendo&qid=1701086282&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
        "asin": "B08541QCKJ",
        "price": 69.99,
        "title": "IOGEAR KeyMander 2 Keyboard/Mouse Adapter Plus Controller Crossover, PS4, PS5, Xbox Series X/S, Xbox One, Nintendo Switch, GE1337P2, FPS, mouse control",
        "rating": 3.7,
        "currency": "USD",
        "is_prime": true,
        "url_image": "https://m.media-amazon.com/images/I/41-AZ8CCl1L._AC_UY218_.jpg",
        "best_seller": false,
        "price_upper": 69.99,
        "is_sponsored": true,
        "manufacturer": "",
        "pricing_count": 1,
        "reviews_count": 1229,
        "is_amazons_choice": false,
        "price_strikethrough": 99.95,
        "shipping_information": "FREE delivery Sun, Dec 3 Or fastest delivery Thu, Nov 30"
    },
    ...
]
```

<table><thead><tr><th width="251.66666666666669">Key</th><th width="304">Description</th><th>Type</th></tr></thead><tbody><tr><td><code>url</code></td><td>The URL of the product.</td><td>string</td></tr><tr><td><code>asin</code></td><td>Amazon Standard Identification Number.</td><td>string</td></tr><tr><td><code>price</code></td><td>The price of the product.</td><td>float</td></tr><tr><td><code>title</code></td><td>The title of the product.</td><td>string</td></tr><tr><td><code>rating</code></td><td>The rating of the product.</td><td>float</td></tr><tr><td><code>rel_pos</code></td><td><p>The relative position of the product in the search results.</p><p>(either <code>pos</code> or <code>rel_pos</code> is present)</p></td><td>integer</td></tr><tr><td><code>pos</code></td><td>A unique indicator denoting the position in the listing. (either <code>pos</code> or <code>rel_pos</code> is present)</td><td>integer</td></tr><tr><td><code>currency</code></td><td>The currency in which the price is denominated.</td><td>string</td></tr><tr><td><code>url_image</code></td><td>The URL of the product image.</td><td>string</td></tr><tr><td><code>best_seller</code></td><td>Indicates whether the product is a best seller.</td><td>boolean</td></tr><tr><td><code>price_upper</code></td><td>The upper limit of the price if applicable.</td><td>float</td></tr><tr><td><code>is_sponsored</code></td><td>Indicates whether the product is sponsored.</td><td>boolean</td></tr><tr><td><code>manufacturer</code></td><td>The name of the manufacturer of the product.</td><td>string</td></tr><tr><td><code>pricing_count</code></td><td>The count of offers for the product.</td><td>integer</td></tr><tr><td><code>reviews_count</code></td><td>The count of reviews for the product.</td><td>integer</td></tr><tr><td><code>coupon_discount</code></td><td>The discounted amount.</td><td>integer (optional)</td></tr><tr><td><code>coupon_discount_type</code></td><td>The type of discount: <code>nominal</code> or <code>percentage</code>.</td><td>string (optional)</td></tr><tr><td><code>is_amazons_choice</code></td><td>Indicates whether the product is marked as "Amazon's choice".</td><td>boolean</td></tr><tr><td><code>no_price_reason</code></td><td>Indicator why the price is not present, if it's equal to 0.0</td><td>string (optional)</td></tr><tr><td><code>sales_volume</code></td><td>The sales volume or number of units sold for a particular product.</td><td>string (optional)</td></tr><tr><td><code>is_prime</code></td><td>Indicates whether the product is eligible for Amazon Prime.</td><td>boolean</td></tr><tr><td><code>shipping_information</code></td><td>Information about the shipping details for the produc</td><td>string</td></tr></tbody></table>

### Organic

The `organic` section of the search results refers to non-sponsored content that appears naturally based on Amazon's search algorithm.

<figure><img src="https://63892162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzrXw45naRpCZ0Ku9AjY1%2Fuploads%2FEX09S6CKHx4bPQhNu9rw%2Famazon_search_organic.png?alt=media&#x26;token=06384ec5-d4e7-4306-ab13-f80926e05b23" alt=""><figcaption></figcaption></figure>

```json
...
"organic": [
    ...
    {
        "pos": 5,
        "url": "/Purifiers-2200sq-ft-MOOKA-purifier-PR1/dp/B0DCBC8KKV/ref=sr_1_5?dib=eyJ2IjoiMSJ9.Qoe5cUAPMM1voliSq4zLfiJ0JVl_hsy805T9yDeoZdvRcrqICV-PjwCg0I67jvJVJ_PSunMweX8SvSH3-M-pI2-ugdCQ85ZkACZeyo0mFA_x-tDj-q1JTf8V3SdCA7KJlxMyHDeIT2N6NHGk7cyVsOpK-UlfWiNJ-dnu6KUIZcC82Zm0ugL-vdGTf8Qj-uDJJcWp35jlmA3m6N3XV3l8BuJVNVIXrsniboQa_FpLjLY.o9cWjzsvdrHpX_CV82v3VY104qfYcK7CkfXDFYuwlC8&dib_tag=se&keywords=air+purifier&qid=1753104496&sr=8-5",
        "asin": "B0DCBC8KKV",
        "price": 99.99,
        "title": "Air Purifiers for Home Large Room up to 2200sq.ft, MOOKA Air purifier for Home Pets with Washable Filter, PM 2.5 Display Air Quality Sensor Air Cleaner for Bedroom, Dorm room, Pets, Office, PR1",
        "rating": 4.6,
        "currency": "USD",
        "is_prime": false,
        "url_image": "https://m.media-amazon.com/images/I/81spn7Ork+L._AC_UY218_.jpg",
        "best_seller": false,
        "price_upper": 99.99,
        "is_sponsored": false,
        "manufacturer": "",
        "sales_volume": "10K+ bought in past month",
        "pricing_count": 1,
        "reviews_count": 1431,
        "coupon_discount": 15,
        "is_amazons_choice": false,
        "price_strikethrough": 105.97,
        "coupon_discount_type": "nominal",
        "shipping_information": "FREE delivery Sat, Jul 26Or fastest delivery Wed, Jul 23"
    },
    ...
]
```

<table><thead><tr><th>Name</th><th width="272.6666666666667">Description</th><th>Type</th></tr></thead><tbody><tr><td><code>pos</code></td><td>A unique indicator denoting the position in the listing.</td><td>integer</td></tr><tr><td><code>url</code></td><td>The URL of the product.</td><td>string</td></tr><tr><td><code>asin</code></td><td>Amazon Standard Identification Number.</td><td>string</td></tr><tr><td><code>price</code></td><td>The price of the product.</td><td>float</td></tr><tr><td><code>title</code></td><td>The title of the product.</td><td>string</td></tr><tr><td><code>rating</code></td><td>The rating of the product.</td><td>float</td></tr><tr><td><code>currency</code></td><td>The currency in which the price is denominated.</td><td>string</td></tr><tr><td><code>is_prime</code></td><td>Indicates whether the product is eligible for Amazon Prime.</td><td>boolean</td></tr><tr><td><code>url_image</code></td><td>The URL of the product image.</td><td>string</td></tr><tr><td><code>best_seller</code></td><td>Indicates whether the product is a best seller.</td><td>boolean</td></tr><tr><td><code>price_upper</code></td><td>The upper limit of the price if applicable.</td><td>float</td></tr><tr><td><code>is_sponsored</code></td><td>Indicates whether the product is sponsored.</td><td>boolean</td></tr><tr><td><code>manufacturer</code></td><td>The name of the manufacturer of the product.</td><td>string</td></tr><tr><td><code>sales_volume</code></td><td>The sales volume or number of units sold for a particular product.</td><td>string (optional)</td></tr><tr><td><code>pricing_count</code></td><td>The count of pricings for the product.</td><td>integer</td></tr><tr><td><code>reviews_count</code></td><td>The count of reviews for the product.</td><td>integer</td></tr><tr><td><code>coupon_discount</code></td><td>The discounted amount.</td><td>integer (optional)</td></tr><tr><td><code>coupon_discount_type</code></td><td>The type of discount: <code>nominal</code> or <code>percentage</code>.</td><td>string (optional)</td></tr><tr><td><code>is_amazons_choice</code></td><td>Indicates whether the product is Amazon's choice.</td><td>boolean</td></tr><tr><td><code>price_strikethrough</code></td><td>Original price before any discounts.</td><td>float</td></tr><tr><td><code>shipping_information</code></td><td>Delivery dates and shipping cost details.</td><td>string</td></tr><tr><td><code>no_price_reason</code></td><td>Indicator why the price is not present, if it's equal to 0.0</td><td>string (optional)</td></tr><tr><td><code>variations</code></td><td>List of different versions or models of a product</td><td>Array</td></tr></tbody></table>

### Suggested

The `suggested` section in the search results typically contains product listings recommended by the platform based on the user's search query, browsing history, or purchase behavior.

<figure><img src="https://63892162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzrXw45naRpCZ0Ku9AjY1%2Fuploads%2FfHi6uxMMCeCOAxRjOvUi%2Fimage.png?alt=media&#x26;token=cf7c303f-3a98-429e-ae38-927f1d49ef88" alt=""><figcaption></figcaption></figure>

```json
...
"suggested": [
    {
        "pos": 3,
        "asin": "B07L4ZRJ7P",
        "best_seller": false,
        "is_sponsored": false,
        "is_amazons_choice": false,
        "manufacturer": "",
        "pricing_count": 1,
        "rating": 4.0,
        "reviews_count": 1,
        "title": "The Supercar Story",
        "url": "/Supercar-Story-Patrick-Mark/dp/B07L4ZRJ7P/ref=sr_1_fkmr0_1?keywords=details about mercedes benz head unit e-class w213 comand navi gps unit a21390050813&qid=1636460216&sr=8-1-fkmr0",
        "url_image": "https://m.media-amazon.com/images/I/81uC-IclZqL._AC_UY218_.jpg",
        "is_prime": false,
        "price": 0.0,
        "price_upper": 0.0,
        "no_price_reason": "unknown",
        "pos": 1,
        "currency": "USD",
        "suggested_query": "details benz head"
    },
    ...
]
```

<table><thead><tr><th width="250">Key</th><th width="277.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td><code>url</code></td><td>The URL of the product.</td><td>string</td></tr><tr><td><code>asin</code></td><td>Amazon Standard Identification Number.</td><td>string</td></tr><tr><td><code>price</code></td><td>The price of the product.</td><td>float</td></tr><tr><td><code>title</code></td><td>The title of the product.</td><td>string</td></tr><tr><td><code>rating</code></td><td>The rating of the product.</td><td>float</td></tr><tr><td><code>currency</code></td><td>The currency in which the price is denominated.</td><td>string</td></tr><tr><td><code>url_image</code></td><td>The URL of the product image.</td><td>string</td></tr><tr><td><code>best_seller</code></td><td>Indicates whether the product is a best seller.</td><td>boolean</td></tr><tr><td><code>price_upper</code></td><td>The upper limit of the price if applicable.</td><td>float</td></tr><tr><td><code>is_sponsored</code></td><td>Indicates whether the product is sponsored.</td><td>boolean</td></tr><tr><td><code>manufacturer</code></td><td>The name of the manufacturer of the product.</td><td>string</td></tr><tr><td><code>pricing_count</code></td><td>The count of pricing for the product.</td><td>integer</td></tr><tr><td><code>reviews_count</code></td><td>The count of reviews for the product.</td><td>integer</td></tr><tr><td><code>coupon_discount</code></td><td>The discounted amount.</td><td>integer (optional)</td></tr><tr><td><code>coupon_discount_type</code></td><td>The type of discount: <code>nominal</code> or <code>percentage</code>.</td><td>string (optional)</td></tr><tr><td><code>is_amazons_choice</code></td><td>Indicates whether the product is Amazon's choice.</td><td>boolean</td></tr><tr><td><code>pos</code></td><td>A unique indicator denoting the position in the listing.</td><td>integer</td></tr><tr><td><code>is_prime</code></td><td>Indicates whether the product is eligible for Amazon Prime.</td><td>boolean</td></tr><tr><td><code>shipping_information</code></td><td>Information about the shipping details for the product.</td><td>string</td></tr><tr><td><code>sales_volume</code></td><td>The sales volume or number of units sold for a particular product.</td><td>string (optional)</td></tr><tr><td><code>no_price_reason</code></td><td>Indicator why the price is not present, if it's equal to 0.0</td><td>string (optional)</td></tr><tr><td><code>suggested_query</code></td><td>The suggested query provided by Amazon as part of the search results.</td><td>string</td></tr></tbody></table>

### Amazon's Choices

The `amazons_choices` section features products with 'Amazon's Choice' badge and are recommended by the platform for their perceived quality and value.

<figure><img src="https://63892162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzrXw45naRpCZ0Ku9AjY1%2Fuploads%2Fg6WiCVtyqMgxvrr0A2qk%2Fimage.png?alt=media&#x26;token=85a25861-abbe-4953-a22b-039af97bb27a" alt=""><figcaption></figcaption></figure>

```json
...
"amazons_choices": [
    {
        "asin": "B07STGGQ18",
        "best_seller": false,
        "is_sponsored": false,
        "is_amazons_choice": true,
        "manufacturer": "",
        "pricing_count": 1,
        "rating": 4.8,
        "reviews_count": 9,
        "title": "AMD Ryzen 5 3600 4, 2GHz AM4 35MB Cache Wraith Stealth",
        "url": "/AMD-Ryzen-3600-Wraith-Stealth/dp/B07STGGQ18/ref=sr_1_3?dchild=1&keywords=0730143309936&qid=1600153905&sr=8-3",
        "url_image": "https://m.media-amazon.com/images/I/71WPGXQLcLL._AC_UY218_.jpg",
        "is_prime": true,
        "price": 179.0,
        "price_upper": 179.0,
        "shipping_information": "Lieferung bis Freitag, 18. September GRATIS Versand durch Amazon",
        "pos": 3,
        "currency": "EUR"
    },
    ...
]
```

<table><thead><tr><th width="252">Key</th><th width="286.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td><code>url</code></td><td>The URL of the product.</td><td>string</td></tr><tr><td><code>asin</code></td><td>Amazon Standard Identification Number.</td><td>string</td></tr><tr><td><code>price</code></td><td>The price of the product.</td><td>float</td></tr><tr><td><code>title</code></td><td>The title of the product.</td><td>string</td></tr><tr><td><code>rating</code></td><td>The rating of the product.</td><td>float</td></tr><tr><td><code>currency</code></td><td>The currency in which the price is denominated.</td><td>string</td></tr><tr><td><code>url_image</code></td><td>The URL of the product image.</td><td>string</td></tr><tr><td><code>best_seller</code></td><td>Indicates whether the product is a best seller.</td><td>boolean</td></tr><tr><td><code>price_upper</code></td><td>The upper limit of the price if applicable.</td><td>float</td></tr><tr><td><code>is_sponsored</code></td><td>Indicates whether the product is sponsored.</td><td>boolean</td></tr><tr><td><code>manufacturer</code></td><td>The name of the manufacturer of the product.</td><td>string</td></tr><tr><td><code>pricing_count</code></td><td>The count of pricing for the product.</td><td>integer</td></tr><tr><td><code>reviews_count</code></td><td>The count of reviews for the product.</td><td>integer</td></tr><tr><td><code>coupon_discount</code></td><td>The discounted amount.</td><td>integer (optional)</td></tr><tr><td><code>coupon_discount_type</code></td><td>The type of discount: <code>nominal</code> or <code>percentage</code>.</td><td>string (optional)</td></tr><tr><td><code>is_amazons_choice</code></td><td>Indicates whether the product is Amazon's choice.</td><td>boolean</td></tr><tr><td><code>pos</code></td><td>A unique indicator denoting the position in the listing.</td><td>integer</td></tr><tr><td><code>is_prime</code></td><td>Indicates whether the product is eligible for Amazon Prime.</td><td>boolean</td></tr><tr><td><code>shipping_information</code></td><td>Information about the shipping details for the product.</td><td>string</td></tr><tr><td><code>sales_volume</code></td><td>The sales volume or number of units sold for a particular product.</td><td>string (optional)</td></tr><tr><td><code>no_price_reason</code></td><td>Indicator why the price is not present, if it's equal to 0.0</td><td>string (optional)</td></tr><tr><td><code>variations</code></td><td>List of different versions or models of a product</td><td>Array</td></tr></tbody></table>

### Variations

The `variations` section lists different versions or models of a product, providing a detailed overview of available options in the specified category.

<figure><img src="https://63892162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzrXw45naRpCZ0Ku9AjY1%2Fuploads%2FOBcuHla4GB9TgSjyPIG3%2Fimage.png?alt=media&#x26;token=3079b917-01a3-4d2c-b426-9d26d97eafe9" alt=""><figcaption></figcaption></figure>

```json
...
"variations": [
  {
    "asin": "B08KXB6SZH",
    "title": "PlayStation 5",
    "price": 29.99,
    "not_available": false
  },
  {
    "asin": "B08L6FZM6D",
    "title": "PlayStation 4",
    "not_available": false,
    "no_price_reason": "unknown"
  },
  {
    "asin": "B08N766Q9W",
    "title": "Xbox Digial Code",
    "not_available": true,
    "no_price_reason": "Currently unavailable."
  }
],
...
```

<table><thead><tr><th width="243.33333333333334">Key</th><th>Description</th><th>Type</th></tr></thead><tbody><tr><td><code>asin</code></td><td>Amazon Standard Identification Number</td><td>string</td></tr><tr><td><code>title</code></td><td>Title of the variation</td><td>string</td></tr><tr><td><code>price</code></td><td>Price of the variation</td><td>float</td></tr><tr><td><code>price_strikethrough</code></td><td>The original price before any discounts or promotions</td><td>float</td></tr><tr><td><code>not_available</code></td><td>Indicates if the variation is currently unavailable</td><td>boolean</td></tr></tbody></table>

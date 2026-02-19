# Sellers

The `amazon_sellers` data source is designed to retrieve Amazon Sellers pages.

{% hint style="info" %}
Explore output [**data dictionary**](#data-dictionary) for Sellers, offering a brief description, screenshot, parsed JSON code snippet, and a table defining each parsed field. Navigate through the details using the right-side navigation or scrolling down the page.
{% endhint %}

## Request samples

In the code examples below, we make a request to retrieve the seller page for seller ID `A2MUQS6AX5GGR` on `amazon.de` marketplace.

{% tabs %}
{% tab title="cURL" %}

```shell
curl 'https://realtime.oxylabs.io/v1/queries' \
--user 'USERNAME:PASSWORD' \
-H 'Content-Type: application/json' \
-d '{
        "source": "amazon_sellers", 
        "domain": "de", 
        "query": "A2MUQS6AX5GGR",
        "parse": true
    }'
```

{% endtab %}

{% tab title="Python" %}

```python
import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'amazon_sellers',
    'domain': 'de',
    'query': 'A2MUQS6AX5GGR',
    'parse': True
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
    source: "amazon_sellers",
    domain: "de",
    query: "A2MUQS6AX5GGR",
    parse: true,
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
https://realtime.oxylabs.io/v1/queries?source=amazon_sellers&domain=de&query=A2MUQS6AX5GGR&parse=true&access_token=12345abcde
```

{% endtab %}

{% tab title="PHP" %}

```php
<?php

$params = array(
    'source' => 'amazon_sellers',
    'domain' => 'de',
    'query' => 'A2MUQS6AX5GGR',
    'parse' => true
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
		"source": "amazon_sellers",
		"domain": "de",
		"query":  "A2MUQS6AX5GGR",
		"parse":  true,
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
                source = "amazon_sellers",
                domain = "de",
                query = "A2MUQS6AX5GGR",
                parse = true
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
import org.json.JSONObject;
import java.util.concurrent.TimeUnit;

public class Main implements Runnable {
    private static final String AUTHORIZATION_HEADER = "Authorization";
    public static final String USERNAME = "USERNAME";
    public static final String PASSWORD = "PASSWORD";
    public void run() {
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("source", "amazon_sellers");
        jsonObject.put("domain", "de");
        jsonObject.put("query", "A2MUQS6AX5GGR");
        jsonObject.put("parse", true);

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
    "source": "amazon_sellers", 
    "domain": "de", 
    "query": "A2MUQS6AX5GGR",
    "parse": true
}
```

{% endtab %}
{% endtabs %}

We use synchronous [**Realtime**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods/realtime) integration method in our examples. If you would like to use [**Proxy Endpoint**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods/proxy-endpoint) or asynchronous [**Push-Pull**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods/push-pull) integration, refer to the [**integration methods**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods) section.

## Request parameter values

### Generic

Basic setup and customization options for scraping Amazon Seller pages.

<table><thead><tr><th width="222">Parameter</th><th width="350.3333333333333">Description</th><th>Default Value</th></tr></thead><tbody><tr><td><mark style="background-color:green;"><strong>source</strong></mark></td><td>Sets the scraper.</td><td><code>amazon_sellers</code></td></tr><tr><td><mark style="background-color:green;"><strong>query</strong></mark></td><td>Seller ID code.</td><td>-</td></tr><tr><td><code>render</code></td><td>Enables JavaScript rendering when set to <code>html</code>. <a href="../../features/js-rendering-and-browser-control/javascript-rendering"><strong>More info</strong></a><strong>.</strong></td><td>-</td></tr><tr><td><code>parse</code></td><td>Returns parsed data when set to <code>true</code>. Explore output <a href="#output-data-dictionary"><strong>data dictionary</strong></a>.</td><td><code>false</code></td></tr><tr><td><code>callback_url</code></td><td>URL to your callback endpoint. <a href="../../../integration-methods/push-pull#callback"><strong>More info</strong></a>.</td><td>-</td></tr><tr><td><code>user_agent_type</code></td><td>Device type and browser. The full list can be found <a href="../../features/http-context-and-job-management/user-agent-type"><strong>here</strong></a>.</td><td><code>desktop</code></td></tr></tbody></table>

&#x20;   \- mandatory parameter

### Localization

Adapt results to specific geographical locations, domains, and languages.

| Parameter      | Description                                                                                                                                                                                                                                        | Default Value |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `geo_location` | The *Deliver to* location. See our guide to using this parameter [**here**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/features/localization/e-commerce-localization)**.**                                                   | -             |
| `domain`       | Domain localization for Amazon. The full list of available domains can be found [**here**](https://github.com/oxylabs/gitbook-public-english/blob/master/scraping-solutions/web-scraper-api/targets/amazon/broken-reference/README.md).            | `com`         |
| `locale`       | `Accept-Language` header value, which sets the interface language of the Amazon page. [**More info**](https://github.com/oxylabs/gitbook-public-english/blob/master/scraping-solutions/web-scraper-api/targets/amazon/broken-reference/README.md). | -             |

{% hint style="warning" %}
**IMPORTANT:** On most page types, Amazon tailors the returned results based on the delivery location of their customers. Therefore, we advise using the `geo_location` parameter to set your preferred delivery location. You can read more about using `geo_location` with Amazon [**here**](https://github.com/oxylabs/gitbook-public-english/blob/master/scraping-solutions/web-scraper-api/targets/amazon/broken-reference/README.md).
{% endhint %}

## Structured data

Below you can find a **structured output example** for `amazon_sellers`. Please note that right now we only support parsed output for `desktop` device type. However, there is no apparent reason to get sellers pages with any other device type, as seller data is going to be exactly the same across all devices.

<details>

<summary><code>Amazon_sellers</code> <strong>structured output</strong></summary>

```json
{
    "results": [
        {
            "content": {
                "url": "https://www.amazon.com/sp?seller=A151FB8X73UXPJ",
                "query": "A151FB8X73UXPJ",
                "rating": 4.5,
                "page_type": "Seller",
                "description": "Service with a smile! Gamer Girlz LLC loves making our customers happy by providing the quickest service & highest quality products. Every order is packaged with care & includes a special THANK YOU for choosing Gamer Girlz to provide you with the first class shopping experience you deserve!",
                "business_name": "Gamer Girlz",
                "recent_feedback": [
                    {
                        "feedback": "The product never came, and was very very expensive. Wasn't eligible for refund for some reason.",
                        "rated_by": "By Juli on May 8, 2022.",
                        "rating_stars": 1
                    },
                    {
                        "feedback": "Favorite game",
                        "rated_by": "By DF on May 8, 2022.",
                        "rating_stars": 5
                    },
                    {
                        "feedback": "It works perfectly and I love the games on it.",
                        "rated_by": "By John on May 8, 2022.",
                        "rating_stars": 5
                    },
                    {
                        "feedback": "All the games I got came super fast and it amazing condition! Would definitely buy from them again and recommend seller to others!",
                        "rated_by": "By Brianna c. on May 6, 2022.",
                        "rating_stars": 5
                    },
                    {
                        "feedback": "They were fast with shipping and provided quality merchandise. A label of authenticity was included with the game I bought to ensure me that I bought a genuine version.",
                        "rated_by": "By anonymous  on May 6, 2022.",
                        "rating_stars": 5
                    }
                ],
                "business_address": "1020 Michigan St. Sandpoint ID 83864 US",
                "parse_status_code": 12000,
                "feedback_summary_table": {
                    "counts": {
                        "30_days": 44,
                        "90_days": 146,
                        "all_time": 7857,
                        "12_months": 611
                    },
                    "neutral": {
                        "30_days": "5%",
                        "90_days": "2%",
                        "all_time": "2%",
                        "12_months": "1%"
                    },
                    "negative": {
                        "30_days": "7%",
                        "90_days": "7%",
                        "all_time": "3%",
                        "12_months": "8%"
                    },
                    "positive": {
                        "30_days": "89%",
                        "90_days": "91%",
                        "all_time": "95%",
                        "12_months": "91%"
                    }
                }
            },
            "created_at": "2022-05-09 06:57:47",
            "updated_at": "2022-05-09 06:57:50",
            "page": 1,
            "url": "https://www.amazon.com/sp?seller=A151FB8X73UXPJ",
            "job_id": "6929323518437886977",
            "status_code": 200,
            "parser_type": ""
        }
    ]
}
```

</details>

## Output data dictionary

#### HTML example

<figure><img src="https://lh7-us.googleusercontent.com/Inq5Q93noPtfnzwbFnF09dP4mvi6G5D98J3gdVGDwULkj1oVYEFRggMr3ZuR7t9XrpBuG5fZoH3DGSQN4CK8X_IRems3mxSehKzzdSukHjux_3H35RljbZABkGSjJ2meVB2llVJn-Q3KY3iozLuEB0o" alt=""><figcaption></figcaption></figure>

#### JSON structure

The `amazon_sellers` structured output includes fields like `URL`, `query`, `rating`, and others. The table below presents a detailed list of each field we parse, along with its description and data type. The table also includes some metadata.

<table><thead><tr><th width="262">Key</th><th width="341">Description</th><th>Type</th></tr></thead><tbody><tr><td><code>url</code></td><td>The URL of the Amazon seller page.</td><td>string</td></tr><tr><td><code>query</code></td><td>A 13-character seller ID used as the original search term.</td><td>string</td></tr><tr><td><code>rating</code></td><td>The rating of the seller.</td><td>integer</td></tr><tr><td><code>page_type</code></td><td>The type of the Amazon page.</td><td>string</td></tr><tr><td><code>description</code></td><td>A short description about the seller.</td><td>string</td></tr><tr><td><code>seller_name</code></td><td>The name of the seller.</td><td>string</td></tr><tr><td><code>business_name</code></td><td>The name of the business.</td><td>string</td></tr><tr><td><code>recent_feedback</code></td><td>A list of most recent feedback items with its respective details.</td><td>array</td></tr><tr><td><code>business_address</code></td><td>The address of the business.</td><td>string</td></tr><tr><td><code>parse_status_code</code></td><td>The status code of the parsing job. You can see the parser status codes described <a href="https://github.com/oxylabs/gitbook-public-english/blob/master/scraping-solutions/web-scraper-api/targets/amazon/broken-reference/README.md"><strong>here</strong></a>.</td><td>integer</td></tr><tr><td><code>feedback_summary_data</code></td><td>A list of details available regarding the ratings of the seller.</td><td>object</td></tr><tr><td><code>created_at</code></td><td>The timestamp when the scraping job was created.</td><td>timestamp</td></tr><tr><td><code>updated_at</code></td><td>The timestamp when the scraping job was finished.</td><td>timestamp</td></tr><tr><td><code>job_id</code></td><td>The ID of the job associated with the scraping job.</td><td>integer</td></tr><tr><td><code>status_code</code></td><td>The status code of the scraping job. You can see the scraper status codes described <a href="https://github.com/oxylabs/gitbook-public-english/blob/master/scraping-solutions/web-scraper-api/targets/amazon/broken-reference/README.md"><strong>here</strong></a>.</td><td>integer</td></tr><tr><td><code>parser_type</code></td><td>The type of parser used for parsing the data.</td><td>string</td></tr></tbody></table>

{% hint style="info" %}
In the following sections, parsed JSON code snippets are shortened where more than one item for the result type is available.
{% endhint %}

### Recent feedback

The `recent_feedback` data shows recent customer reviews and feedback left for a specific product listing on the Amazon marketplace.

<figure><img src="https://63892162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzrXw45naRpCZ0Ku9AjY1%2Fuploads%2FaDQmpJ6V5sEOQtQL1Sy3%2Famazon_sellers.png?alt=media&#x26;token=672afcf5-78c7-4a41-8729-62853adb0d13" alt=""><figcaption></figcaption></figure>

```json
...
"recent_feedback": [
    {
        "feedback": "We truly appreciate you taking time out of your busy day to leave such a nice review. As a small business we truly like dealing with customers like you who share their positive experience.",
        "rated_by": "By Troy on January 29, 2024.",
        "rating_stars": 5
    },
...
],
...

```

| Key (recent\_feedback) | Description                                                      | Type    |
| ---------------------- | ---------------------------------------------------------------- | ------- |
| `feedback`             | The feedback submitted for the seller or seller’s product.       | string  |
| `rated_by`             | Information on the user who has submitted the feedback and data. | string  |
| `rating_stars`         | The number of stars submitted.                                   | integer |

### Feedback summary data

The `feedback_summary_data` is feedback statistics provided for a particular product listing on the Amazon marketplace. The feedback summary data includes information for different time periods, allowing sellers and analysts to track changes in customer sentiment over time.

<figure><img src="https://lh7-us.googleusercontent.com/0ww8aVbAgN2H8vV8PxPNKB8TWQAPr289gm9P4MfYusweXSwDqyO9EEiEwBtj1OIVuzibxe4obZWqyXWszR41Obxm1ehpAmlbvd-UrZx3Mb32ZAXnHgaYyLjRuLjnBSR9GnvMoyrUg6Pels63BrWKVy0" alt=""><figcaption></figcaption></figure>

```json
...               
 "feedback_summary_data": {
    "1_month": {
        "count": 3,
        "1_star": "33%",
        "2_star": "0%",
        "3_star": "0%",
        "4_star": "33%",
        "5_star": "33%"
    },
    "3_month": {
        "count": 10,
        "1_star": "10%",
        "2_star": "0%",
        "3_star": "0%",
        "4_star": "20%",
        "5_star": "70%"
    },
 ...
}
...
```

<table><thead><tr><th width="229">Key (content.feedback_summary_data)</th><th width="354">Description</th><th>Type</th></tr></thead><tbody><tr><td><code>1_month/3_month/12_month/all_time</code></td><td>A filter to review ratings information per defined timeframe.</td><td>object</td></tr><tr><td><code>1_month/3_month/12_month/all_time.count</code></td><td>The number of reviews available for a certain timeframe.</td><td>integer</td></tr><tr><td><code>1_month-all_time.1_star-5_star</code></td><td>The percentage distribution of rating stars for a certain timeframe.</td><td>percentage</td></tr></tbody></table>
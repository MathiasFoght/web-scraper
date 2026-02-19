# URL

The `amazon` source is designed to retrieve the content from various Amazon URLs. This means that instead of sending multiple parameters, you can provide us with a direct URL to the required Amazon page. We do not strip any parameters or alter your URLs in any other way.

## Request samples

In the code examples below, we make a request to retrieve the Amazon product page for ASIN `B08Y6Z944Q`.

{% tabs %}
{% tab title="cURL" %}

```shell
curl 'https://realtime.oxylabs.io/v1/queries' \
--user 'USERNAME:PASSWORD' \
-H 'Content-Type: application/json' \
-d '{
        "source": "amazon", 
        "url": "https://www.amazon.co.uk/dp/B08Y6Z944Q/",
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
    'source': 'amazon',
    'url': 'https://www.amazon.co.uk/dp/B08Y6Z944Q/',
    'parse': True
}

# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('USERNAME', 'PASSWORD'), #Your credentials go here
    json=payload,
)

# Instead of response with job status and results url, this will return the
# JSON response with results.
pprint(response.json())
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const https = require("https");

const username = "USERNAME";
const password = "PASSWORD";
const body = {
    source: "amazon",
    url: "https://www.amazon.co.uk/dp/B08Y6Z944Q/",
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
https://realtime.oxylabs.io/v1/queries?source=amazon&url=https%3A%2F%2Fwww.amazon.co.uk%2Fdp%2FB08Y6Z944Q%2F&parse=true&access_token=12345abcde
```

{% endtab %}

{% tab title="PHP" %}

```php
<?php

$params = array(
    'source' => 'amazon',
    'url' => 'https://www.amazon.co.uk/dp/B08Y6Z944Q/',
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
		"source": "amazon",
		"url":    "https://www.amazon.co.uk/dp/B08Y6Z944Q/",
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
                source = "amazon",
                url = "https://www.amazon.co.uk/dp/B08Y6Z944Q/",
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
        jsonObject.put("source", "amazon");
        jsonObject.put("url", "https://www.amazon.co.uk/dp/B08Y6Z944Q/");
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
    "source": "amazon", 
    "url": "https://www.amazon.co.uk/dp/B08Y6Z944Q/",
    "parse": true
}
```

{% endtab %}
{% endtabs %}

<details>

<summary>Output example</summary>

```json
{
    "results": [
        {
            "content": {
                "ads": [
                    {
                        "pos": 1,
                        "asin": "B0CH3JJN66",
                        "type": "organic_also_viewed",
                        "price": 375,
                        "title": "Samsung 55 Inch AU7020 UHD HDR 4K Smart TV (2023) - Crystal UHD 4K Smart TV With HDR Picture, Adaptive Sound Lite, PurColour ",
                        "images": [
                            "https://m.media-amazon.com/images/I/71Dxs5msCcL._AC_SS57_.jpg",
                            "https://m.media-amazon.com/images/I/61rH38KyMnL.jpg",
                            "https://m.media-amazon.com/images/I/71xvR9thu1L.jpg"
                        ],
                        "rating": 4.5,
                        "location": "carousel",
                        "price_upper": 375,
                        "reviews_count": 45,
                        "is_prime_eligible": true
                    },
                    {
                        "pos": 2,
                        "asin": "B0BW9RPQPW",
                        "type": "organic_also_viewed",
                        "price": 362,
                        "title": "50 Inch CU7110 UHD HDR Smart TV (2023) - 4K Crystal Processor, Adaptive Sound Audio, PurColour, Built In Gaming TV Hub, Strea",
                        "images": [
                            "https://m.media-amazon.com/images/I/81eKwOlfhTL._AC_SS57_.jpg",
                            "https://m.media-amazon.com/images/I/619tbh+PSSL.jpg",
                            "https://m.media-amazon.com/images/I/81iuMoHZWhL.jpg"
                        ],
                        "rating": 4.5,
                        "location": "carousel",
                        "price_upper": 362,
                        "reviews_count": 45,
                        "is_prime_eligible": true
                    },
                    {...}
                ],
                "url": "https://www.amazon.co.uk/dp/B08Y6Z944Q/",
                "asin": "B08Y6Z944Q",
                "page": 1,
                "brand": "Samsung",
                "price": 0,
                "stock": "",
                "title": "Samsung AU7100 50 Inch (2021) \u00e2\u20ac\u201c Crystal 4K Smart TV With HDR10+ Image Quality, Adaptive Sound, Motion Xcelerator Picture, Samsung Q-Symphony Audio And Gaming Mode - UE50AU7100KXXU",
                "coupon": "",
                "images": [
                    "https://m.media-amazon.com/images/I/71Urp17dnYL._AC_SL1500_.jpg",
                    ...
                    "https://m.media-amazon.com/images/I/51yb9wscZTL._AC_SL1500_.jpg"
                ],
                "rating": 4.5,
                "category": [
                    {
                        "ladder": [
                            {
                                "url": "/tv-bluray-dvd-home-cinema/b/ref=dp_bc_aui_C_1?ie=UTF8&node=560858",
                                "name": "Home Cinema, TV & Video"
                            },
                            {
                                "url": "/LED-Smart-4K-TVs/b/ref=dp_bc_aui_C_2?ie=UTF8&node=560864",
                                "name": "TVs"
                            }
                        ]
                    }
                ],
                "currency": "GBP",
                "delivery": [],
                "_warnings": [
                    "Could not parse pricing count.",
                    "Could not parse price.",
                    "Could not parse description."
                ],
                "page_type": "Product",
                "price_sns": 0,
                "variation": [
                    {
                        "asin": "B08Y7182XL",
                        "selected": false,
                        "dimensions": {
                            "Size Name": "85\""
                        }
                    },
                    {
                        "asin": "B08Y733RV1",
                        "selected": false,
                        "dimensions": {
                            "Size Name": "43\""
                        }
                    },
                    {...}
                ],
                "has_videos": true,
                "sales_rank": [
                    {
                        "rank": 28405,
                        "ladder": [
                            {
                                "url": "/gp/bestsellers/electronics/ref=pd_zg_ts_electronics",
                                "name": "Electronics & Photo"
                            }
                        ]
                    },
                    {
                        "rank": 479,
                        "ladder": [
                            {
                                "url": "/gp/bestsellers/electronics/560864/ref=pd_zg_hrsr_electronics",
                                "name": "TVs"
                            }
                        ]
                    }
                ],
                "top_review": "This is an excellent TV for the price, with an awesome picture, especially on streaming services, which is what we watch most of the time. I read lots of professional reviews online first, all of which rated it very highly, and I wasn't disappointed. There is quite a bit of setting up to do and I did have to tweak some of the settings to get the best picture. At first the picture was too dark, especially on Amazon Prime. It seems this is a particular problem on Prime. I got a much better picture by switching off the \"Brightness Optimisation\". We also didn't like the \"ultra real\" effect you get with 4K LED TVs. Switching to \"Filmmaker Mode\" solved this. Sound quality is OK, but we use a soundbar anyway. I particularly like the two remote controls which come with the TV. There's a traditional remote with lots of buttons: I used this at first to set everything up, including controlling the BluRay player and the soundbar. Once everything was working I switched to the smaller remote which has only the most essential buttons but looks and feels more refined and has a better \"click\" to the buttons than its big brother. Watching terrestrial TV is fine as well, though not as good as streaming services. We're not gamers so I can't comment on its quality there.All in all, a great TV and a bargain.\n  \nRead more",
                "asin_in_url": "B08Y6Z944Q",
                "description": "",
                "parent_asin": "B09DLFS6JN",
                "price_upper": 0,
                "pricing_str": "",
                "pricing_url": "https://www.amazon.co.uk/gp/offer-listing/B08Y6Z944Q?startIndex=0",
                "manufacturer": "Samsung",
                "price_buybox": -1,
                "product_name": "Samsung AU7100 50 Inch (2021) \u00e2\u20ac\u201c Crystal 4K Smart TV With HDR10+ Image Quality, Adaptive Sound, Motion Xcelerator Picture, Samsung Q-Symphony Audio And Gaming Mode - UE50AU7100KXXU",
                "bullet_points": "Home Entertainment Excellence With The AU7100 \u2013 A Smart, Ultra HD TV that delivers it all, the Samsung 50 Inch AU7100 smart tv blends stunning visuals, vibrant colour, crisp audio and striking slim fit design to enhance your living space.\nGet A Powerful Picture With Stunning 4K\u2013 Your 50 Inch Smart TV includes Dynamic Crystal Colour and a Contrast Enhancer, so you can watch all your favourite shows in stunning 4K detail, with colours that pop and contrast that gives a clearer image.\nExperience Audio Perfection with Adaptive Sound on your TV- your Samsung TV adjusts sound in every scene to what\u2019s on screen, so you\u2019ll feel as if you\u2019re part of the action. Q-Symphony allows for a cinema experience when you add a Samsung soundbar.\nUpgrade Your Office Set-up Or Dive Into Gaming With Your Samsung TV \u2013 PC on TV allows you to access your office PC remotely from your Smart TV, so you can do it all, straight from your living room. Our Smart TV also offers an immersive game mode.\nStart Experiencing Samsung TVs - We believe a TV is more than something you watch. It should inspire, amaze, envelop and immerse you. From quality picture, to elegant design, our TVs push the boundaries of what is possible and what a TV can be.",
                "price_initial": 0,
                "pricing_count": 1,
                "reviews_count": 2067,
                "sns_discounts": [],
                "developer_info": [],
                "price_shipping": 0,
                "product_details": {
                    "asin": "B08Y6Z944Q",
                    "batteries": "2 AAA batteries required. (included)",
                    "manufacturer": "Samsung",
                    "item_model_number": "UE50AU7100KXXU",
                    "product_dimensions": "5.99 x 111.68 x 64.42 cm; 11.4 kg",
                    "date_first_available": "2 Mar. 2021"
                },
                "featured_merchant": [],
                "is_prime_eligible": false,
                "parse_status_code": 12005,
                "product_dimensions": "5.99 x 111.68 x 64.42 cm; 11.4 kg",
                "answered_questions_count": 0,
                "rating_stars_distribution": [
                    {
                        "rating": 5,
                        "percentage": 74
                    },
                    {
                        "rating": 4,
                        "percentage": 15
                    },
                    {...}
                ]
            },
            "created_at": "2024-07-01 10:35:28",
            "updated_at": "2024-07-01 10:35:32",
            "page": 1,
            "url": "https://www.amazon.co.uk/dp/B08Y6Z944Q/",
            "job_id": "7213490386797350913",
            "status_code": 200,
            "parser_type": ""
        }
    ]
}
```

</details>

We use synchronous [**Realtime**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods/realtime) integration method in our examples. If you would like to use [**Proxy Endpoint**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods/proxy-endpoint) or asynchronous [**Push-Pull**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods/push-pull) integration, refer to the [**integration methods**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods) section.

## Request parameter values

### Generic

Basic setup and customization options for scraping Google URLs.

<table><thead><tr><th width="222">Parameter</th><th width="350.3333333333333">Description</th><th>Default Value</th></tr></thead><tbody><tr><td><mark style="background-color:green;"><strong>source</strong></mark></td><td>Sets the scraper.</td><td><code>amazon</code></td></tr><tr><td><mark style="background-color:green;"><strong>url</strong></mark></td><td>Direct URL (link) to Amazon page</td><td>-</td></tr><tr><td><code>render</code></td><td>Enables JavaScript rendering when set to <code>html</code>. <a href="../../features/js-rendering-and-browser-control/javascript-rendering"><strong>More info</strong></a><strong>.</strong></td><td>-</td></tr><tr><td><code>parse</code></td><td>Returns parsed data when set to <code>true</code><strong>.</strong> Limited to URLs of specific <a href="../../features/result-processing-and-storage/dedicated-parsers"><strong>Amazon page types</strong></a>.</td><td><code>false</code></td></tr><tr><td><code>callback_url</code></td><td>URL to your callback endpoint. <a href="../../../integration-methods/push-pull#callback"><strong>More info</strong></a>.</td><td>-</td></tr><tr><td><code>user_agent_type</code></td><td>Device type and browser. The full list can be found <a href="../../features/http-context-and-job-management/user-agent-type"><strong>here</strong></a>.</td><td><code>desktop</code></td></tr></tbody></table>

&#x20;   \- mandatory parameter

### Localization

Adapt results to specific geographical locations and languages.

| Parameter      | Description                                                                                                                                                                                                          | Default Value |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `geo_location` | The *Deliver to* location. See our guide to using this parameter [**here**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/features/localization/e-commerce-localization)**.**                     | -             |
| `locale`       | `Accept-Language` header value, which sets the interface language of the Amazon page. [**More info**](https://developers.oxylabs.io/scraping-solutions/features/localization/domain-locale-results-language#locale). | -             |

{% hint style="warning" %}
**IMPORTANT:** On most page types, Amazon tailors the returned results based on the delivery location of their customers. Therefore, we advise using the `geo_location` parameter to set your preferred delivery location. You can read more about using `geo_location` with Amazon [**here**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/features/localization/e-commerce-localization).
{% endhint %}

### Other

Additional advanced settings and controls for specialized requirements.

| Parameter                                             | Description                                                                                                                                                                                                                                                     | Default Value                                                                                                                                                                                                                                                          |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p><code>context</code>:<br><code>currency</code></p> | Sets the currency. Check the available values [**here**](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzrXw45naRpCZ0Ku9AjY1%2Fuploads%2FNNybEQaVnTrc9ymR1NGE%2Fcurrency_new.json?alt=media\&token=a77440f9-50a5-4e07-9993-b2db2144800b). | Depends on the marketplace. Check the default values [**here**](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzrXw45naRpCZ0Ku9AjY1%2Fuploads%2FNNybEQaVnTrc9ymR1NGE%2Fcurrency_new.json?alt=media\&token=a77440f9-50a5-4e07-9993-b2db2144800b). |

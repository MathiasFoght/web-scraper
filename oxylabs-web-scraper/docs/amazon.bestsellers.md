# Best Sellers

The `amazon_bestsellers` data source is designed to retrieve Amazon Best Sellers pages. To see the response example with retrieved data, download this [**sample output**](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiwDdoZGfMbUe5cRL2417%2Fuploads%2Frf2S2YKKlEEhu4cCoW6b%2Famazon_bestsellers.json?alt=media\&token=6b4b3817-5a6e-4095-96b0-81d8d9d0883f) file in HTML format or check structured data output [**here**](#structured-data).

{% hint style="info" %}
Explore output [**data dictionary**](#data-dictionary) for Best Sellers, offering a brief description, screenshot, parsed JSON code snippet, and a table defining each parsed field. Navigate through the details using the right-side navigation or scrolling down the page.
{% endhint %}

## Request samples

In the code examples below, we make a request to retrieve the `2`nd page of Best Sellers in category, which ID is `172541`, on `amazon.com` marketplace.

{% tabs %}
{% tab title="cURL" %}

```bash
curl 'https://realtime.oxylabs.io/v1/queries' \
--user 'USERNAME:PASSWORD' \
-H 'Content-Type: application/json' \
-d '{
        "source": "amazon_bestsellers",
        "domain": "com", 
        "query": "172541", 
        "render": "html",
        "start_page": 2, 
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
    'source': 'amazon_bestsellers',
    'domain': 'com',
    'query': '172541',
    'render': 'html',
    'start_page': 2,
    'parse': True,
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
    source: "amazon_bestsellers",
    domain: "com",
    query: "172541",
    render: "html",
    start_page: 2, 
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
https://realtime.oxylabs.io/v1/queries?source=amazon_bestsellers&domain=com&query=172541&render=html&start_page=2&parse=true&access_token=12345abcde
```

{% endtab %}

{% tab title="PHP" %}

```php
<?php

$params = array(
    'source' => 'amazon_bestsellers',
    'domain' => 'com',
    'query' => '172541',
    'render' => 'html',
    'start_page' => 2, 
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
		"source":     "amazon_bestsellers",
		"domain":     "com",
		"query":      "172541",
		"render":     "html",
		"start_page": 2,
		"parse":      true,
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
                source = "amazon_bestsellers",
                domain = "com",
                query = "172541",
                render = "html",
                start_page = 2,
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
        jsonObject.put("source", "amazon_bestsellers");
        jsonObject.put("domain", "com");
        jsonObject.put("query", "172541");
        jsonObject.put("render", "html");
        jsonObject.put("start_page", 2);
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
    "source": "amazon_bestsellers",
    "domain": "com",
    "query": "172541",
    "render": "html",
    "start_page": 2,
    "parse": true
}
```

{% endtab %}
{% endtabs %}

We use synchronous [**Realtime**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods/realtime) integration method in our examples. If you would like to use [**Proxy Endpoint**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods/proxy-endpoint) or asynchronous [**Push-Pull**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods/push-pull) integration, refer to the [**integration methods**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/integration-methods) section.

## Request parameter values

### Generic

Basic setup and customization options for scraping Amazon Best Sellers pages.

<table><thead><tr><th width="222">Parameter</th><th width="309.3333333333333">Description</th><th>Default Value</th></tr></thead><tbody><tr><td><mark style="background-color:green;"><strong>source</strong></mark></td><td>Sets the scraper.</td><td><code>amazon_bestsellers</code></td></tr><tr><td><mark style="background-color:green;"><strong>query</strong></mark></td><td>Browse node ID.</td><td>-</td></tr><tr><td><mark style="background-color:green;"><strong>render</strong></mark></td><td>Enables JavaScript rendering when set to <code>html</code>. <a href="../../features/js-rendering-and-browser-control/javascript-rendering"><strong>More info</strong></a><strong>.</strong></td><td>-</td></tr><tr><td><code>parse</code></td><td>Returns parsed data when set to <code>true</code>. Explore output <a href="#output-data-dictionary"><strong>data dictionary</strong></a>.</td><td><code>false</code></td></tr><tr><td><code>callback_url</code></td><td>URL to your callback endpoint. <a href="../../../integration-methods/push-pull#callback"><strong>More info</strong></a>.</td><td>-</td></tr><tr><td><code>user_agent_type</code></td><td>Device type and browser. The full list can be found <a href="../../features/http-context-and-job-management/user-agent-type"><strong>here</strong></a>.</td><td><code>desktop</code></td></tr></tbody></table>

&#x20;   \- mandatory parameter

### Localization

Adapt results to specific geographical locations, domains, languages.

| Parameter      | Description                                                                                                                                                                                                                                        | Default Value |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `geo_location` | The *Deliver to* location. See our guide to using this parameter [**here**](https://developers.oxylabs.io/scraping-solutions/web-scraper-api/features/localization/e-commerce-localization)**.**                                                   | -             |
| `domain`       | Domain localization for Amazon. The full list of available domains can be found [**here**](https://github.com/oxylabs/gitbook-public-english/blob/master/scraping-solutions/web-scraper-api/targets/amazon/broken-reference/README.md).            | `com`         |
| `locale`       | `Accept-Language` header value, which sets the interface language of the Amazon page. [**More info**](https://github.com/oxylabs/gitbook-public-english/blob/master/scraping-solutions/web-scraper-api/targets/amazon/broken-reference/README.md). | -             |

{% hint style="warning" %}
**IMPORTANT:** On most page types, Amazon tailors the returned results based on the delivery location of their customers. Therefore, we advise using the `geo_location` parameter to set your preferred delivery location. You can read more about using `geo_location` with Amazon [**here**](https://github.com/oxylabs/gitbook-public-english/blob/master/scraping-solutions/web-scraper-api/targets/amazon/broken-reference/README.md).
{% endhint %}

### Pagination

Controls for managing the pagination and retrieval of search results.

<table><thead><tr><th width="222">Parameter</th><th width="350.3333333333333">Description</th><th width="167">Default Value</th></tr></thead><tbody><tr><td><code>start_page</code></td><td>Starting page number.</td><td><code>1</code></td></tr><tr><td><code>pages</code></td><td>Number of pages to retrieve.</td><td><code>1</code></td></tr></tbody></table>

### Other

Additional advanced settings and controls for specialized requirements.

| Parameter                                             | Description                                                                                                                                                                                                                                                     | Default Value                                                                                                                                                                                                                                                          |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p><code>context</code>:<br><code>currency</code></p> | Sets the currency. Check the available values [**here**](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzrXw45naRpCZ0Ku9AjY1%2Fuploads%2FNNybEQaVnTrc9ymR1NGE%2Fcurrency_new.json?alt=media\&token=a77440f9-50a5-4e07-9993-b2db2144800b). | Depends on the marketplace. Check the default values [**here**](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzrXw45naRpCZ0Ku9AjY1%2Fuploads%2FNNybEQaVnTrc9ymR1NGE%2Fcurrency_new.json?alt=media\&token=a77440f9-50a5-4e07-9993-b2db2144800b). |

#### Code example

```json
{
    "source": "amazon_bestsellers",
    "domain": "com",
    "query": "172541",
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

Below you can find a **structured output example** for `amazon_bestsellers`.

<details>

<summary><code>Amazon_bestsellers</code> <strong>output example</strong></summary>

```json
{
  "results": [
    {
      "content": {
        "url": "https://www.amazon.com/Best-Sellers/zgbs/x/2407760011/?pg=1",
        "page": 1,
        "pages": 2,
        "query": "2407760011",
        "results": [
          {
            "pos": 1,
            "url": "/Hiearcool-Universal-Waterproof-Samsung-Cellphone/dp/B082R2TMRV/ref=zg_bs_2407760011_1/140-4851587-8700940?pd_rd_i=B09KY7BMXF&psc=1",
            "asin": "B082R2TMRV",
            "price": 0,
            "title": "Universal Waterproof Case,Hiearcool Waterproof Phone Pouch Compatible for iPhone 13 12 11 Pro Max XS Max Samsung Galaxy s10 G",
            "rating": 4.6,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 2,
            "url": "/TAURI-iPhone-13-Protector-Protection/dp/B09WJYQY94/ref=zg_bs_2407760011_2/140-4851587-8700940?pd_rd_i=B09PNVCCDF&psc=1",
            "asin": "B09WJYQY94",
            "price": 0,
            "title": "TAURI [3 in 1 Defender Designed for iPhone 13 Pro Max Case 6.7 Inch, with 2 Pack Tempered Glass Screen Protector + 2 Pack Cam",
            "rating": 4.6,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 3,
            "url": "/Mkeke-Compatible-Yellowing-Shockproof-Protective/dp/B09DPG49YB/ref=zg_bs_2407760011_3/140-4851587-8700940?pd_rd_i=B09J3ZVYSX&psc=1",
            "asin": "B09DPG49YB",
            "price": 0,
            "title": "Mkeke Compatible with iPhone 13 Case Black, Not Yellowing Shockproof 13 Phone Black Case with Protective Bumper Slim Fit for ",
            "rating": 4.7,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 4,
            "url": "/CASEKOO-iPhone-13-Pro-Protection/dp/B09WJ1NBHQ/ref=zg_bs_2407760011_4/140-4851587-8700940?pd_rd_i=B09J62TMS5&psc=1",
            "asin": "B09WJ1NBHQ",
            "price": 0,
            "title": "CASEKOO Crystal Clear Designed for iPhone 13 Pro case, [Not Yellowing] [Military Drop Protection] Shockproof Protective Phone",
            "rating": 4.7,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 5,
            "url": "/Spigen-Hybrid-Anti-Yellowing-Technology-Designed/dp/B096J9ZSG1/ref=zg_bs_2407760011_5/140-4851587-8700940?pd_rd_i=B096HLB5WB&psc=1",
            "asin": "B096J9ZSG1",
            "price": 0,
            "title": "Spigen Ultra Hybrid [Anti-Yellowing Technology] Designed for iPhone 13 Pro Max Case (2021) - Crystal Clear",
            "rating": 4.6,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 6,
            "url": "/OtterBox-COMMUTER-Case-iPhone-Plus/dp/B00Z7S33CC/ref=zg_bs_2407760011_6/140-4851587-8700940?pd_rd_i=B08SB2WWM9&psc=1",
            "asin": "B00Z7S33CC",
            "price": 0,
            "title": "OtterBox COMMUTER SERIES Case for iPhone SE (3rd and 2nd gen) and iPhone 8/7 - Retail Packaging - BALLET WAY (PINK SALT/BLUSH",
            "rating": 4.6,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 7,
            "url": "/IMBZBK-Samsung-Galaxy-S22-Ultra/dp/B09NL5BTR8/ref=zg_bs_2407760011_7/140-4851587-8700940?pd_rd_i=B09ZQHPT68&psc=1",
            "asin": "B09NL5BTR8",
            "price": 0,
            "title": "IMBZBK [3+3 Pack] for Samsung Galaxy S22 Ultra 5G Screen Protector [Not Glass], 3 Pack Flexible TPU Film with 3 Pack Tempered",
            "rating": 4.3,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 8,
            "url": "/Cordking-iPhone-11-Shockproof-Anti-Scratch/dp/B091TGTP4S/ref=zg_bs_2407760011_8/140-4851587-8700940?pd_rd_i=B09525CQGL&psc=1",
            "asin": "B091TGTP4S",
            "price": 0,
            "title": "Cordking iPhone 11 Case, Silicone Ultra Slim Shockproof Phone Case with [Soft Anti-Scratch Microfiber Lining], 6.1 inch, Blac",
            "rating": 4.5,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 9,
            "url": "/Cordking-Designed-Shockproof-Anti-Scratch-Microfiber/dp/B08CXZHG4C/ref=zg_bs_2407760011_9/140-4851587-8700940?pd_rd_i=B08MZW4JJ1&psc=1",
            "asin": "B08CXZHG4C",
            "price": 0,
            "title": "Cordking Designed for iPhone 12 Case, Designed for iPhone 12 Pro Case, Silicone Shockproof Phone Case with [Soft Anti-Scratch",
            "rating": 4.5,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 10,
            "url": "/Cordking-iPhone-13-Pro-Anti-Scratch/dp/B09BP2C3G2/ref=zg_bs_2407760011_10/140-4851587-8700940?pd_rd_i=B09FZNRCFY&psc=1",
            "asin": "B09BP2C3G2",
            "price": 0,
            "title": "Cordking Designed for iPhone 13 Pro Case, Silicone Ultra Slim Shockproof Protective Phone Case with [Soft Anti-Scratch Microf",
            "rating": 4.5,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 11,
            "url": "/OtterBox-Commuter-Case-iPhone-Pro/dp/B08DY7D8WZ/ref=zg_bs_2407760011_11/140-4851587-8700940?pd_rd_i=B093721WFT&psc=1",
            "asin": "B08DY7D8WZ",
            "price": 0,
            "title": "OTTERBOX COMMUTER SERIES Case for iPhone 12 & iPhone 12 Pro - BESPOKE WAY (BLAZER BLUE/STORMY SEAS BLUE)",
            "rating": 4.7,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 12,
            "url": "/Mkeke-Compatible-iPhone-Clear-Inch-Black/dp/B081G9JCQ1/ref=zg_bs_2407760011_12/140-4851587-8700940?pd_rd_i=B08HN8SQL1&psc=1",
            "asin": "B081G9JCQ1",
            "price": 0,
            "title": "Mkeke Compatible with iPhone 11 Case, Clear Shock Absorption Cases for 6.1 Inch Black",
            "rating": 4.7,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 13,
            "url": "/OTTERBOX-COMMUTER-Case-iPhone-Pro/dp/B09D55YMC1/ref=zg_bs_2407760011_13/140-4851587-8700940?pd_rd_i=B09NCXVBYH&psc=1",
            "asin": "B09D55YMC1",
            "price": 0,
            "title": "OTTERBOX COMMUTER SERIES Case for iPhone 13 Pro Max & iPhone 12 Pro Max - BLACK",
            "rating": 4.6,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 14,
            "url": "/Elando-Compatible-Non-Yellowing-Shockproof-Protective/dp/B08RNNJN4P/ref=zg_bs_2407760011_14/140-4851587-8700940?pd_rd_i=B09S3R1WSZ&psc=1",
            "asin": "B08RNNJN4P",
            "price": 0,
            "title": "Elando Crystal Clear Case Compatible with iPhone 12/12 Pro, Non-Yellowing Shockproof Protective Phone Case Slim Thin, 6.1 inc",
            "rating": 4.7,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 15,
            "url": "/OTTERBOX-COMMUTER-Case-iPhone-ONLY/dp/B09D51Z5TR/ref=zg_bs_2407760011_15/140-4851587-8700940?pd_rd_i=B09NCWDKKR&psc=1",
            "asin": "B09D51Z5TR",
            "price": 0,
            "title": "OTTERBOX COMMUTER SERIES Case for iPhone 13 (ONLY) - BLACK",
            "rating": 4.7,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 16,
            "url": "/OTTERBOX-SYMMETRY-CLEAR-Case-iPhone/dp/B09D5DCTRH/ref=zg_bs_2407760011_16/140-4851587-8700940?pd_rd_i=B09SF5MR3V&psc=1",
            "asin": "B09D5DCTRH",
            "price": 0,
            "title": "OTTERBOX SYMMETRY CLEAR SERIES Case for iPhone 13 (ONLY) - CLEAR",
            "rating": 4.7,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 17,
            "url": "/Cordking-13-Shockproof-Protective-Anti-Scratch/dp/B09BPSXHN6/ref=zg_bs_2407760011_17/140-4851587-8700940?pd_rd_i=B09FZLH56R&psc=1",
            "asin": "B09BPSXHN6",
            "price": 0,
            "title": "Cordking Designed for iPhone 13 Pro Max Case, Silicone Ultra Slim Shockproof Protective Phone Case with [Soft Anti-Scratch Mi",
            "rating": 4.6,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 18,
            "url": "/TAURI-iPhone-13-Protection-Shockproof/dp/B09C5R18QW/ref=zg_bs_2407760011_18/140-4851587-8700940?pd_rd_i=B09FYSSN53&psc=1",
            "asin": "B09C5R18QW",
            "price": 0,
            "title": "TAURI [3 in 1] Defender Designed for iPhone 13 Case 6.1 Inch, with 2 Pack Tempered Glass Screen Protector + 2 Pack Camera Len",
            "rating": 4.6,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 19,
            "url": "/COOLQO-Compatible-Protector-Shockproof-Protective/dp/B082HQRL1P/ref=zg_bs_2407760011_19/140-4851587-8700940?pd_rd_i=B082HQ38SF&psc=1",
            "asin": "B082HQRL1P",
            "price": 0,
            "title": "COOLQO Compatible for iPhone 11 Case, with [2 x Tempered Glass Screen Protector] Clear 360 Full Body Coverage Hard PC+Soft Si",
            "rating": 4.5,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 20,
            "url": "/SPIDERCASE-Designed-Yellowing-Military-Protection/dp/B09WXVT9R2/ref=zg_bs_2407760011_20/140-4851587-8700940?pd_rd_i=B09XZV8VN8&psc=1",
            "asin": "B09WXVT9R2",
            "price": 0,
            "title": "SPIDERCASE Designed for iPhone 13 Pro Max Case, [Crystal Clear] [Not Yellowing Military Grade Drop Protection] Slim Thin Clea",
            "rating": 4.6,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 21,
            "url": "/OTOFLY-Protection-Anti-Scratch-Shockproof-Compatible/dp/B07XQHDDVQ/ref=zg_bs_2407760011_21/140-4851587-8700940?pd_rd_i=B07XQP2LG9&psc=1",
            "asin": "B07XQHDDVQ",
            "price": 0,
            "title": "OTOFLY iPhone 11 Case,Ultra Slim Fit iPhone Case Liquid Silicone Gel Cover with Full Body Protection Anti-Scratch Shockproof ",
            "rating": 4.5,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 22,
            "url": "/OTTERBOX-SYMMETRY-CLEAR-Case-iPhone/dp/B09D5FPZZW/ref=zg_bs_2407760011_22/140-4851587-8700940?pd_rd_i=B09XJWVF43&psc=1",
            "asin": "B09D5FPZZW",
            "price": 0,
            "title": "OTTERBOX SYMMETRY CLEAR SERIES Case for iPhone 13 Pro (ONLY) - CLEAR",
            "rating": 4.6,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 23,
            "url": "/Cordking-iPhone-13-Shockproof-Anti-Scratch/dp/B09BP234TP/ref=zg_bs_2407760011_23/140-4851587-8700940?pd_rd_i=B09J3Z6S39&psc=1",
            "asin": "B09BP234TP",
            "price": 0,
            "title": "Cordking Designed for iPhone 13 Case, Silicone Ultra Slim Shockproof Protective Phone Case with [Soft Anti-Scratch Microfiber",
            "rating": 4.6,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 24,
            "url": "/JOTO-Universal-Waterproof-Cellphone-Underwater/dp/B07V8HGM7T/ref=zg_bs_2407760011_24/140-4851587-8700940?pd_rd_i=B07WK1ZG9C&psc=1",
            "asin": "B07V8HGM7T",
            "price": 0,
            "title": "JOTO Waterproof Case Universal Phone Holder Pouch, Underwater Cellphone Dry Bag Compatible with iPhone 13 Pro 12 11 Pro Max X",
            "rating": 4.5,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 25,
            "url": "/OTOFLY-Compatible-Silicone-Full-Body-Protective/dp/B08H5T9KM4/ref=zg_bs_2407760011_25/140-4851587-8700940?pd_rd_i=B08H5W88G7&psc=1",
            "asin": "B08H5T9KM4",
            "price": 0,
            "title": "OTOFLY Compatible with iPhone 12 Case and iPhone 12 Pro Case 6.1 inch(2020),[Silky and Soft Touch Series] Premium Soft Liquid",
            "rating": 4.5,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 26,
            "url": "/AEDILYS-Shockproof-iPhone-pro-Case/dp/B09ZTYW5JP/ref=zg_bs_2407760011_26/140-4851587-8700940?pd_rd_i=B09ZTYW5JP&psc=1",
            "asin": "B09ZTYW5JP",
            "price": 0,
            "title": "AEDILYS Shockproof for iPhone 13 pro Case",
            "rating": 0,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 27,
            "url": "/OTTERBOX-COMMUTER-Case-iPhone-ONLY/dp/B09D5PFMDR/ref=zg_bs_2407760011_27/140-4851587-8700940?pd_rd_i=B09NCYK6P4&psc=1",
            "asin": "B09D5PFMDR",
            "price": 0,
            "title": "OTTERBOX COMMUTER SERIES Case for iPhone 13 Pro (ONLY) - BLACK",
            "rating": 4.7,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 28,
            "url": "/Cordking-iPhone-Silicone-Shockproof-Microfiber/dp/B08QFB7N8P/ref=zg_bs_2407760011_28/140-4851587-8700940?pd_rd_i=B08X7L75L8&psc=1",
            "asin": "B08QFB7N8P",
            "price": 0,
            "title": "Cordking iPhone SE Case 2022/2020, iPhone 7 8 Case, Silicone Ultra Slim Shockproof Phone Case with [Soft Microfiber Lining], ",
            "rating": 4.6,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 29,
            "url": "/OTOFLY-Silicone-Full-Body-Protective-Compatible/dp/B07QG5HY9M/ref=zg_bs_2407760011_29/140-4851587-8700940?pd_rd_i=B07QKSYGY4&psc=1",
            "asin": "B07QG5HY9M",
            "price": 0,
            "title": "OTOFLY Compatible with iPhone XR Case,[Silky and Soft Touch Series] Premium Soft Liquid Silicone Rubber Full-Body Protective ",
            "rating": 4.5,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 30,
            "url": "/SPIDERCASE-Waterproof-Protection-Shockproof-Anti-Scratched/dp/B09N3JLG44/ref=zg_bs_2407760011_30/140-4851587-8700940?pd_rd_i=B09XQZBZDL&psc=1",
            "asin": "B09N3JLG44",
            "price": 0,
            "title": "SPIDERCASE for Samsung Galaxy S22 Ultra Case, Waterproof Built-in Screen Protector Full Protection Heavy Duty Shockproof Anti",
            "rating": 4.4,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 31,
            "url": "/JOTO-Universal-Waterproof-Cellphone-Samsung/dp/B00LBK7OSY/ref=zg_bs_2407760011_31/140-4851587-8700940?pd_rd_i=B01ITNRGFG&psc=1",
            "asin": "B00LBK7OSY",
            "price": 0,
            "title": "JOTO Universal Waterproof Phone Pouch Cellphone Dry Bag Case Compatible with iPhone 13 12 11 Pro Max Mini Xs XR X 8 7 6S Plus",
            "rating": 4.5,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 32,
            "url": "/OtterBox-SYMMETRY-Antimicrobial-MagSafe-iPhone/dp/B09LPFQ8LY/ref=zg_bs_2407760011_32/140-4851587-8700940?pd_rd_i=B09MX2XN43&psc=1",
            "asin": "B09LPFQ8LY",
            "price": 0,
            "title": "OtterBox SYMMETRY SERIES+ Antimicrobial Case with MagSafe for iPhone 12/13 Pro Max - Black",
            "rating": 4.4,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 33,
            "url": "/OTTERBOX-SYMMETRY-DISNEYS-50th-iPhone/dp/B09JYLQPGD/ref=zg_bs_2407760011_33/140-4851587-8700940?pd_rd_i=B09NCX976Y&psc=1",
            "asin": "B09JYLQPGD",
            "price": 0,
            "title": "OTTERBOX SYMMETRY SERIES DISNEY'S 50th Case for iPhone 13 Pro Max & iPhone 12 Pro Max - 50th BADGE",
            "rating": 4.8,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 34,
            "url": "/OtterBox-DEFENDER-SCREENLESS-Case-iPhone/dp/B07V1PC86V/ref=zg_bs_2407760011_34/140-4851587-8700940?pd_rd_i=B09SF7C7V8&psc=1",
            "asin": "B07V1PC86V",
            "price": 0,
            "title": "OTTERBOX DEFENDER SERIES SCREENLESS EDITION Case for iPhone 11 - BLACK",
            "rating": 4.7,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 35,
            "url": "/TORRAS-Shockproof-Compatible-Military-Grade-Translucent/dp/B0946Y2ZM6/ref=zg_bs_2407760011_35/140-4851587-8700940?pd_rd_i=B09VZ9VGHJ&psc=1",
            "asin": "B0946Y2ZM6",
            "price": 0,
            "title": "TORRAS Shockproof Compatible for iPhone 13 Pro Case, [Military-Grade Drop Tested] Translucent Matte Hard PC Back with Soft Si",
            "rating": 4.6,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 36,
            "url": "/OtterBox-COMMUTER-Case-iPhone-11/dp/B07W45LYY8/ref=zg_bs_2407760011_36/140-4851587-8700940?pd_rd_i=B07W45LYY8&psc=1",
            "asin": "B07W45LYY8",
            "price": 0,
            "title": "OTTERBOX COMMUTER SERIES Case for iPhone 11 - BLACK",
            "rating": 4.8,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 37,
            "url": "/TAURI-iPhone-13-Pro-Protection/dp/B09C5S9DMM/ref=zg_bs_2407760011_37/140-4851587-8700940?pd_rd_i=B09GYVWBVK&psc=1",
            "asin": "B09C5S9DMM",
            "price": 0,
            "title": "TAURI [3 in 1] Defender Designed for iPhone 13 Pro Case 6.1 Inch, with 2 Pack Tempered Glass Screen Protector + 2 Pack Camera",
            "rating": 4.5,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          },
          {
            "pos": 38,
            "url": "/Cordking-iPhone-11-Anti-Scratch-Microfiber/dp/B09NGMBLNL/ref=zg_bs_2407760011_38/140-4851587-8700940?pd_rd_i=B09QNKR7GM&psc=1",
            "asin": "B09NGMBLNL",
            "price": 0,
            "title": "Cordking iPhone 11 Case, Silicone [Square Edges] & [Camera Protecion] Upgraded Phone Case with Soft Anti-Scratch Microfiber L",
            "rating": 4.8,
            "currency": "USD",
            "is_prime": false,
            "price_str": "",
            "price_upper": 0,
            "ratings_count": 0
          }
        ],
        "parse_status_code": 12000
      },
      "created_at": "2022-05-10 11:25:45",
      "updated_at": "2022-05-10 11:26:34",
      "page": 1,
      "url": "https://www.amazon.com/Best-Sellers/zgbs/x/2407760011/?pg=1",
      "job_id": "6929753341157204993",
      "status_code": 200,
      "parser_type": ""
    }
  ]
```

</details>

## Data dictionary

#### HTML example

<figure><img src="https://63892162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzrXw45naRpCZ0Ku9AjY1%2Fuploads%2FMAR4idgOy55p08D7vy5k%2Famazon_best_sellers.png?alt=media&#x26;token=7e6117ad-066f-4725-aef9-3165b21387cb" alt=""><figcaption></figcaption></figure>

#### JSON structure

The `amazon_bestsellers` provides comprehensive data on the best-selling products on Amazon. The table below presents a detailed list of each field we parse, along with its description and data type. The table also includes some metadata.

<table><thead><tr><th width="239">Key</th><th width="364">Description</th><th>Type</th></tr></thead><tbody><tr><td><code>url</code></td><td>The URL of the Amazon Best Sellers page.</td><td>string</td></tr><tr><td><code>page</code></td><td>The current page number.</td><td>integer</td></tr><tr><td><code>pages</code></td><td>The total number of pages.</td><td>integer</td></tr><tr><td><code>query</code></td><td>The original search term.</td><td>string</td></tr><tr><td><code>results</code></td><td>A dictionary containing the results of the search.</td><td>object</td></tr><tr><td><code>results.pos</code></td><td>An indicator denoting the position of a bestselling item.</td><td>integer</td></tr><tr><td><code>results.url</code></td><td>The URL of the best selling item.</td><td>string</td></tr><tr><td><code>results.asin</code></td><td>Amazon Standard Identification Number.</td><td>string</td></tr><tr><td><code>results.price</code></td><td>The price of the product.</td><td>string</td></tr><tr><td><code>results.title</code></td><td>The title of the product.</td><td>string</td></tr><tr><td><code>results.rating</code></td><td>The rating of the product.</td><td>float</td></tr><tr><td><code>results.currency</code></td><td>The currency in which the price is denominated.</td><td>string</td></tr><tr><td><code>results.is_prime</code></td><td>Indicates whether the product is eligible for Amazon Prime.</td><td>boolean</td></tr><tr><td><code>results.price_str</code></td><td>The original price before any discounts or promotions</td><td>float</td></tr><tr><td><code>results.price_upper</code></td><td>The upper limit of the price if applicable.</td><td>float</td></tr><tr><td><code>results_ratings_count</code></td><td>The total number of ratings given to the product.</td><td>integer</td></tr><tr><td><code>parse_status_code</code></td><td>The status code of the parsing job. You can see the parser status codes described <a href="https://github.com/oxylabs/gitbook-public-english/blob/master/scraping-solutions/web-scraper-api/targets/amazon/broken-reference/README.md"><strong>here</strong></a>.</td><td>integer</td></tr><tr><td><code>created_at</code></td><td>The timestamp when the scraping job was created.</td><td>timestamp</td></tr><tr><td><code>updated_at</code></td><td>The timestamp when the scraping job was finished.</td><td>timestamp</td></tr><tr><td><code>job_id</code></td><td>The ID of the job associated with the scraping job.</td><td>string</td></tr><tr><td><code>status_code</code></td><td>The status code of the scraping job. You can see the scraper status codes described <a href="https://github.com/oxylabs/gitbook-public-english/blob/master/scraping-solutions/web-scraper-api/targets/amazon/broken-reference/README.md"><strong>here</strong></a>.</td><td>integer</td></tr><tr><td><code>parser_type</code></td><td>The type of parser used for parsing the data.</td><td>string</td></tr></tbody></table>
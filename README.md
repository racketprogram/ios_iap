---
title: Flask 应用程序 API v1.0.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="flask-api">Flask 应用程序 API v1.0.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

这是一个用于验证 iOS 应用内购买并处理 Apple 通知的 API 文档。

Base URLs:

* <a href="http://{host}:{port}">http://{host}:{port}</a>

    * **host** -  Default: localhost

    * **port** -  Default: 5000

<h1 id="flask-api-default">Default</h1>

## post__verify_purchase

> Code samples

```shell
# You can also use wget
curl -X POST http://{host}:{port}/verify_purchase \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST http://{host}:{port}/verify_purchase HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "receipt": "receipt_data",
  "user_id": "user_123"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('http://{host}:{port}/verify_purchase',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post 'http://{host}:{port}/verify_purchase',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://{host}:{port}/verify_purchase', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','http://{host}:{port}/verify_purchase', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://{host}:{port}/verify_purchase");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://{host}:{port}/verify_purchase", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /verify_purchase`

*验证 iOS 应用内购买收据并记录用户订阅信息*

> Body parameter

```json
{
  "receipt": "receipt_data",
  "user_id": "user_123"
}
```

<h3 id="post__verify_purchase-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» receipt|body|string|false|iOS 应用内购买的收据数据|
|» user_id|body|string|false|用户的唯一标识符|

> Example responses

> 200 Response

```json
{
  "success": true,
  "data": {
    "product_id": "com.example.product1",
    "purchase_date": "2023-01-01T00:00:00",
    "expiry_date": "2024-01-01T00:00:00"
  }
}
```

<h3 id="post__verify_purchase-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功响应|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|请求错误|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器错误|Inline|

<h3 id="post__verify_purchase-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» success|boolean|false|none|none|
|» data|object|false|none|none|
|»» product_id|string|false|none|none|
|»» purchase_date|string(date-time)|false|none|none|
|»» expiry_date|string(date-time)|false|none|none|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» error|string|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» error|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post__apple_notifications

> Code samples

```shell
# You can also use wget
curl -X POST http://{host}:{port}/apple_notifications \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST http://{host}:{port}/apple_notifications HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "notification_type": "INITIAL_BUY",
  "user_id": "user_123",
  "product_id": "com.example.product1",
  "purchase_date": "2023-01-01T00:00:00",
  "expiry_date": "2024-01-01T00:00:00"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('http://{host}:{port}/apple_notifications',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post 'http://{host}:{port}/apple_notifications',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://{host}:{port}/apple_notifications', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','http://{host}:{port}/apple_notifications', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://{host}:{port}/apple_notifications");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://{host}:{port}/apple_notifications", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /apple_notifications`

*处理 Apple 的通知*

> Body parameter

```json
{
  "notification_type": "INITIAL_BUY",
  "user_id": "user_123",
  "product_id": "com.example.product1",
  "purchase_date": "2023-01-01T00:00:00",
  "expiry_date": "2024-01-01T00:00:00"
}
```

<h3 id="post__apple_notifications-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» notification_type|body|string|false|通知类型|
|» user_id|body|string|false|用户的唯一标识符|
|» product_id|body|string|false|购买的产品 ID|
|» purchase_date|body|string(date-time)|false|购买日期和时间|
|» expiry_date|body|string(date-time)|false|订阅到期日期和时间|

> Example responses

> 200 Response

```json
{
  "success": true
}
```

<h3 id="post__apple_notifications-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功响应|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|请求错误|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|服务器错误|Inline|

<h3 id="post__apple_notifications-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» success|boolean|false|none|none|

Status Code **400**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» error|string|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» error|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_Subscription">Subscription</h2>
<!-- backwards compatibility -->
<a id="schemasubscription"></a>
<a id="schema_Subscription"></a>
<a id="tocSsubscription"></a>
<a id="tocssubscription"></a>

```json
{
  "id": 1,
  "user_id": "user_123",
  "product_id": "com.example.product1",
  "purchase_date": "2023-01-01T00:00:00",
  "expiry_date": "2024-01-01T00:00:00",
  "status": "active"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|none|none|
|user_id|string|false|none|none|
|product_id|string|false|none|none|
|purchase_date|string(date-time)|false|none|none|
|expiry_date|string(date-time)|false|none|none|
|status|string|false|none|none|


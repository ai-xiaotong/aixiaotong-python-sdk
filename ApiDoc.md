# 公共请求参数

公共请求参数用于标识用户、区分独立调用和鉴权，统一放在HTTP请求Header中，
在每个接口单独的接口文档中不再赘述，但每次请求均需携带。

## 签名方法

接口鉴权采用HMAC-SHA1签名方法。

| 参数名称  | 类型 | 必选 | 描述 |
|  ----  | ----  | ----  | ----  |
| Authorization  | String | 是 | HTTP 标准身份认证头部字段，格式为`<签名方法>:<访问ID>:<签名值>`，其中，签名方法为`AXT-HMAC-SHA1`，POST请求时签名值为base64(hmacSHA1(akSecret, METHOD + "\n" + base64(Content-MD5) + "\n" + Content-Type + "\n" + Date))，例如：`AXT-HMAC-SHA1 dHJpYWw=:LlEoE03Sr3a7KruOskGtDYrCPKg=`。 |
| Date | String | 是 | 当前GMT时间，格式为`EEE, dd MMM yyyy HH:mm:ss 'GMT'`，例如Mon, 02 Dec 2019 08:28:18 GMT。**如果与服务器时间相差超过1分钟，会导致签名过期错误。** |
| Content-Type | String | 否 | 请求内容的类型，例如`application/json; charset=utf-8`，允许为为空。 |
| Content-MD5 | String | 否 | 请求内容数据的MD5值，对消息内容（不包括头部）计算MD5值，再进行base64编码。该请求头用于消息完整性校验，例如`XUFAKrxLKna5cZ2REBfFkg==`，允许为空。 |
| Content-Length | String | 否 | 请求内容数据长度，十进制表示字节数 |

# 公共响应参数

公共响应参数返回统一错误信息。

| 参数名称  | 类型 | 描述 |
|  ----  | ----  | ----  |
| code  | Integer | 错误码，例如，20000 |
| message | String | 错误提示，例如，ok |

## 公共错误码

| 错误码  | 描述 |
|  ----  | ----  |
| 20000  | SUCCESS，成功 |
| 40000 | PARAM_ERROR，参数错误 |
| 40001 | IMAGE_ERROR，照片格式不支持 |
| 40002 | FREQ_LIMIT，频繁调用 |
| 40100 | UNAUTHORIZED，鉴权失败 |
| 40301 | INACTIVE，服务未开通 |
| 40302 | INSUFFICIENT_BALANCE，账户余量不足 |
| 40020 | NO_FACE，未检测到人脸 |
| 41300 | ENTITY_TOO_LARGE，实体太大 |
| 50000 | INTERNAL_ERROR，服务异常 |
| 50101 | NOT_SUPPORT，不支持 |
| 50006 | SYSTEM_BUSY，系统繁忙 |

# Face

## FaceCompare

比对两张照片中最大的脸，返回相似度得分。

### 请求语法

```
POST /face/compare HTTP/1.1
Host: api.ai-xiaotong.com
Content-Type: application/json; charset=utf-8
Authorization: signature
Date: Mon, 02 Dec 2019 08:28:18 GMT
{
  "requestId": UUID,
  "imageA": base64(imageA),
  "imageB": base64(imageB)
}
```

### 请求参数

| 参数名称  | 类型 | 必选 | 描述 |
|  ----  | ----  | ----  | ----  |
| requestId  | String | 是 | 本次调用唯一标识 |
| imageA | String | 是 | 待比对照片，照片文件Base64编码，格式为`EEE, dd MMM yyyy HH:mm:ss 'GMT'`，例如Mon, 02 Dec 2019 08:28:18 GMT。**如果与服务器时间相差超过5分钟，会导致签名过期错误。** |
| imageB | String | 否 | 待比对照片，照片文件Base64编码，例如`application/json; charset=utf-8`，允许为为空。 |

### 响应参数

| 参数名称  | 类型 | 描述 |
|  ----  | ---- | ----  |
| score  | Double | 相似度得分，0-100，越大则比对的人脸越相似，千分之一误识别率时score为50，万分一误识别率时为60 |

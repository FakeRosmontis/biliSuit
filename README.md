# Attention
**由于未知原因，暂时无法解决 69949/261XX 类型的错误**

**This code is like shit, please don't try to understand it.**

**Use this project will probably ruslt in your account is banned.**  

**IOS is not supported.**

# Usage
### python 3.10
Edit `config.json` to input your account info.  

Then run `python main.py` to start purchase.

### config.json
```
{
  "accessKey": "",
  "android_api_level": 30,
  "app_build": "",
  "appVer": "",
  "chrome_version": "",
  "coupon_token": "",
  "device": "",
  "devicefingerprint": "",
  "fp_local": "",
  "fp_remove": "",
  "item_id": "",
  "log_level": "",
  "osVer": "",
  "pay_appVer": "",
  "phone": "",
  "sdkVersion": "",
  "session_id": "",
  "time_before": 0,
  "x-bili-aurora-eid": "",
  "cookies": ""
}
```

### Details
|        key        |        value        |                                                 description                                                 |             url             |
|:-----------------:|:-------------------:|:-----------------------------------------------------------------------------------------------------------:|:---------------------------:|
|     accessKey     |     [accessKey]     |                                      Can be found in bili wallet page.                                      | `https://pay.bilibili.com/` |
| android_api_level |      [sdkInt]       | Can be found in `User-Agent`<br/>Also can use **_AIDA64_** to check it.<br/>Android: `ro.build.version.sdk` | `https://api.bilibili.com/` |
|     app_build     |     [app_build]     |           Android build id.<br/>Also can use **_AIDA64_** to check it.<br/>Android: `ro.build.id`           | `https://api.bilibili.com/` |
|      appVer       |       6610300       |                         Bilibili APP version.<br/>Can be found in bili wallet page.                         | `https://pay.bilibili.com/` |
|  chrome_version   |  [chrome_version]   |           Android version, can be found in `User-Agent`.<br/>Seems different in different phones.           | `https://api.bilibili.com/` |
|   coupon_token    |                     |                                      Token of coupon, default `None`.                                       |                             |
|      device       |       android       |                                        Android and must be Android !                                        |                             |
| devicefingerprint | [devicefingerprint] |         Android device finger .<br/>Can be found in bili wallet page.<br/>`None` for auto generate.         | `https://pay.bilibili.com/` |
|     fp_local      |     [fp_local]      |                       Can be found in bili wallet page.<br/>`None` for auto generate.                       | `https://pay.bilibili.com/` |
|     fp_remove     |     [fp_remove]     |                       Can be found in bili wallet page.<br/>`None` for auto generate.                       | `https://pay.bilibili.com/` |
|      item_id      |      [item_id]      |                               Bili suit items id, can be found in share link.                               | `https://api.bilibili.com/` |
|     log_level     |    [info, debug]    |                       `info`: print simple info. <br/>`debug`:  print response data.                        |                             |
|       osVer       |       [osVer]       |           Android Version. Can be found in `User-Agent`.<br/>Android: `ro.build.version.release`            | `https://api.bilibili.com/` |
|    pay_appVer     |       6.61.0        |                                   You know, can be found in `User-Agent`.                                   | `https://api.bilibili.com/` |
|       phone       |       [phone]       |                       Your Mobile phone Model.<br/>Can be found in android settings.                        |                             |
|    sdkVersion     |        1.4.5        |                                      Can be found in bili wallet page.                                      | `https://pay.bilibili.com/` |
|    session_id     |    [session_id]     |        Can be found in bili wallet page.<br/>`None` for auto generate.<br/>Recommend to use `None`.         | `https://pay.bilibili.com/` |
|    time_before    |      [0 ~ 999]      |                          Time to buy in advance, unit: `ms`.<br/>Maximum `999` ms.                          |                             |
|x-bili-aurora-eid|[x-bili-aurora-eid]|Can be found in headers.||
|      cookies      |      [cookies]      |                                       Can be found in mostly headers.                                       | `https://api.bilibili.com/` |

### cookies
You can capture cookies in mostly requests.
```
SESSDATA=; bili_jct=; DedeUserID=; DedeUserID__ckMd5=; sid=; Buvid=
```

## Example config
```
{
  "accessKey": "XXX",
  "android_api_level": 30,
  "app_build": "QWERT",
  "appVer": "6600300",
  "coupon_token": "",
  "chrome_version": "99.0.3325.110",
  "device": "android",
  "devicefingerprint": "XXX",
  "fp_local": "XXX",
  "fp_remove": "XXX",
  "item_id": "114514",
  "log_level": "debug",
  "osVer": "12.0.1",
  "pay_appVer": "6.61.0",
  "phone": "S22",
  "sdkVersion": "1.4.9",
  "session_id": "",
  "time_before": 810,
  "x-bili-aurora-eid": "XXX==",
  "cookies": "SESSDATA=XXX; bili_jct=XXX; DedeUserID=1; DedeUserID__ckMd5=XXX; sid=XXX; Buvid=XXX"
}
```

## Traffic capture
Bilibili APP has enabled SSL pinning.  
So phone must be root.  
Need to use Virtual Xposed to install APP, then use Fiddler to capture HTTPS package.

## Some useful API
1. [Check your phone info.](https://api.bilibili.com/client_info) &nbsp; (Only a part of User-Agent.)
</br>**Open this url in APP !!!**</br>
Example: `https://api.bilibili.com/client_info` </br></br>
2. [Bilibili app info.(Android)](https://app.bilibili.com/x/v2/version?mobi_app=android) </br>
Example: `https://app.bilibili.com/x/v2/version?mobi_app=android` </br></br>
3. [Check to see if coupons are available .](https://api.bilibili.com/x/garb/coupon/usable?item_id=32296) </br>
Example: `https://api.bilibili.com/x/garb/coupon/usable?item_id={item_id}` </br></br>
4. [Latest 30 buyers and fans id.](https://api.bilibili.com/x/garb/rank/fan/recent?item_id=32296) </br>
Example: `https://api.bilibili.com/x/garb/rank/fan/recent?item_id={item_id}` </br>

# Feature
1. Multiply purchase.
2. Sacn and return the fastest CDN IP.  
3. Lock number.

# Author
[**超急玛丽**](https://space.bilibili.com/24924450)  
[**恋利普贝当**](https://space.bilibili.com/2932835)

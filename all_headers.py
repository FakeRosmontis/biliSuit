import random
import uuid

import all_url
import tools

android_api_level = tools.get_value("android_api_level")
appVer = tools.get_value("appVer")
app_build = tools.get_value("app_build")
chrome_version = tools.get_value("chrome_version")
devicefingerprint = tools.get_value("devicefingerprint")
device = tools.get_value("device")
fp_local = tools.get_value("fp_local")
fp_remove = tools.get_value("fp_remove")
item_id = tools.get_value("item_id")
osVer = tools.get_value("osVer")
pay_appVer = tools.get_value("pay_appVer")
phone = tools.get_value("phone")
session_id = tools.get_value("session_id")
x_bili_aurora_eid = tools.get_value("x-bili-aurora-eid")

Buvid = tools.cookies_value("Buvid")
csrf = tools.cookies_value("bili_jct")

if app_build == "":
    app_build = "".join([random.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ") for i in range(64)])

if fp_local == "":
    fp_local = "".join([random.choice("0123456789abcdef") for i in range(64)])

if fp_remove == "":
    fp_remove = "".join([random.choice("0123456789abcdef") for i in range(64)])

if session_id == "":
    session_id = "".join([random.choice("0123456789abcdef") for i in range(8)])  # 尝试混入其中

if devicefingerprint == "":
    deviceFingerprint = "".join(str(uuid.uuid4()).split("-"))

item_url = "https://www.bilibili.com/h5/mall/suit/detail?id={item_id}&navhide=1".format(item_id=item_id)

app_User_Agent = "Mozilla/5.0 (Linux; Android {osVer}; {phone} Build/{app_build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "Version/4.0 Chrome/{chrome} Mobile Safari/537.36 os/android model/{phone} build/{appVer} " \
                 "osVer/{osVer} sdkInt/{s} network/2 BiliApp/{appVer} mobi_app/android channel/bilih5 " \
                 "Buvid/{Buvid} sessionID/{session_id} innerVer/{appVer} " \
                 "c_locale/zh_CN s_locale/zh_CN disable_rcmd/0 {pay_appVer} os/android model/M6 Note " \
                 "mobi_app/android build/{appVer} channel/bilih5 innerVer/{appVer} osVer/{osVer} network/2" \
    .format(app_build=app_build, appVer=appVer, Buvid=Buvid, chrome=chrome_version, osVer=osVer, pay_appVer=pay_appVer,
            phone=phone, session_id=session_id, s=android_api_level)

pay_User_Agent = "Mozilla/5.0 BiliDroid/{pay_appVer} (bbcallen@gmail.com) os/android model/{phone} mobi_app/android " \
                 "build/{appVer} channel/bilih5 innerVer/{appVer} osVer/{osVer} network/2" \
    .format(appVer=appVer, pay_appVer=pay_appVer, phone=phone, osVer=osVer)

nav_headers = {
    "native_api_from": "h5",
    "refer": all_url.mall_url,
    "User-Agent": app_User_Agent,
    "bili-bridge-engine": "cronet"
}

app_get_headers = {
    "native_api_from": "h5",
    "Referer": item_url,
    "User-Agent": app_User_Agent,
    "x-bili-trace-id": "",
    "x-bili-aurora-eid": x_bili_aurora_eid,
    "x-bili-aurora-zone": ""
}

app_post_headers = {
    "Buvid": Buvid,
    "native_api_from": "h5",
    "Referer": item_url,
    "X-CSRF-TOKEN": csrf,
    "User-Agent": app_User_Agent,
    "x-bili-trace-id": "",
    "x-bili-aurora-eid": x_bili_aurora_eid,
    "x-bili-aurora-zone": ""
}

pay_headers = {
    "APP-KEY": device,
    "bili-bridge-engine": "cronet",
    "Buvid": Buvid,
    "buildId": appVer,
    "cLocale": "zh_CN",
    "deviceFingerprint": devicefingerprint,
    "env": "prod",
    "fp_local": fp_local,
    "fp_remote": fp_remove,
    "session_id": session_id,
    "sLocale": "zh_CN",
    "User-Agent": pay_User_Agent,
    "x-bili-trace-id": "",
    "x-bili-aurora-eid": x_bili_aurora_eid,
    "x-bili-aurora-zone": ""
}

PcHeaders = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69"
}

# print(app_User_Agent)
# print(pay_User_Agent)


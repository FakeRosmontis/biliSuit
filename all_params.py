import tools
import json
import time

item_id = tools.get_value("item_id")
coupon_token = tools.get_value("coupon_token")
accessKey = tools.get_value("accessKey")
appVersion = tools.get_value("appVer")
pay_appVer = tools.get_value("pay_appVer")
csrf = tools.cookies_value("bili_jct")

params_nav = {
    "access_key": accessKey,
    "appkey": "1d8b6e7d45233436",
    "csrf": csrf,
    "disable_rcmd": 0,
    "statistics": json.dumps({"appId": 1,
                              "platform": 3,
                              "version": pay_appVer,
                              "abtest": ""}, separators=(',', ':')),
    "ts": 0,
}

params_item = {
    'item_id': item_id,
    'part': 'suit'
}

params_create = {
    "access_key": accessKey,
    "add_month": -1,
    "appkey": "1d8b6e7d45233436",
    "buy_num": 1,
    "coupon_token": "",
    "csrf":	csrf,
    "currency":	"bp",
    "disable_rcmd":	0,
    "item_id": item_id,
    "platform":	"android",
    "statistics": json.dumps({"appId": 1,
                              "platform": 3,
                              "version": pay_appVer,
                              "abtest": ""}, separators=(',', ':')),
    "ts": 0,
}

params_confirm = {
    'order_id': "",
    'csrf': csrf
}

trade_query_params = {
    'order_id': ""
}

user_multbuy_params = {
    'item_id': item_id
}

suit_asset_params = {
    'item_id': item_id,
    'part': 'suit',
    'trial': 0
}

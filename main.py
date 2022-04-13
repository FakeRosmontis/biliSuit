import math
import sys
import json
import logging
import time
import urllib.parse
import requests
import all_data, all_url, all_headers, all_params, tools


# 实例化session
bili = requests.session()
pay_data = all_data.pay_data
pay_query_data = all_data.pay_query_data

h1 = all_headers.app_get_headers
h2 = all_headers.app_post_headers
h3 = all_headers.pay_headers


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
handler = logging.FileHandler("log.txt")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

log_level = tools.get_value("log_level")
log_level = log_level.upper()
if log_level == "INFO":
    logger.setLevel(level=logging.INFO)
    handler.setLevel(logging.INFO)
elif log_level == "DEBUG":
    logger.setLevel(level=logging.DEBUG)
    handler.setLevel(logging.DEBUG)
else:
    logger.setLevel(level=logging.DEBUG)
    handler.setLevel(logging.DEBUG)
    logger.debug("Plese input correct log level.")
    sys.exit()


def verify():
    nav_params = all_params.params_nav
    nav_params["ts"] = math.ceil(time.time())
    signed_params = tools.appsign(nav_params)
    login = bili.get(url=all_url.login_api, headers=tools.mod_headers(h1),
                     cookies=tools.all_cookies(), params=signed_params)
    if login.json()['code'] == 0:
        logger.info("Login succeed.")
        logger.debug("Login information: " + login.text)
    else:
        logger.info("Cookies can not be used.")
        sys.exit()


def get_items():
    if all_params.params_item["item_id"] == "":
        logger.info("Item id is none, exit.")
        sys.exit()
    item = bili.get(url=all_url.item_url, headers=tools.mod_headers(h1), cookies=tools.all_cookies(),
                    params=all_params.params_item)
    # item = requests.get(url=all_url.item_url, headers=all_headers.app_get_headers, cookies=tools.all_cookies(),
    #                 params=all_params.params_item)
    # print(all_headers.app_get_headers)
    # pprint.pprint(item.headers)
    item_info = item.json()
    start_time = item_info["data"]["item"]["properties"]["sale_time_begin"]
    return int(start_time)


def get_time():
    bili_time = bili.get(url=all_url.time_api, headers=all_headers.pay_headers)
    bili_timestamp = bili_time.json()
    return bili_timestamp["data"]["now"]


def local_timestamp():
    time.sleep(0.001)
    return time.time()


def create_order(c_params):
    error_times = 0
    while True:
        try:
            all_params.params_create["ts"] = math.ceil(time.time())
            signed_params = tools.appsign(c_params)
            params = urllib.parse.urlencode(signed_params)
            create = bili.post(url=all_url.create_order, headers=tools.mod_headers(h2),
                               cookies=tools.all_cookies(),
                               params=params)
            logger.debug("Url debug info: " + create.url)
            # logger.debug("Create headers info: " + str(create.headers))
            if create.json()['code'] == 0:
                logger.info("Payment success.")
                logger.debug("Create order data:  " + json.dumps(create.json(), ensure_ascii=False))
                return create.json()
            elif create.json()['code'] == -403:
                logger.info("Your account has been banned.")
                logger.debug("Create order data:  " + json.dumps(create.json(), ensure_ascii=False))
                sys.exit()
            elif create.json()['code'] == 26125:
                logger.info("You don't have enough money, come again next time.")
                logger.debug("Create order data:  " + json.dumps(create.json(), ensure_ascii=False))
                sys.exit()
            else:
                error_times += 1
                logger.info("Code Status: " + json.dumps(create.json()['code'], ensure_ascii=False))
                logger.debug("Create order data:  " + json.dumps(create.json(), ensure_ascii=False))
                time.sleep(0.5)         # 等待500ms
                if error_times >= 3:    # 事实证明刷这个接口没有必要
                    logger.info("Error up to 10 times, exit.")
                    sys.exit()

        except Exception:
            logger.debug("Something error.")
            error_times += 1


def order(orderid):
    order_params = all_params.params_confirm
    order_params["order_id"] = orderid
    logger.debug("Order id data:  " + json.dumps(order_params, ensure_ascii=False))
    return order_params


def confirm_order(order_par):
    confirm = bili.post(url=all_url.confirm_order, headers=tools.mod_headers(h2), cookies=tools.all_cookies(),
                        params=order_par)
    logger.debug("Confirm data:  " + json.dumps(confirm.json(), ensure_ascii=False))
    return confirm.json()


def format_pay_data():
    data = all_data.pay_query_data
    data["timestamp"] = int(round(time.time() * 1000))
    logger.debug("Pay data:  " + json.dumps(pay_data, ensure_ascii=False))
    return data


def pay_return(pay1, pay2):
    pay_bp = bili.post(url=all_url.pay_bp, json=pay1, headers=tools.mod_headers(h3))
    logger.debug("Pay bp json:  " + json.dumps(pay_bp.json(), ensure_ascii=False))
    pay_query = bili.post(url=all_url.pay_query, json=pay2, headers=tools.mod_headers(h3))
    logger.debug("pay query json:  " + json.dumps(pay_query.json(), ensure_ascii=False))


def get_item(orderid):
    logger.info("Getting item id.")
    all_params.trade_query_params["order_id"] = orderid
    trade_query = bili.get(url=all_url.query_items, headers=tools.mod_headers(h1),
                           params=all_params.trade_query_params, cookies=tools.all_cookies())
    logger.debug("Trade query:  " + json.dumps(trade_query.json(), ensure_ascii=False))


def user_multbuy():
    user_multbuy = bili.get(url=all_url.user_multbuy, headers=tools.mod_headers(h1),
                            params=all_params.user_multbuy_params, cookies=tools.all_cookies())
    logger.debug("User multbuy:  " + json.dumps(user_multbuy.json(), ensure_ascii=False))
    
    
def get_item_id():
    suit_asset = bili.get(url=all_url.suit_asset, headers=tools.mod_headers(h1),
                          params=all_params.suit_asset_params, cookies=tools.all_cookies())
    logger.debug("Suit info:  " + json.dumps(suit_asset.json(), ensure_ascii=False))
    logger.info("编号：" + json.dumps(suit_asset.json()['data']['fan']['number'], ensure_ascii=False))


def main():
    # print(all_headers.app_get_headers)
    # print(all_headers.app_post_headers)

    check_time = 0
    # 可能会触发69949/26134，暂时注释掉
    # verify()
    start_time = get_items()
    # 提前四秒获取b站时间
    post_time = start_time - 4
    logger.info("Using local time now.")
    logger.info("Star time at " + str(start_time))
    time.sleep(1)

    while True:
        local_time = local_timestamp()
        print("\rLocal time: {t}".format(t=local_time), end="", flush=True)
        if local_time >= post_time:
            print("")
            logger.info("Get bili time now!")
            break

    while True:
        # bili_time = get_time()
        times = bili.get(url=all_url.time_api, headers=all_headers.pay_headers)
        bili_time = times.json()["data"]["now"]
        # 判断时间为前两秒
        if bili_time >= start_time - 2:
            # 提前进入抢购状态
            http_response_time = times.elapsed.total_seconds()
            tools.time_before(http_response_time)
            logger.info("Star to Buy!!!")
            break

    # 获取order_id,用于确认订单状态
    create_json = create_order(all_params.params_create)
    order_id = create_json['data']['order_id']
    order_params = order(order_id)

    # 确认订单信息
    logger.info("Start to confirm your order.")
    while True:
        confirm = confirm_order(order_params)
        confirm_status = confirm['data']['state']
        if confirm_status == "creating":
            logger.info("Order creating.")
            logger.debug("Confirm json" + json.dumps(confirm, ensure_ascii=False))
            time.sleep(0.1)
        elif confirm_status == "created":
            logger.info("Order has been created.")
            logger.debug("Confirm json" + json.dumps(confirm, ensure_ascii=False))
            pay_data_2 = confirm['data']['pay_data']
            pay_data_2 = json.loads(pay_data_2)
            for k in pay_data_2.keys():
                pay_data[k] = pay_data_2[k]
            break
        else:
            check_time += 1
            logger.info("Something error.")
            logger.debug("Confirm json" + json.dumps(confirm, ensure_ascii=False))
            if check_time >= 10:
                logger.info("Error up to 10 times, exit.")
                sys.exit()

    # 付款
    pay_pay = bili.post(url=all_url.pay_pay, json=pay_data, headers=tools.mod_headers(h3))
    payChannelParam = json.loads(pay_pay.json()['data']['payChannelParam'])
    queryOrderReqVO = pay_pay.json()['data']['queryOrderReqVO']

    logger.debug("Pay json: " + json.dumps(pay_pay.json(), ensure_ascii=False))
    logger.debug("Pay channel params: " + json.dumps(payChannelParam, ensure_ascii=False))
    logger.debug("Query order: " + json.dumps(queryOrderReqVO, ensure_ascii=False))

    # 返回支付数据
    logger.info("Return your payment information.")
    pay_return(payChannelParam, queryOrderReqVO)

    pay_query_data = format_pay_data()
    pay_ch = bili.post(url=all_url.pay_ch, json=pay_query_data, headers=tools.mod_headers(h3))
    logger.debug("Pay channel responses: " + json.dumps(pay_ch.json(), ensure_ascii=False))

    get_item(order_id)
    user_multbuy()
    get_item_id()


if __name__ == '__main__':
    main()


"""
通过“我的钱包”页面可抓 session_id, accessKey, fp_local, fp_remote, devicefingerprint, Device-ID, appVer, sdkVersion	 	
coupon_token 为优惠券token, 无则留空
session_id 每次启动app都不同（删进程）
"""

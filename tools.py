import json
import time
import hashlib
import urllib.parse
import uuid

config = json.loads(open("config.json", "r", encoding="utf-8").read())


def all_cookies():  # 将cookies转为json
    c = str(config["cookies"])
    cookies = {}
    for line in c.split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value
    return cookies


def cookies_value(key):
    return all_cookies()[key]


def get_value(key):
    return config[key]


def time_before(t1):
    t2 = config["time_before"]
    time.sleep(2 - t1 - t2/1000)


def appsign(params):
    appsec = "560c52ccd288fed045859ed18bffd973"
    # 为请求参数进行 api 签名
    params = dict(sorted(params.items()))  # 重排序参数 key
    query = urllib.parse.urlencode(params)  # 序列化参数
    sign = hashlib.md5((query + appsec).encode()).hexdigest()  # 计算 api 签名
    # print(sign)
    params.update({'sign': sign})
    return params


def bili_trace():
    a = "".join(str(uuid.uuid4()).split("-"))
    t = int(round(time.time()))
    b = hex(t)
    trace_id = a[0:26] + b[2:8] + ":" + a[16:26] + b[2:8] + ":0:0"
    return trace_id


def mod_headers(h):
    h["x-bili-trace-id"] = bili_trace()
    return h


'''
参考资料：
https://blog.csdn.net/qq_38851536/article/details/114238361
https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/other/API_sign.md
'''




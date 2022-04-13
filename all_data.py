import json
import uuid
import tools

accessKey = tools.get_value("accessKey")
appVersion = tools.get_value("appVer")
sdkVersion = tools.get_value("sdkVersion")
device = str.upper(tools.get_value("device"))
traceId = str(uuid.uuid1())

pay_data = {
    "accessKey": accessKey,
    "appName": "tv.danmaku.bili",
    "appVersion": appVersion,
    "device": device,
    "network": "WiFi",
    "payChannel": "bp",
    "payChannelId": 99,
    "realChannel": "bp",
    "sdkVersion": sdkVersion,
}

pay_query_data = {
    "accessKey": accessKey,
    "appName": "tv.danmaku.bili",
    "appVersion": appVersion,
    "customerIds": ["10002"],
    "device": "ANDROID",
    "deviceType": 3,
    "network": "WiFi",
    "sdkVersion": sdkVersion,
    "timestamp": "",
    "traceId": traceId,
    "version": "1.0"
}
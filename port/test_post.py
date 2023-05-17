# -*-coding:utf-8-*-
import requests
import urllib3
urllib3.disable_warnings()

# 首页
url = "https://test-baodian.tal.com/exactly/api/v1/learn_center/primary/index"
data = {
        "grade": 3
    }
headers = {
        'Authorization': 'tal173X8ohYA1AdhpImi4uifvEro-FYcFRZrOd_cZD5CPGasLcDCtKMWiZbGV1mOZNThK_EAwkdeLIVVjPPFYrwfP8-1Jvs5Uk2avHunQ_Hf6znA17dwXz-7A-wqFagCjP4v2NuY6BP82mUtLm5bn8MMlobAU6T7pQrs-o7-mtSVZj2iIml',
        # 'X-Tal-Sn': '71DC0522A2000216',
        # 'X-Tal-Version': 'D230321',
        # 'X-Tal-Sign': '035c803b00d3cecb6fb7988439fb9f7e',
        # 'X-Tal-ClientId':'552402',
        # 'X-Tal-Gps': '',
        # 'X-Tal-AppVersion': '230316789',
        # 'X-Tal-Timestamp': '1679640954',
        # 'X-Tal-DeviceId': 'TAL2205F6B5C831BDEDB962D1E0D8B09203016D',
        # 'X-Tal-Nonce': 'c0825bcb-3ded-4dca-86d9-85915c7bf8bc',
        # 'X-Tal-PackageName':'com.tal.pad.launcher',
        # 'X-Tal-AppKey': 'hs_v1_0_0',
        # 'traceparent': '00-ab19da172827f197811ead28618ed1a8-d52b3b153606f131-01',
        # 'Host': 'test-baodian.tal.com',
        # 'User-Agent': 'okhttp/3.14.9',
        'Content-Type': 'application/json',
        'Cookie': 'tal173X8ohYA1AdhpImi4uifvEro-FYcFRZrOd_cZD5CPGasLcDCtKMWiZbGV1mOZNThK_EAwkdeLIVVjPPFYrwfP8-1Jvs5Uk2avHunQ_Hf6znA17dwXz-7A-wqFagCjP4v2NuY6BP82mUtLm5bn8MMlobAU6T7pQrs-o7-mtSVZj2iIml'
    }

response = requests.post(url=url, json=data, headers=headers, verify=False)
print(response.text)
# -*-coding:utf-8-*-
import requests
import urllib3
urllib3.disable_warnings()


# 登录，每次获取新token
def login():
    url = "https://sso.zhiyinlou.com/portal/api/v1/login"
    data = "account=yangzhiqi%40tal.com&password=6isSGC%2BAAPvs3U0a%2BaApBg%3D%3D&appid=1039646235&plat=Web&query=41386802614584d031839dd0369adc3d&ticket=bfb0c6da00b4c9c835b39ef18e297f55&captchaCode=&encrypt=a8c2165b-10ac-47ee-87f1-77c54c6559ed"

    headers = {
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'apiToken': 'eyJpdiI6IkdabjJmd1BZTitHUUM3UzdnWkw4dVE9PSIsInZhbHVlIjoiYTlVXC9GRlBqMHNteFk0UWlSOTYrQm9tWm56bjVcL1BTZHhxWEFzTTU4MzBvPSIsIm1hYyI6ImJhMWY4MzlhYTcxZjI0ZDU3N2ExMzRmYjVhMWY4MWVhZTIzMmVmNzUyMGIzNDM3NThhNTQzZGI0MzE4OWUwY2IifQ==',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-platform': '"macOS"',
        'Origin': 'https://sso.zhiyinlou.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://sso.zhiyinlou.com/portal/login/1039646235?adminIntellect=https://test-member.tal.com/adminIntellect/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
         'Cookie': '_ga=GA1.2.1056029327.1640586844; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22182169f9fe5bcb-06efb9bc7fc574-1c525635-2007040-182169f9fe6cd4%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fsso.100tal.com%2F%22%7D%2C%22%24device_id%22%3A%22182169f9fe5bcb-06efb9bc7fc574-1c525635-2007040-182169f9fe6cd4%22%7D; userid=46127; mp_eSpCz4lYpMYgtuhdH0F6Wgtt_mixpanel=%7B%22distinct_id%22%3A%20%2217dfa9896ab14c-07046ec62880dc-36657407-168000-17dfa9896acc1e%22%2C%22_id%22%3A%20%225ff3587c9d5bae1d4c66a750%22%2C%22email%22%3A%20%22yangzhiqi%40tal.com%22%2C%22lang%22%3A%20%22zh%22%2C%22name%22%3A%20%22%E6%9D%A8%E8%8A%9D%E7%90%AA%22%2C%22userKey%22%3A%20%225ff3587c9d5bae1d4c66a750%22%2C%22%24os_version%22%3A%20%22Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fproject.zhiyinlou.com%2Forganization%2F5c550302be825b5b84a4ac9b%2Fprofile%2F5cc68599be825bf627498ec9%22%2C%22%24initial_referring_domain%22%3A%20%22project.zhiyinlou.com%22%2C%22avatarUrl%22%3A%20%22https%3A%2F%2Fprojectfile.zhiyinlou.com%2Fthumbnail%2F0128e20a1e62c6c82904310acd4c61f2cee8%2Fw%2F200%2Fh%2F200%22%2C%22language%22%3A%20%22zh%22%2C%22region%22%3A%20%22cn%22%2C%22latestActived%22%3A%20%222021-04-24T15%3A08%3A05.735Z%22%7D; grey=0; ttc-token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdmF0YXIiOiJodHRwczpcL1wveWFjaC1zdGF0aWMuemhpeWlubG91LmNvbVwvb25saW5lXC9qc2FwaVwvMjk1OTE3XC8xNjM5MzE0MTg2MTgwXC8xYzMyZWNlNWIwMThjMTBhN2VjZDIxOGNiYzdmZDIyMlwvMGUzOTUyNzQtOWVjNi00ZWFmLWJiZGItYjBkNWVmZjM3OWY1LmpwZyIsImRlcGFydG1lbnQiOiJUZWFtIDItXHU2NjdhXHU4MGZkXHU1MTg1XHU1YmI5XHU3ZWM0LVx1NjY3YVx1ODBmZFx1NWI2Nlx1NGU2MC1cdTRlYTdcdTU0YzFcdTRlMDBcdTkwZTgtXHU1ZGU1XHU3YTBiXHU3ODE0XHU1M2QxXHU5MGU4LVx1OGQyOFx1OTFjZlx1NzgxNFx1NTNkMVx1N2VjNCIsImRpbmdfaWQiOiIiLCJlbWFpbCI6Inlhbmd6aGlxaUB0YWwuY29tIiwibmFtZSI6Ilx1Njc2OFx1ODI5ZFx1NzQyYSIsInBvc2l0aW9uIjoiIiwid29ya2NvZGUiOiIyNTQ2NzMiLCJpZCI6NDYxMjcsImV4cGlyZSI6MTY5MjU5ODE1OH0.YFNFIyeYvZRl_AwwU1N0zhENR04d-TeIh95btvqvfo8; referral=%7B%22domain%22%3A%22sso.100tal.com%22%2C%22path%22%3A%22%2F%22%2C%22query%22%3A%22%22%2C%22hash%22%3A%22%22%7D; mp_123456_mixpanel=%7B%22distinct_id%22%3A%20%2217dc249ddd9dba-0107e7090dc678-36657407-168000-17dc249dddac20%22%2C%22userKey%22%3A%20%225ff3587c9d5bae1d4c66a750%22%2C%22created_at%22%3A%20null%2C%22userLanguage%22%3A%20%22zh%22%2C%22env%22%3A%20%22production%22%2C%22version%22%3A%20%2211.21.3-private.29%22%2C%22daysSinceRegistered%22%3A%2019439%2C%22timezone%22%3A%208%2C%22experiments%22%3A%20%5B%5D%2C%22%24os_version%22%3A%20%22Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; SSO_SESSION_ID=d7D3kLMbS0K38iZDI2QXSKRIBg50sjOKVN7m8Jwq; SSO_SESSION_ID=zXWZEqqEOQTfnsr9tyBKhduYvCrefYa7lZ7YmOEU; TALSSO=eyJpdiI6IlVVbSs3dHc3QXRsdVhcL1JLamsyOElRPT0iLCJ2YWx1ZSI6IlJOdnpvWnNzR1pnZm1ickY4WTJwZk1jZEprblgyUUdhV0E5WklFOERqbW5ZcU9mejFTdTllVmFHY3lYZjNjOEx5RVJpeTlBODJ0aHgxVWd2T1FzOTFFNytpcW1PQWxSeWNvcWt1Q0Vpa2VFPSIsIm1hYyI6IjgwMjI2YTFjM2FlNTdmMDg1MjZmOWNkMmJmM2JhYWJjYzkwN2JjMTA5ZWIxZmIzNjMwYTY5OTFjYmVlNmVmODcifQ%3D%3D; TALSSO_PWD_ERROR=0; grey=0',
    }

    response1 = requests.post(url=url, data=data, headers=headers, cookies=cookies, verify=False)
    response_token1 = response1.json()
    # print(response_token)

    global token
    token = response_token1["data"]["token"]
    print("sso鉴权，获取的token传参给cms登录接口：")
    print(token)


# cms后台登录
def cmsLogin():
    url = "https://test-member.tal.com/admin/api/sso/authorize"
    token = "eyJpdiI6Iml0eU5saWlYNldIUnMrdUJNK1lnZXc9PSIsInZhbHVlIjoieHRGaW55RGFVdUdUXC82clpTenJxejd1NjU4aXNzK2p3UWpYeHcrUG12cTVVK2hWbjZBcnJraWRHNGsyRmxJUEFmcFNrMUYwamhvRlBFdHhOcnZNU0tYeVZJRm16K1FqbTNlZHRFOEN5aEFRPSIsIm1hYyI6ImYzNWFjNzJjMDY4ZDI2NjA4ODAzNWRkYTM5YzViYmNkYmIxM2NhMDg5OTU5NmU5NGEwNmU5YTI4ZTEyNDA1ZTUifQ=="
    data = {
        "zyl_token": token
    }

    headers = {
        'Host': 'test-member.tal.com',
        'Cookie': 'imfetoken=702dc3250dfdcdf72155ff2025a4e16d; tal_token=tal173X8ohYA1AdhpImi4uifvEro-FYcFRZrOd_cZD5CPGasLcDCtKMWiZbGV1mOZNThK_EAwkdeLIVVjPPFYrwfP8-1Jvs5Uk2avHunQ_Hf6znA17dwXz-7A-wqFagCjP4v2NuY6BP82mUtLm5bn8MMlobAU6T7pQrs-o7-mtSVZj2iIml',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'accept': 'application/json, text/plain, */*' ,
        'sec-ch-ua-platform': '"macOS"',
        'content-type': 'application/json',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'authtoken': 'null',
        'origin': 'https://test-member.tal.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://test-member.tal.com/systemCenter/?token=eyJpdiI6IlcrV2d4UEdvSjd1aDlzbXpHOGVSNHc9PSIsInZhbHVlIjoiS0VMRDRqbkJvN0k4WGM2VVc4OURFWXREXC9mcERWRUhIRmhUdG1QWXpNNTNENVJDSWxqSm95YVI5QWN6dGZXeHpLaXNFUWxVd1U5SHlTZXlYYmZZalkwQ3NmaWxuREZ3cTFrTGZqZ1YzQ0dFPSIsIm1hYyI6IjhiZGVkYTUwNmJhNTcyOTI5NDk0NGFlNmYwNDY4ZWZhNWY4YzUxMWNlZWI5M2Y5MjEwMzFiNzc4NWJiYTYxODQifQ==&adminIntellect=https%3A%2F%2Ftest-member.tal.com%2FadminIntellect%2F',
        'accept-language': 'zh-CN,zh;q=0.9'
    }

    response2 = requests.post(url=url, json=data, headers=headers, verify=False)
    # print(response2.text)

    response_token2 = response2.json()
    # print(response_token2)

    global authtoken
    authtoken= response_token2["data"]["token"]

    print("cms后台登录，再将authtoken传给用户详情接口的header中：")
    print(authtoken)


def userDetail():
    url = "https://test-member.tal.com/admin/api/user/detail"
    cookies = {
        'imfetoken': '702dc3250dfdcdf72155ff2025a4e16d',
        'tal_token': 'tal173X8ohYA1AdhpImi4uifvEro-FYcFRZrOd_cZD5CPGasLcDCtKMWiZbGV1mOZNThK_EAwkdeLIVVjPPFYrwfP8-1Jvs5Uk2avHunQ_Hf6znA17dwXz-7A-wqFagCjP4v2NuY6BP82mUtLm5bn8MMlobAU6T7pQrs-o7-mtSVZj2iIml',
    }
    headers = {
        'Host': 'test-member.tal.com',
        # 'Cookie': 'imfetoken=702dc3250dfdcdf72155ff2025a4e16d; tal_token=tal173X8ohYA1AdhpImi4uifvEro-FYcFRZrOd_cZD5CPGasLcDCtKMWiZbGV1mOZNThK_EAwkdeLIVVjPPFYrwfP8-1Jvs5Uk2avHunQ_Hf6znA17dwXz-7A-wqFagCjP4v2NuY6BP82mUtLm5bn8MMlobAU6T7pQrs-o7-mtSVZj2iIml',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'accept': 'application/json, text/plain, */*',
        'authtoken': '702dc3250dfdcdf72155ff2025a4e16d',
        # 'authtoken': authtoken,
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://test-member.tal.com/adminIntellect/',
        'accept-language': 'zh-CN,zh;q=0.9'
    }

    response3 = requests.get(url=url, headers=headers, cookies=cookies, verify=False)
    print("用户详情接口信息：")
    print(response3.text)


if __name__ == '__main__':
    # 1、先sso鉴权，获取sso的token
    # login()

    # # 2、cms后台登录，传参sso的token
    # cmsLogin()

    # 3、用户详情，传cms登录的接口的authtoken信息
    userDetail()
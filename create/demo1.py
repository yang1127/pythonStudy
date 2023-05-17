# -*-coding:utf-8-*-
import requests

'''
# 基本使用
response = requests.get(url="http://httpbin.org/get")
print(response.text)
'''

'''
# 添加headers
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'ci=1%2C%E5%8C%97%E4%BA%AC; ci.sig=pm2UF_F52zvopd9VUIy6q53v_5w; featrues=[object Object]; featrues.sig=KbQquuOrr42L3kMHbtKc319ems8; uuid_n_v=v1; iuuid=ABB128E0C95911EDB097BD6262BA07EC599F85A0E1BB4884A556306B34E1F62E',
    'Host': 'i.maoyan.com',
    'Pragma': 'no-cache',
    'Referer': 'https://i.maoyan.com/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'
}

response = requests.get(url="http://httpbin.org/get", headers=headers)
print(response.text)
'''

# 路径参数
url = "https://www.maoyan.com/board/4"

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'ci=1%2C%E5%8C%97%E4%BA%AC; ci.sig=pm2UF_F52zvopd9VUIy6q53v_5w; featrues=[object Object]; featrues.sig=KbQquuOrr42L3kMHbtKc319ems8; uuid_n_v=v1; iuuid=ABB128E0C95911EDB097BD6262BA07EC599F85A0E1BB4884A556306B34E1F62E',
    'Host': 'i.maoyan.com',
    'Pragma': 'no-cache',
    'Referer': 'https://maoyan.com/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'
}
for page in range(10+1):
    params = {
        "offset": page * 10
    }
    response = requests.get(url=url, params=params, headers=headers)
    print(response.url)
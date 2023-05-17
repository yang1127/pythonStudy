# -*-coding:utf-8-*-
import requests

url = "https://test-member.tal.com/exactly/api/course/list"

headers = {
    'content-type': "application/json; charset=utf-8",
    'authtoken': "cd07d04d6ddb5e77fd58aa6f3445c169"
}

data = {"course_systems": "5", "subjects": "1", "currentPage": 1, "page_size": 10, "page": 1}

response = requests.post(url, json=data, headers=headers)

print(response.text)
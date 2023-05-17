# -*-coding:utf-8-*-
import requests

# 封装url、header
class CreateLesson():
    def __init__(self, grade, semester, subject, version, module_type, course_name, course_system):
        self.grade = grade
        self.semester = semester
        self.subject = subject
        self.version = version
        self.module_type = module_type
        self.course_name = course_name
        self.course_system = course_system

    def create_lesson(self):
        url = "https://test-member.tal.com/exactly/api/course/add"

        headers = {
            'authorit': 'test-member.tal.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'authtoken': '702dc3250dfdcdf72155ff2025a4e16d',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'cookie': 'imfetoken=702dc3250dfdcdf72155ff2025a4e16d; tal_token=tal173O2m1-OFxpwskQ5C3RQjsnXMnoRmJC4w2-tJvDrDAjQQQwAZIWrR6OpnusQXA_3-nLFSXsgrVeX_K8jy9ulZFXJOtLxqCJf_ZqG1G_IGsHGf4vcmrMCD1C2gbjJ6295q0ORWjAfFS0SN_xF5NRZXZsVL06s_DUYBCw36SR8r7oS0ml',
            'origin': 'https://test-member.tal.com',
            'pragma': 'no-cache',
            'referer': 'https://test-member.tal.com/adminIntellect/',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        }

        json_data = {
            "grade": self.grade,
            "semester": self.semester,
            "subject": self.subject,
            "version": self.version,
            "module_type": self.module_type,
            "course_name": self.course_name,
            "course_system": self.course_system,
            "cover": "https://aliresource-member.tal.com/tocCmsPic/f1ca84ca-2fda-4ebe-8e21-b49113a66bea-1679560760971.jpg",
            "cover_special": "https://aliresource-member.tal.com/tocCmsPic/e679c404-6a96-4075-a829-3303314797e0-1679560766795.jpg",
        }

        response = requests.post(url=url, json=json_data, headers=headers)
        print(response.text)


if __name__ == "__main__":
    cl = CreateLesson("1", "5", 1, 5, 1, "测试", 5)
    cl.create_lesson()

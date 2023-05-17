# -*-coding:utf-8-*-
old_str = "hello xiaoyang"
new_str = old_str[::-1]
print(new_str)

old_str1 = "hello xiaoyang"
new_str1 = ''.join(reversed(old_str1))
print(new_str1)

old_str2 = "hello xiaoyang"
new_str2 = list(old_str2)
new_str2.reverse()
print(''.join(new_str2))


def func(content):
    if len(content) <= 1:
        return content
    return func(content[1:]) + content[0]

old_str3 = "hello"
print(func(old_str3))
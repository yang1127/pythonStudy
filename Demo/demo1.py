# -*-coding:utf-8-*-
str = 'hello'
str1 = ""
i = len(str) - 1
while i >= 0:
    str1 += str[i]
    i -= 1

print(str1)
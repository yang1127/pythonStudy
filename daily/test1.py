# -*-coding:utf-8-*-

# 练习 if elif else语法
# age = input('输入')
# if (int(age) >= 18) and (int(age) <= 45):
#     print(11)
# elif int(age) > 45:
#     print(22)
# else:
#     print(33)

# 练习3目运算 xx if a else b
# a = 2
# b = 3
# result = (a - b) if a > b else (b - a)
# print

# 练习循环语句 while
# i = 1
# a = 10
# count = 0
# while i < a:
#     count += i
#     i += 1
# print(count)

# 练习循环语句 for in range(a, b, step):
# for i in range(5):
#     print(i)

# for i in range(2, 6):
#     print(i)

# for i in range(2, 6, 2):
#     print(i)

# a = 2
# b = 6
# step = 2
# for i in range(a, b, step):
#     print(i)

# for i in range(5):
#     print(i)
#     for j in range(6):
#         print(j)

# for i in range(5):
#     for j in range(5):
#         print('*', end=" ")
#     print()

# 练习字符串
# name = 'yzq'
# res = name * 3
# print(res)

# 下标
# str = 'helloyangzhiqi'
# print(str[0])
# print(str[-1])
# print(len(str))
# print(str[len(str)-1])


# 切片[start:end:step] 左闭右开
# str = 'helloyangzhiqi'
# print(str[0:2])
# print(str[-5:-1])
# print(str[:3])
# print(str[3:])
# print(str[0:-1:2] + str[0:2])
# print(str[::])
# print(str[-1:-5:-1])
# print(str[::-1])  # 字符串逆转

# find、rfind 查找
# str = 'helloyangzhiqi'
# print(str.find('yan'))
# print(str.find('z', 1, 2))
# print(str.rfind('i'))

# 统计出现的次数
# str = 'helloyangzhiqi'
# print(str.count('i'))


# 替换 str.replace(oldstr, newstr, count)
# str = "yang yang zhi qi yangyang hello hi your name"
# str1 = str.replace('yang', 'yzq', 1)
# print(str1)

# 分割 str.split(str1, count)、str.rsplit(str1, count)
# str = "yang yang zhi qi yangyang hello hi your name"
# str1 = str.split(' ')  # 用空格分割
# str2 = str1[0]  # 取下标为0的数值
# print(str2)


# 字符串拼接
# list = ['yzq', 'hello']
# print('_'.join(list))

# 列表遍历
# list = [1, 2, 3, 4, 5, 6]
# for i in list:
#     print(i)
#
# j = 0
# while j < len(list):
#     j += 1
# print(j)

# 列表删除
# remove()
# list = [1, 2, 3, 4, 5, 'yzq']
# list.remove('yzq')
# print(list)

# pop(下标)
# list = [1, 2, 3, 4, 5, 'yzq']
# list.pop(0)
# print(list)

# del 列表[下标]
# list = [1, 2, 3, 4, 5, 'yzq']
# del list[0]
# print

# 列表排序
# list = [9, 1, 4, 2, 8]
# list.sort()
# print(list)

# list = [9, 1, 4, 2, 8]
# list1 = sorted(list)
# print(list)
# print(list1)

# 列表逆置
# list = [1, 2, 3, 4, 5]
# list1 = list[::-1]
# list.reverse()
#
# print(list1)
# print(list)

# 列表嵌套
# list = [
#     ['清华', '北大'],
#     ['厦大', '天津大学'],
#     ['山东大学', '中国海洋大学']
# ]
#
# print(list[1])
# print(list[1][1])
# print(list[1][1][1])
#
# for list1 in list:
#     print(list1)
#
# for list1 in list:
#     for list2 in list1:
#         print(list2)

# 列表中的key
# list = [
#     {'name': 'yzq', 'age': 18},
#     {'name': 'd', 'age': 19},
#     {'name': 'yy', 'age': 20}
# ]

# list.sort(key=lambda x: x['name'])
# print(list)

# list.sort(key=lambda  x: x['age'])
# print(list)

# list = ['a', 'ccc', 'bb', 'dddd']
# list.sort(key=lambda x: len(x))
# print(list)

# 字典
# dict = {'name': 'yzq', 'age': 18, 'like': ['pingpong', 'hahah~']}
# print(dict['name'])
# print(dict['like'][0])
# print(dict['like'][0][1])

# key是否存在 get(key, value)
# print(dict['yzq']) # 报错
# print(dict.get('yzq')) # None

# 长度
# print(len(dict))

# 添加、修改
# dict['name'] = 'Yang'
# print(dict)
#
# dict['life'] = 'sleep'
# print(dict)

# 删除
# del dict['name']
# print(dict)
#
# dict.pop('age')
# print(dict)

# del dict
# print(dict)

# 遍历
# for i in dict: # key
#     print(i)
#
# for j in dict.values():
#     print(j)


# set
# s = set([1, 2, 3, 4, 4, 5])
# print(s)

# 添加
# s.add(6)
# print(s)

# 删除
# s.remove(4)
# print(s)
#
# x = s.pop()  # 头删
# print(x)

# s1 = set([1, 3, 2])
# s2 = set([7, 9, 6])
# s3 = s1 | s2
# str1 = str(s3)
# print(str1)
#
# s = set([1, 2, 3, 4, 4, 5])
# print('6' in s)
# print('6' not in s)


# 迭代器



# 生成器
# L = [1, 2, 'yzq', True, 3.1415726]
# print(type(L))
# print(L)
#
# G = (x for x in range(10))
# for n in G:
#     print(n)


# 斐波那契数列0 1 1 2 3 5 8
# def func(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
# f = func(6)



# 函数
# def add(a, b):
#     return a + b
#
# print(add(1, 2))

# # 普通
# def fun1(a1, b1):
#     return a1 + b1
#
# print(fun1(1, 2))
#
# # 缺省
# def fun2(a2, b2 = 1):
#     return a2 + b2
#
# print(fun2(1, b2=10))
#
#
# # 不定长元祖
# def fun3(a3, *args):
#     count3 = 0
#     for i in args:
#         count3 += i
#     return a3 + count3
#
# print(fun3(1, 1, 2, 3, 4, 5))
#
# # 不定长字典
# def func4(a4, **kwargs):
#     count4 = 0
#     for j in kwargs.values():
#         count4 += j
#     return a4 + count4
#
# print(func4(1, a=1, b=2, c=3, d=4, e=5))

# lambda
# f = lambda x: x*x
# print(f(5))

def now():
    print('2015-3-25')

print(now.__name__)

# -*-coding:utf-8-*-
'''
# filter使用 - 普通函数
old_list = [1, 2, 3, 4, 5, 6, 7, 8]

def func1(n):
    if n % 2 == 0:
        return True
    return False

new_list = filter(func1, old_list)

# for i in new_list:
#     print(i)
result_list = list(new_list)
print(result_list)
'''

'''
# filter使用 - 匿名函数
# 过滤0
old_list = [1, 0, 2, 4, 0, 0, 0, 10]
new_list = filter(lambda x: x != 0, old_list)
result_list = list(new_list)
print(result_list)
'''

'''
# 过滤出大写、小写字母
old_list = ['A', 'c', 's', 'S', 'D']
newlist_upper = filter(lambda x: x.isupper(), old_list)
newlist_lower = filter(lambda x: x.islower(), old_list)

# 大写
resultlist_upper = list(newlist_upper)
print(resultlist_upper)

# 小写
resultlist_lower = list(newlist_lower)
print(resultlist_lower)

# 大写、小写排序
result = list(resultlist_upper + resultlist_lower)
print(result)
'''

old_list = [
    {'name': 'Tom', 'sorce': 11},
    {'name': 'Rose', 'sorce': 88},
    {'name': 'LiLi', 'sorce': 33},
    {'name': 'ZZ', 'sorce': 99},
]

new_list = filter(lambda x: x['sorce']>70, old_list)
result_list = list(new_list)
print(result_list)
# -*-coding:utf-8-*-
# 普通函数
from functools import reduce

a = [1, 2, 3, 4]

def add(x, y):
    return x + y

print(reduce(add, a))

# 使用lambda
nums = [1, 2, 3, 4]

result = reduce(lambda x, y: x+y, nums)
print(result)
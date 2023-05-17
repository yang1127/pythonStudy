# -*-coding:utf-8-*-
'''
# 题1：求字符串最后一个单词的长度
# 思路：按空格分隔，找最后一个单词在分割后的位置，再求长度
str = input()
list = str.split(" ")
n = len(list) - 1
print(len(list[n]))
'''

'''
# 题2：求字符出现的次数，不区分大小写
# 思路：将输入均转换为小写，内置函数count()统计st2在st1出现的次数
st1 = input().lower()
st2 = input().lower()
print(st1.count(st2))
'''

'''
# 题3：字符串分隔
# 思路：足8个分隔，不足右对齐补充0
l = input()
for i in range(0, len(l), 8):
    print("{0:0<8}".format(l[i:i+8]))
'''

'''
# 题4：16进制转换10进制
# python将16进制转为10进制可以用int('hex型',16) 八进制转十进制int('八进制型',8) 八进制或十六进制或10进制装二进制直接调用 bin(任意进制)
s = input()
print(int(s, 16))
'''

'''
# 题5：字符串反转
st = input()
st1 = ""
st2 = st1.join(reversed(st))
print(st2)
'''

'''
# 题6：质子因数
# 思路：1）输入的数字本身就是质数，那么输出结果只有该数字本身；
# 2）输入的数字是合数：从2开始遍历，如果遍历到的数字是质数，且该数字是输入整数的因数，则该数字符合要求输出。
# 否则继续遍历查询。找到质数因子后，整数除以质数因子，递归查找，直至本身不断的除以找到的质数因子变成质数结束递归。

import math
n = int(input())
for i in range(2, int(math.sqrt(n))+1):
    while n % i == 0:
        print(i, end=' ')
        n = n // i

if n > 2:
    print(n)
'''

'''
n = float(input())
y = lambda x: int(x+0.5)
print(y(n))
'''

'''
# 题7：合并表记录
n = int(input())
dic = {}

# idea: 动态建构字典
for i in range(n):
    line = input().split()
    key = int(line[0])
    value = int(line[1])
    dic[key] = dic.get(key, 0) + value  # 累积key所对应的value

for each in sorted(dic):  # 最后的键值对按照升值排序
    print(each, dic[each])
'''

'''
# 题8：不重复数字
# 思路：1）输入完，直接将数组置成反序
# 2）遍历，将数据存储在hash中，hash去重
# 3）再遍历hash中存储的数据，输出
nums = input()[::-1]
hash = dict()
res = ""
for key, value in enumerate(nums):
    hash[value] = key

for i in hash.keys():
    res += i

print(res)
'''

'''
# 题9：字符个数统计
# 思路：1）将输入的字符串放置hash中（hash不重复）
# 2）统计hash中的个数
st = input()
hash = dict()
for key, value in enumerate(st):
    hash[value] = key

res = len(hash)

print(res)
'''

'''
# 题10：数字颠倒
nums = input()[::-1]
print(nums)
'''

# 题11：句子逆序
# i am a girl
# girl a am i
# 思路：1）输入字符串，以空格逆向分隔
# 2）再添加空格，使用join拼接成字符串

# st = input()
# res = ""
# st1 = st.split(" ")[::-1]
# st2 = " ".join(st1)
# for i in st2:
#     res += i
#
# print(res)




# 
# -*-coding:utf-8-*-
import re

old_str = "hello yang zhao 11 77 99"
print(old_str)  # hello yang zhao 11 77 99

# split()
new1 = re.split(" ", old_str)
print(new1)  # ['hello', 'yang', 'zhao', '11', '77', '99']

# sub()
new2 = re.sub("[^A-Za-z]", " ", old_str)
print(new2)  # hello yang zhao

# subn()
new3 = re.subn("[^A-Za-z]", " ", old_str)
print(new3)  # ('hello yang zhao         ', 11)


def dedup(items):
    list = []
    seen = set()
    for item in items:
        if item not in seen:
            list.append(item)
            seen.add(item)
    return list


nums = [1, 1, 2, 2, 3, 4]
print(dedup(nums))

# -*-coding:utf-8-*-
'''
# 冒泡排序
arr = [3, 44, 38, 5, 47, 15, 36, 26]
print(len(arr))

def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubbleSort(arr))
'''

'''
# 选择排序
arr = [3, 44, 38, 5, 47, 15, 36, 26]

def selectSort(arr):
    for i in range(len(arr)-1):
        minindex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minindex]:
                minindex = j

            if i != minindex:
                arr[minindex], arr[i] = arr[i], arr[minindex]
    return arr

print(selectSort(arr))
'''

'''
#  插入排序
arr = [3, 44, 38, 5, 47, 15, 36, 26]

def insertSort(arr):
    for i in range(len(arr)):
        cur = arr[i]
        preindex = i-1
        while preindex >= 0 and cur < arr[preindex]:
            arr[preindex+1] = arr[preindex]
            preindex -= 1
        arr[preindex+1] = cur

    return arr

print(insertSort(arr))
'''







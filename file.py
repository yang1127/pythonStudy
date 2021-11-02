'''
# 文件：可以永久保存数据
# 文件在硬盘中存储的格式是二进制
# 操作步骤：打开文件、读写文件、关闭文件

# 1、打开文件：文件从磁盘中存到内存中
# open(file, mode='r', encoding=None)
# file：要操作的文件名字 - 字符串
# mode：文件打开的方式 - r只读、r只写、a追加打开
# encoding：文件的编码格式，常见的编码格式有两种，一种为gbk、一种为utf-8
# 返回值，文件对象

# 以只读的方式打开当前目录中的。test.txt 文件，文件不存在会报错
f = open('test.txt', 'r')

# 2、读文件  文件对象.read()
buf = f.read()
print(buf)

# 3、关闭文件  文件.close()  将内存中的三大文件同步到硬盘中
f.close()
'''

'''
# 1、打开文件，文件不存在则创建、文件存在则覆盖
f = open('xiaoyang.txt', 'w', encoding='utf-8')

# 2、写入：windows默认是gbk，pycharm默认为utf-8，需统一处理为一种编码
f.write('hello xiaoyang\n')
f.write('hello yzq\n')
f.write('小杨吖～～\n')

# 再读
f = open('xiaoyang.txt', 'r')
buf = f.read()
print(buf)

# 3、关闭
f.close()
'''

'''
# 追加打开，在文件末尾写入内容
f = open('xiaoyang.txt', 'a', encoding='utf-8')
f.write('杨芝琪\n')

f = open('xiaoyang.txt', 'r')
buf = f.read()
print(buf)

f.close()
'''

'''
# 1、打开文件
f = open('xiaoyang.txt', 'r', encoding='utf-8')

# 2、读写文件 文件对象.read(n) n 一次读取多少字节的内容
buf = f.read(10)
print(buf) # hello xiao

# 3、关闭文件
f.close()
c
'''

'''
# 1、打开文件
f = open('xiaoyang.txt', 'r', encoding='utf-8')

# 2、读写文件
# 文件对象.readline() 一次读取一行内容，返回值为str
# 文件对象.readlines() 一次读取所有行，返回值为列表，列表中的每一项是一个字符串

buf = f.readline()
# buf = f.readlines()
print(buf) 

# 3、关闭文件
f.close()
'''

'''
# 模拟读取大文件
# 有规律的文件
f = open('test1.txt', 'r', encoding='utf-8')
while True:
    buf = f.readline()
    if buf: # if len(buf) > 0, 容器可以直接作为判断条件，容器有内容，为True
        print(buf, end='')
    else:
        # 文件读完
        break
f.close()

# 无规律文件
f = open('test2.txt', 'r', encoding='utf-8')
while True:
    buf = f.read(4)
    if buf: # if len(buf) > 0, 容器可以直接作为判断条件，容器有内容，为True
        print(buf, end='')
    else:
        # 文件读完
        break
f.close()
'''

'''
# 二进制文件操作
# encode() 转为二进制
f = open('test3.txt', 'wb')
f.write('你好'.encode())
f.close()


f1 = open('test3.txt', 'rb')
buf = f1.read()
print(buf)  # 二进制
print(buf.decode()) # 转为字符串
f1.close()
'''























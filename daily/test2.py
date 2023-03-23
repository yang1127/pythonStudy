# -*-coding:utf-8-*-
# 装饰器
"""
python中支持特殊语法，在某个函数上方使用：

@函数名
def xx():
    pass

python内部会自动执行，函数(xx)，执行完之后，再将结果赋值给 xx
相当于 xx = 函数名(xx)
"""

# def outer(origin):
#     def inner():
#         print("before")
#         res = origin()
#         print("after")
#         return res
#
#     return inner
#
# @outer
# def func():
#     print("我是func函数")
#     value = (11, 22, 33, 44)
#     return value
#
# result = func()
# print(result)


# 函数有参数
# def outer(origin):
#     def inner(*args, **kwargs):
#         print("before")
#         res = origin(*args, **kwargs)
#         print("after")
#         return res
#     return inner
#
#
# @outer
# def func1(a1):
#     print("我是func1函数")
#     value = (11, 22, 33, 44)
#     return value
#
#
# def func2(a1, a2):
#     print("我是func2函数")
#     value = (11, 22, 33, 44)
#     return value
#
#
# def func3(a1, a2, a3):
#     print("我是func3函数")
#     value = (11, 22, 33, 44)
#     return value
#
#
# func1(11)
# func2(11, a2=22)
# func3(11, 22, 33)
#
# """
# 实现原理：基于@语法和函数闭包，将原函数封装在闭包中，然后将函数赋值为一个新的函数（内层函数），执行函数时再将内层函数中执行闭包中的原函数
# 实现效果：多个函数系统统一，在执行前后自定义一些功能
# 适用场景：多个函数系统统一，在执行前后自定义一些功能
# """
# def outer(origin):
#     def inner(*args, **kwargs):
#         # 执行前
#         res = origin(*args, **kwargs)  # 调用原来的func函数
#         # 执行后
#         return res
#     return inner
#
#
# @outer
# def func(a1, a2):
#     pass
#
#
# func(11, a2=22)

# functools扩展
import functools

def outer(origin):
    functools.wraps(func)
    def inner(*args, **kwargs):
        # 执行前
        res = origin(*args, **kwargs)  # 调用原来的func函数
        # 执行后
        return res
    return inner


@outer
def func(a1, a2):
    pass


func(11, a2=22)
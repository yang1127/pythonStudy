# -*-coding:utf-8-*-

'''
# 基础重试
# 1、重试之间无间隔
from tenacity import retry

@retry
def test_retry():
    print("等待重试，重试无间隔执行...")
    raise Exception

test_retry()
'''

'''
# 2、重试之前等待n秒钟
from tenacity import retry, wait_fixed


@retry(wait = wait_fixed(5))
def test_retry():
    print("等待重试，重试无间隔10s执行...")
    raise Exception


test_retry()
'''

'''
# 设置停止基本条件
# 1、重试n次
from tenacity import retry, stop_after_attempt


@retry(stop=stop_after_attempt(1))
def test_retry():
    print("等待重试，只重试1次...")
    raise Exception


test_retry()
'''

'''
# 2、重试ns不再重试
from tenacity import retry, stop_after_delay


@retry(stop=stop_after_delay(1))
def test_retry():
    print("等待重试，只重试1秒...")
    raise Exception


test_retry()
'''

'''
# 3、重试n次 / 重试ns不再重试 满足任何一种
from tenacity import retry, stop_after_attempt, stop_after_delay


@retry(stop=stop_after_attempt(1) | stop_after_delay(1))
def test_retry():
    print("等待重试，只重试1次 / 只重试1秒...")
    raise Exception


test_retry()
'''

'''
# 设置何时进行重试
# 例如：在出现特定错误/异常（比如请求超时）的情况下，再进行重试
from requests import exceptions
from tenacity import retry, retry_if_exception_type


@retry(retry=retry_if_exception_type(exceptions.Timeout))
def test_retry():
    print("出现超时，重试...")
    raise Exception


test_retry()
'''

'''
# 例如：在满足自定义条件时，再进行重试（当 test_retry 函数返回值为 False 时，再进行重试）
from tenacity import retry, stop_after_attempt, retry_if_result


def is_false(valuse):
    return valuse is False


@retry(stop=stop_after_attempt(3), retry=retry_if_result(is_false))
def test_retry():
    print("当 test_retry 函数返回值为 False 时，再进行3次重试...")
    return False


test_retry()
'''

'''
# 重试后错误重新抛出
# 当出现异常后，tenacity 会进行重试，若重试后还是失败，默认情况下，往上抛出的异常会变成 RetryError，而不是最根本的原因;
# 因此可以加一个参数（reraise=True），使得当重试失败后，往外抛出的异常还是原来的那个

from tenacity import retry, stop_after_attempt


@retry(stop=stop_after_attempt(3), reraise=True)
def test_retry():
    print("等待重试, 试3次，抛出原来的异常...")
    raise Exception


test_retry()
'''

# 设置回调函数
# 当最后一次重试失败后，可以执行一个回调函数

from tenacity import *


def return_last_value(retry_state):
    print("执行回调函数")
    return retry_state.outcome.result()  # 表示返回原函数的返回值


def is_false(value):
    return value is False


@retry(stop=stop_after_attempt(3), retry_error_callback=return_last_value,
       retry=retry_if_result(is_false))
def test_retry():
    print("等待重试中，重试3次...")
    return False


print(test_retry())










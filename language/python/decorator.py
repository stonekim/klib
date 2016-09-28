# -*- coding:utf-8 -*-
import os
import sys

# 这个装饰器 相当于 myfunc=deco(myfunc), 所以只会执行一次
def deco(func):
    print("before myfunc() called.")
    func()
    print("  after myfunc() called.")
    return func

def deco1(func):
    def _deco():
        print("before myfunc() called.")
        func()
        print("  after myfunc() called.")
        # 不需要返回func，实际上应返回原函数的返回值
    return _deco

'''示例6: 对参数数量不确定的函数进行装饰，
参数用(*args, **kwargs)，自动适应变参和命名参数'''
def deco2(func):
    def _deco(*args, **kwargs):
        print("before %s called." % func.__name__)
        ret = func(*args, **kwargs)
        print("  after %s called. result: %s" % (func.__name__, ret))
        return ret
    return _deco

@deco1
def myfunc():
    print(" myfunc() called.")

myfunc()
myfunc()

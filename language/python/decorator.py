# -*- coding:utf-8 -*-
import os
import sys

# ���װ���� �൱�� myfunc=deco(myfunc), ����ֻ��ִ��һ��
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
        # ����Ҫ����func��ʵ����Ӧ����ԭ�����ķ���ֵ
    return _deco

'''ʾ��6: �Բ���������ȷ���ĺ�������װ�Σ�
������(*args, **kwargs)���Զ���Ӧ��κ���������'''
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

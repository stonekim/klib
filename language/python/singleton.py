#!/usr/bin/python
# -*- coding: utf-8 -*

import threading

class Singleton(object):  # pylint: disable=R0903
    """
    Singleton你的类.
    用法如下::

        @Singleton
        class YourClass(object):
            def __init__(self):
            pass
    """
    def __init__(self, cls):
        self.__instance = None
        self.__cls = cls
        self._lock = threading.Lock()

    def __call__(self, *args, **kwargs):
        self._lock.acquire()
        if self.__instance is None:
            self.__instance = self.__cls(*args, **kwargs)
        self._lock.release()
        return self.__instance


@Singleton
class A():
    def __init__(self):
        print 'init from A'


a = A()
a2 = A()

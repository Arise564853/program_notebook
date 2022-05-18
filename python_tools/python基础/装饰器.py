#!/usr/bin/env python
# -*- coding: utf-8 -*-
_author_ = '吴晓南'
from datetime import datetime as dt


def func(msg):
    print("-->>"+msg)


def log(func):
    def wrapper(msg):
        print('['+str(dt.now())+']'+func.__name__)
	return func(msg)
    return wrapper
  # 这样一改， log 就又可以用了，给 func 再加上语法糖：
@log
def func(msg):
	print("-->>"+msg)
	func('hello')


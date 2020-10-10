#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020/10/10 9:47
# @file : 装饰器.py
# @software : PyCharm

def deco(func=None):
    def new():
        print('failed')
    if func:
        print('succeed!')
        return func
    else:
        print('run new()')
        return new

@deco
def test_func():
    print('this is a test function!')

test_func()
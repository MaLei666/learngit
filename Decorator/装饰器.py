#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020/10/10 9:47
# @file : 装饰器.py
# @software : PyCharm

# def deco(func=None):
#     def new():
#         print('failed')
#     if func:
#         print('succeed!')
#         return func
#     else:
#         print('run new()')
#         return new
#
# @deco
# def test_func():
#     print('this is a test function!')
#
# test_func()


import time
def clock(func):
    def son(*args):
        t0 = time.perf_counter()
        res = func(*args)
        els=time.perf_counter()-t0
        name=func.__name__
        args_str=','.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (els, name, args_str, res))
        return res
    return son

@clock
def test(seconds):
    time.sleep(seconds)

@clock
def test2(n):
    return 1 if n<2 else n*test2(n-1)

print('*' * 40, 'Calling snooze(.123)')
test(.123)
print('*' * 40, 'Calling factorial(6)')
print('6! =', test2(6))
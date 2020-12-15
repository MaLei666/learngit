# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020/12/15 10:46
# @file : 12-15.py
# @software : PyCharm

class test(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


# 继承自 dict 的 __init__ 方法显然忽略了我们覆盖的 __setitem__ 方法：'one' 的值没有重复
a = test(one=1)
print(a)
# [] 运算符会调用我们覆盖的 __setitem__ 方法，按预期那样工 作：'two' 对应的是两个重复的值，即 [2, 2]。
a['two'] = 2
print(a)
# 继承自 dict 的 update 方法也不使用我们覆盖的 __setitem__ 方 法：'three' 的值没有重复
a.update(three=3)
print(a)

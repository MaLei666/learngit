# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020/12/15 10:32
# @file : 12-15.py
# @software : PyCharm


# 即便不注册，抽象基类也 能把一个类识别为虚拟子类
class test:
    def __len__(self):
        return 23


from collections import abc

print(issubclass(test, abc.Sized))
print(isinstance(test(), abc.Sized))
print(test.__mro__)

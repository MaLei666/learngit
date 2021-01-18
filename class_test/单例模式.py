#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2021/1/5 10:41 下午
# @file : 单例方法.py
# @software : PyCharm

class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class MyClass(Singleton):
    a = 1

# 创建实例时把所有实例的__dict__指向同一个字典,这样它们具有相同的属性和方法.
class Borg(object):
    _state = {}
    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob

class MyClass2(Borg):
    a = 1


#装饰器版本
def singleton(cls):
    instances = {}
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

@singleton
class MyClass:
    a = 1

for i in [1,1]:
    print(MyClass().a)


# 作为python的模块是天然的单例模式
# # mysingleton.py
# class My_Singleton(object):
#     def foo(self):
#         pass
#
# my_singleton = My_Singleton()
# to use
# from mysingleton import my_singleton
# my_singleton.foo()
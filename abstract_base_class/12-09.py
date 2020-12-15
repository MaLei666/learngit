# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020/12/9 9:55
# @file : 12-09.py
# @software : PyCharm

import abc


# 自己定义的抽象基类要继承 abc.ABC
class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """从可迭代对象中添加元素。"""

    # 声明抽象类方法的推荐方式
    # 与其他方法描述符一起使用时，abstractmethod() 应该放在最里层
    @abc.abstractmethod
    def pick(self):
        """随机删除元素，然后将其返回。
        如果实例为空，这个方法应该抛出`LookupError`。 """

    def loaded(self):
        """如果至少有一个元素，返回`True`，否则返回`False`。"""
        return bool(self.inspect())

    def inspect(self):
        """返回一个有序元组，由当前元素构成。"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


class test(Tombola):
    def pick(self):
        return 10


a = test()

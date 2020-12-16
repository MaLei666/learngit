# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020/12/16 14:56
# @file : 可迭代的对象与迭代器.py
# @software : PyCharm

'''
Python从可迭代的对象中获取迭代器。

可迭代的对象有个 __iter__ 方法，每次都实例化一个新的迭代器；
迭代器要实现 __next__ 方法，返回单个元素，此外还要实现 __iter__ 方法，返回迭代器本身
迭代器可以迭代，但是可迭代的对象不是迭代器
'''

'''
迭代器是这样的对象：
---   实现了无参数的 __next__ 方法，返回序列中的下一个元素；
---   如果没有元素了，那么抛出 StopIteration 异常。 
---   实现了 __iter__ 方法，因此迭代器也可以迭代。
---   因为内置的 iter(...) 函数会对序列做特殊处理
'''

'''
迭代器模式可用来： 
---   访问一个聚合对象的内容而无需暴露它的内部表示 
---   支持对聚合对象的多种遍历 
---   为遍历不同的聚合结构提供一个统一的接口（即支持多态迭代）

为了“支持多种遍历”，必须能从同一个可迭代的实例中获取多个独立的迭代器，
而且各个迭代器要能维护自身的内部状态，
因此这一模式正确的实现方式是，每次调用iter(my_iterable)都新建一个独立的迭代器

可迭代的对象一定不能是自身的迭代器！！！
可迭代的对象 必须实现 __iter__ 方法，但不能实现 __next__ 方法
迭代器应该一直可以迭代。迭代器的 __iter__ 方法应 该返回自身。
'''
from Iterator_and_Generator.iterator import Sentence


# s=Sentence('aaaa abbb')
# a=iter(s)
# while True:
#     try:
#         print(next(a))
#     except StopIteration:
#         print('-' * 50)
#         break

class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


class Sentence2(Sentence):
    # __iter__ 方法实例化并返回一个迭代器
    def __iter__(self):
        return SentenceIterator(self.words)


from collections import abc

s = Sentence('aaaa abbb')
print(issubclass(SentenceIterator, abc.Iterator))

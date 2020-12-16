# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020/12/16 14:19
# @file : base.py
# @software : PyCharm

'''
所有生成器都是迭代器，因为生成器完全实现了迭代器接口。
迭代器用于从集合中取出元素；而生成器用于“凭空”生成元素

迭代器用于支持：
--  for 循环
--  构建和扩展集合类型
--  逐行遍历文本文件
--  列表推导、字典推导和集合推导
--  元组拆包
--  调用函数时，使用 * 拆包实参
'''

import re
import reprlib


class Sentence:
    def __init__(self, text):
        RE_WORD = re.compile('\w+')
        self.text = text
        # 函数返回一个字符串列表，里面的元素是正则表达式的全部非重叠匹配。
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    # 用于生成大型数据结构的简略字符串表示形式。
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)



# s = Sentence('"The time has come," the Walrus said,')
# print(s)
# for i in s:
#     print(i)
# print(list(s))

'''
检查对象x能否迭代，最准确的方法是：调用iter(x)函数，
如果不可迭代，抛出TypeError异常
这比使用isinstance(x,abc.Iterable)更准确，
因为iter(x)函数会考虑到遗留的__getitem__方法，而abc.Iterable类则不考虑
'''
# print(iter(s))
# print(iter(None))

'''
序列可以迭代的原因：   iter函数
解释器需要迭代对象 x 时，会自动调用 iter(x)

内置的 iter 函数有以下作用。 
(1) 检查对象是否实现了 __iter__ 方法，如果实现了就调用它，获取 一个迭代器。 
(2) 如果没有实现 __iter__ 方法，但是实现了 __getitem__ 方法， 
    Python 会创建一个迭代器，尝试按顺序（从索引 0 开始）获取元素。 
(3) 如果尝试失败，Python 抛出 TypeError 异常，
    通常会提示“C object is not iterable”（C 对象不可迭代），其中 C 是目标对象所属的类。

任何 Python 序列都可迭代的原因是，它们都实现了 __getitem__ 方 法。
'''

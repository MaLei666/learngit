# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020/12/16 16:53
# @file : lazy_and_eager.py
# @software : PyCharm


import reprlib
import re

'''
惰性求值（lazy evaluation）和 及早求值（eager evaluation）是编程语言理论方面的技术术语
'''


class Sentence:
    def __init__(self, text):
        self.RE_WORD = re.compile('\w+')
        self.text = text

    # 用于生成大型数据结构的简略字符串表示形式。
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        # 函数返回一个字符串列表，里面的元素是正则表达式的全部非重叠匹配。
        # self.words = RE_WORD.findall(text)

        for i in self.RE_WORD.finditer(self.text):
            yield i.group()


iter=Sentence('a c v dd').__iter__()
for i in iter:
    print(i)
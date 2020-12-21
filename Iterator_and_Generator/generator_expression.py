#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020/12/21 16:37
# @file : generator_expression.py
# @software : PyCharm

import reprlib
import re


'''
生成器表达式是语法糖：完全可以替换成生成器函数，不过有时使用生 成器表达式更便利
'''


class Sentence:
    def __init__(self, text):
        self.RE_WORD = re.compile('\w+')
        self.text = text

    # 用于生成大型数据结构的简略字符串表示形式。
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        # for i in self.RE_WORD.finditer(self.text):
        #     yield i.group()
        return (i.group() for i in self.RE_WORD.finditer(self.text))


a=Sentence('a c v f ff')
print(type(a))
for i in a:
    print(i)
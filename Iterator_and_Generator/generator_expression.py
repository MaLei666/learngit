# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020/12/21 16:37
# @file : generator_expression.py
# @software : PyCharm

import reprlib
import re

'''
生成器表达式是语法糖：完全可以替换成生成器函数，不过有时使用生成器表达式更便利

生成器表达式是创建生成器的简洁句法，这样无需先定义函数再调用
不过，生成器函数灵活得多，可以使用多个语句实现复杂的逻辑，也可以作为协程使用
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
#
#
# a=Sentence('a c v f ff')
# print(type(a))
# for i in a:
#     print(i)
#


'''
典型的迭代器模式作用很简单：遍历数据结构。
不过，即便不是从集合中获取元素，而是获取序列中即时生成的下一个值时，也用得到这种基于方法的标准接口。
'''


class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        # 把 self.begin 赋值给 result，不过会先强制转换成前面的加法算式得到的类型
        print(type(self.begin + self.step))
        result = type(self.begin + self.step)(self.begin)
        # 如果 self.end 属性的值是 None，那么forever的值是True
        forever = self.end is None
        print(forever)
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


# ap = ArithmeticProgression(0, 1, 3)
# print(list(ap))


import itertools
gen=itertools.count(1,2)
# for i in range(10):
#     print(next(gen))

gen2=itertools.takewhile(lambda n:n<10,gen)
for i in gen2:
    print(i)
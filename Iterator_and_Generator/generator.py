# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020/12/16 16:30
# @file : generator.py
# @software : PyCharm

'''
所有生成器都是迭代器，因为生成器完全实现了迭代器接口。

只要Python函数的定义体中有yield关键字，该函数就是生成器函数。
调用生成器函数时，会返回一个生成器对象。
也就是说，生成器函数是生成器工厂。

普通的函数与生成器函数在句法上唯一的区别是，在后者的定义体中有 yield 关键字
'''

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    # 迭代器其实是生成器对象，每次调用 __iter__ 方法都会 自动创建，因为这里的 __iter__ 方法是生成器函数
    def __iter__(self):
        for word in self.words:
            # 产出当前的 word
            yield word
        # 这个 return 语句不是必要的；这个函数可以直接“落空”，自动返 回。
        # 不管有没有 return 语句，生成器函数都不会抛出 StopIteration 异常
        # 而是在生成完全部值之后会直接退出
        return


def gen_123():
    yield 1
    yield 2
    yield 3


print(gen_123)
print(gen_123())
# 生成器函数会创建一个生成器对象，包装生成器函数的定义体
for i in gen_123():
    print(i)
print('*' * 40)

# 把生成器传给next(...)函数时，生成器函数会向前，执行函数定义体中的下一个yield语句，
# 返回产出的值，并在函数定义体的当前位置暂停。
g = gen_123()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# -*- coding:utf-8 -*-
# @author : MaLei
# @datetime : 2020/11/26 14:27
# @file : __init__.py.py
# @software : PyCharm


# a=[1,2,3]
# b=[4,5,6]
# c=[(i,j) for i in a for j in b]
# print(c)


# import collections
#
# Card = collections.namedtuple('Card', ['rank', 'suit'])
#
#
# class FrenchDeck:
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#     suits = 'spades diamonds clubs hearts'.split()
#
#     def __init__(self):
#         self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
#
#     def __len__(self):
#         return len(self._cards)
#
#     def __getitem__(self, position):
#         return self._cards[position]
#
#
# from random import shuffle
#
#
# # 为FrenchDeck 打猴子补丁，把它变成可变的，让 random.shuffle 函数能处理
# def set_card(deck, position, card):
#     # print(position,deck._cards[position],card)
#     deck._cards[position] = card
#
#
# # 这种技术叫猴子补丁：在运行时修改类或模块，而不改动源码。
# # 猴子补丁很强大，但是打补丁的代码与要打补丁的程序耦合十分紧密，而且往往要处理隐藏和没有文档的部分。
# FrenchDeck.__setitem__ = set_card
# deck = FrenchDeck()
# print(deck._cards)
# print('*'*100)
# shuffle(deck)
# print(deck._cards)


import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck2(collections.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):
        self._cards[position] = value

    # 继承 MutableSequence 的类必须实现 __delitem__ 方法，这 是 MutableSequence 类的一个抽象方法
    def __delitem__(self, position):
        del self._cards[position]

    # 还要实现 insert 方法，这是 MutableSequence 类的第三个 抽象方法
    # 即便 FrenchDeck2 类不需要 __delitem__ 和 insert 提供的行 为，也要实现，因为 MutableSequence 抽象基类需要它们
    def insert(self, position, value):
        self._cards.insert(position, value)


FrenchDeck2()

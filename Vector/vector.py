# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020/11/24 16:39
# @file : vector.py
# @software : PyCharm

import reprlib
import math
from array import array


class Vector:
    typecode = 'd'

    def __init__(self, components):
        # self._components 是“受保护的”实例属性，把 Vector 的分量保存 在一个数组中
        self._components = array(self.typecode, components)

    def __iter__(self):
        # 使用 self._components 构建一个迭代器
        return iter(self._components)

    def __repr__(self):
        # reprlib.repr() 函数获取 self._components 的有限长度表 示形式
        components = reprlib.repr(self._components)
        # 把字符串插入 Vector 的构造方法调用之前，去掉前面的 array('d', 和后面的)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        # 使用 self._components 构建 bytes 对象
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        # 不能使用 hypot 方法了，因此我们先计算各分量的平方之和，然后 再使用 sqrt 方法开平方
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        # 直接把 memoryview 传给构造方法，不用像前面那样使用 * 拆包
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

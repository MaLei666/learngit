# -*- coding:utf-8 -*-
# @author : MaLei
# @datetime : 2020/12/16 9:50
# @file : base.py
# @software : PyCharm

# 不能重载内置类型的运算符
# 不能新建运算符，只能重载现有的
# 某些运算符不能重载——is、and、or 和 not（不过位运算符 &、| 和 ~ 可以）

'''
一元运算符
'''
# 按位取反   ~x == -(x+1)
# print(bin(3))
# print(type(3))
# print(~3)
# print(bin(~3))

# x 和 +x 何时不相等
# 1.   如果 x 是 Decimal 实例，在 算术运算的上下文中创建，然后在不同的上下文中计算 +x，那么 x != +x。
# import decimal
# a=decimal.getcontext()
# a.prec=40
# b=decimal.Decimal('1')/decimal.Decimal('3')
# print(b)
# print(+b)
# print(b==+b)
#
# # 每个 +one_third 表达式都会使用 one_third 的值创建一个 新 Decimal 实例
# # 但是会使用当前算术运算上下文的精度。
# a.prec=28
# print(b)
# print(+b)
# print(b==+b)

# 2.  Counter 相加时，负值和零值计数会从结果中剔除。
# 而一元运 算符 + 等同于加上一个空 Counter，因此它产生一个新的 Counter 且仅保留大于零的计数器
# from collections import Counter
#
# a = Counter('aaabbccda')
# print(a)
# a['r'] = -3
# a['e'] = 0
# a['s'] = 3
# print(a)
# print(+a)
# print(a == +a)

'''
重载向量加法运算符 +
'''
from Vector.vector import Vector
import itertools


class Vector2(Vector):
    def __init__(self, components):
        super().__init__(components)

    def __add__(self, other):
        # pairs 是个生成器，它会生成 (a, b) 形式的元组,a 来自 self，b 来自 other。
        # 如果 self 和 other 的长度不同，使用 fillvalue 填充较短的那个可迭代对象
        pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        # __add__ 返回一个新 Vector 实例
        return Vector(a + b for a, b in pairs)


#
#
# v1 = Vector2([1, 2, 3])
# v2 = Vector2([4, 5, 6])
# print(v1 + v2)
# v1 = Vector2([1, 2, 3, 4, 5])
# v2 = Vector2([4, 5, 6])
# print(v1 + v2)
# # 还可以把 Vector 加到元组或任何生成数字的可迭代对象上
# v3 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# print(v1 + v3)
# # 如果对调操作数，混合类型的加法就会失败
# print(v3 + v1)


# 为了支持涉及不同类型的运算，Python为中缀运算符特殊方法提供了特殊的分派机制。
# 对表达式a+b来说，解释器会执行以下几步操作
# (1)如果a有__add__方法，而且返回值不是NotImplemented，调用a.__add__(b)，然后返回结果。
# (2)如果返回值是NotImplemented，检查b有没有__radd__方法
# (3)如果有，而且没有返回NotImplemented，调用b.__radd__(a)，然后返回结果。
# (4)如果没有__radd__方法，或者NotImplemented，抛出TypeError

# (5)如果a没有__add__方法，或者调用__add__方法返回NotImplemented
# (6)检查b有没有__radd__方法，如果有，而且没有返回NotImplemented，调用b.__radd__(a)，然后返回结果。
# (7)如果b没有__radd__方法，或者调用__radd__方法返回NotImplemented
# (8)抛出TypeError，并在错误消息中指明操作数类型不支持。

# __radd__ 是 __add__ 的“反射”（reflected）版本或“反向”（reversed） 版本
class Vector3(Vector2):
    def __radd__(self, other):
        return self + other


#
# v1 = Vector3([1, 2, 3])
# v3 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# print(v3 + v1)

# 如果中缀运算符方法抛出异常，就终止了运算符分派机制。
# 对 TypeError 来说，通常最好将其捕获，然后返回 NotImplemented。
# 这样，解释器会尝试调用反向运算符方法，如果操作数是不同的类型，对调之后，反向运算符方法可能会正确计 算。
class Vector4(Vector3):
    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(a + b for a, b in pairs)
        except TypeError:
            return NotImplemented

    def __radd__(self, other):
        return self + other


#
# v1 = Vector4([1, 2, 3])
# v3 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# print(v3 + v1)

'''
重载标量乘法运算符  *
'''
import numbers
from fractions import Fraction


class Vector5(Vector4):
    def __mul__(self, scalar):
        # 显式检查抽象类型
        if isinstance(scalar, numbers.Real):
            return Vector(n * scalar for n in self)
        else:
            return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar


# v1 = Vector5([1, 2, 3])
# print(v1 * 10)
# print(v1 * Fraction(1, 3))


'''
增量赋值运算符
'''
# 增量赋值不会修改不可变目标，而是新建实例，然后重新绑定
v1 = Vector5([1, 2, 3])
print(id(v1))
v1 += Vector5([2, 3, 4])
print(v1)
# v1重新绑定了新的id实例
print(id(v1))

print(issubclass(Vector5, Vector))

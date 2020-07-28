# #-*-coding:utf-8-*-
#
# import types
#
# class person ():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eat(self):
#         print('eat foot')
#
# #定义一个实例方法
# def run(self,speed):
#     print('%d'%speed)
#
# #定义一个类方法
# @classmethod
# def Class(cls):
#     cls.num=100
#
# #定义一个静态方法
# def Static():
#     print('static')
#
# #创建一个实例对象
# P=person('malei',24)
# print(P.name)
# #给对象添加属性
# P.sex='male'
# print(P.sex)
#
# #给对象添加方法
# P.run=types.MethodType(run,P)
# # 调用实例方法
# P.run(1020)
#
#
# #给类添加类方法
# person.Class=Class
# # 调用类方法
# person.Class()
#
#
#
# #给类添加静态方法
# person.Static=Static
# # 调用静态方法
# person.Static()
#
# L=[x for x in range(5)]
# G=(x for x in range(5))
# print(L)
# for x in L:
#     print(x,end='')
# print('\n')
#
# for x in G:
#     print(x,end='')

# def fib(times):
#     n=0
#     a,b=0,1
#     while n<times:
#         yield b
#         # print(b)
#         a,b = b,a+b   # 先计算等值右边b=1,a+b=1,赋值给a和b
#         n+=1
#     return 'done'
#
# # for x in fib(5):   #这种输出无法输出return返回值
# #     print(x)
# #输出
# g=fib(5)
# while True:
#     try:           #处理异常语句try/except
#         x=next(g)
#         print('%d'%x)
#     except StopIteration as e:
#         print('%s'%e.value)
#         break

# #判断是否可以迭代，即是否为迭代对象
# from collections import Iterable
# print(isinstance((x for x in range(10)), Iterable))
# print(isinstance([],Iterable))
#
# #判断是否为迭代器
# from collections import Iterator
# print(isinstance([],Iterator))
# print(isinstance(iter([]),Iterator))

# import sys
# print(sys.path)








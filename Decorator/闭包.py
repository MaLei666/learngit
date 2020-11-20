#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020/10/10 14:58
# @file : 闭包.py
# @software : PyCharm

# def test():
#     test_list=[]
#     def test_son(value):
#         test_list.append(value)
#         total=sum(test_list)
#         print(test_list)
#         return total/len(test_list)
#     return test_son
#


# def test():
#     count=0
#     total=0
#     def test1(value):
#         #当 count 是数字或任何不可变类型时，我们在 test1 的定义体中为 count 赋值了，这会把 count 变成局部变量。
#         # count += 1
#         # total += value
#         # return total / count
#         nonlocal count,total
#         count += 1
#         total += value
#         return total / count
#     return test1
#
# a=test()
# print(a(10))
# print(a(13))
# print(a(22))
# print(a(21))
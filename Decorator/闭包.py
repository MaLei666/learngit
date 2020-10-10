#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020/10/10 14:58
# @file : 闭包.py
# @software : PyCharm

def test():
    test_list=[]
    def test_son(value):
        test_list.append(value)
        total=sum(test_list)
        print(test_list)
        return total/len(test_list)
    return test_son

a=test()
print(a(10))
print(a(13))
print(a(22))
print(a(21))

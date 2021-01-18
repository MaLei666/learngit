# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2021/1/3 8:07 下午
# @file : 希尔排序.py
# @software : PyCharm

a = [32, 54, 65, 23, 45, 74, 79, 99, 88, 11, 34, 68, 33]


def xier(datas):
    gap = len(a) // 2
    while gap > 0:
        for i in range(gap, len(a)):
            while i > 0:
                if datas[i] < datas[i - gap]:
                    datas[i], datas[i - gap] = datas[i - gap], datas[i]
                    i -= gap
                else:
                    break
        gap //= 2
    return a


print(xier(a))

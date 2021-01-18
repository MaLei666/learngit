#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2021/1/3 9:11 下午
# @file : 选择排序.py
# @software : PyCharm

a = [32, 54, 65, 23, 45, 74, 79, 99, 88, 11, 34, 68, 33]

def xuanze(datas):
    for i in range(len(a)):
        min = i
        for j in range(i+1, len(a)):
            if datas[j] < datas[min]:
                min = j
        datas[i], datas[min] = datas[min], datas[i]
    return datas

print(xuanze(a))
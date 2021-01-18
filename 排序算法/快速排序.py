# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2021/1/3 4:06 下午
# @file : 快速排序.py
# @software : PyCharm

# a=[32,54,65,23,45,74,79,99,88,11,34,68,33]

# def kuaisu(datas,left,right):
#     if left>=right:
#         return 0
#     base=datas[left]
#     i=left
#     j=right
#     while i!=j:
#         if datas[j] > base:
#             j -= 1
#         elif datas[j] < base:
#             datas[j],datas[i]=datas[i],datas[j]
#             i += 1
#         if datas[i] > base:
#             datas[j],datas[i]=datas[i],datas[j]
#             j -= 1
#         elif datas[i] < base:
#             i += 1
#
#     kuaisu(datas, left,i-1)
#     kuaisu(datas, i+1,right)
#     return datas
#
# print(kuaisu(a,0,len(a)-1))


b = [32, 54, 65, 23, 45, 74, 79, 99, 88, 11, 34, 68, 33]


def sort1(datas, left, right):
    if left >= right:
        return 0
    i = left
    j = right
    base = datas[left]
    while i != j:
        if datas[j] > base:
            j -= 1
        elif datas[j] < base:
            datas[i], datas[j] = datas[j], datas[i]
            i += 1
        if datas[i] > base:
            datas[i], datas[j] = datas[j], datas[i]
            j -= 1
        elif datas[i] < base:
            i += 1

    sort1(datas, left, i - 1)
    sort1(datas, i + 1, right)
    return datas


print(sort1(b, 0, len(b) - 1))

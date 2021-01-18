# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2021/1/3 9:52 下午
# @file : 二分查找.py
# @software : PyCharm

a = [1, 2, 3, 4, 5, 6, 7, 8, 10, 12]


# def erfen(datas, k):
#     if len(datas) > 0:
#         mid = len(datas) // 2
#         if datas[mid] < k:
#             return erfen(datas[mid + 1:], k)
#         elif datas[mid] > k:
#             return erfen(datas[:mid], k)
#         else:
#             return True
#     else:
#         return False

def erfen(datas, k):
    lens = len(datas)
    start = 0
    end = lens - 1
    while start <= end:
        mid = (start + end) // 2
        if datas[mid] == k:
            return True
        elif datas[mid] > k:
            end = mid - 1
        else:
            start = mid + 1


print(erfen(a, 4))
print(erfen(a, 1030))

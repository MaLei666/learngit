#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020/12/31 12:45 下午
# @file : test.py
# @software : PyCharm

import copy

# a=[1,2,3,['a']]
# b=copy.deepcopy(a)
# c=copy.copy(a)
# d=a
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))
# a.append(4)
# b.append(5)
# c[3].append('c')
# a[3].append('a')
# print('\n',a,'\n',b,'\n',c,'\n',d)

# print({True:1,False:2}[2>1])

# class a(object):
#     pass
#
# class b(object):
#     pass
#
# class c(a,b):
#     pass
#
# class d(a,b):
#     pass
#
# class e(c,d):
#     pass
#
# print(e.mro())

# def func(s, i, j):
#     if i < j:
#         func(s, i + 1, j - 1)
#         s[i],s[j] = s[j], s[i]
#
# def main():
#     a = [10, 6, 23, -90, 0, 3]
#     func(a, 0, len(a)-1)
#     for i in range(6):
#         print(a[i])
#         print("\n")
# main()


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))



# print(tree)
def mid_travelsal(root):
    row = [root]
    while row:
        row = [kid for item in row for kid in (item.left, item.right) if kid.data==2]
    print(row)
    return row



if __name__ == '__main__':
    mid_travelsal(tree)

#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
# line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
# uname, *fields, homedir, sh = line.split(':')
# print(uname,fields,homedir,sh)
# from collections import defaultdict
# d = defaultdict(list)
# pairs={'a': [1, 2], 'b': [4]}
# for key, value in pairs:
#     d[key].append(value)

# class Pair:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return 'Pair(%r, %r)' % (self.x, self.y)
#     def __str__(self):
#         return '({0.x!s}, {0.y!s})'.format(self)
#
# p=Pair(3, 4).__repr__()
# print(p)
# print('p is {0!r}'.format(p))
# def __repr__(self):
#     return 'Pair(%r, %r)' % (self.x, self.y)

#collections.namedtuple 是一个工厂函数，它可以用来构建一个带 字段名的元组和一个有名字的类
# 创建一个具名元组需要两个参数，一个是类名，另一个是类的各个 字段的名字。
# 后者可以是由数个字符串组成的可迭代对象，或者是由空 格分隔开的字段名组成的字符串
# from collections import namedtuple
# a=namedtuple('test','one two three four five')
# b=namedtuple('test2',('one','two','three','four','five'))
# c=a(1,2,3,4,5)
# print(c)
# d=b(1,2,3,4,5)
# print(d)
# print(d._fields)
# print(d._asdict())


# a=[1,2,3]
# b=[4,5,6]
# c=[7,8,9]
#
# a2=(1,2,3)
# b2=(4,5,6)
# c2=(7,8,9)
#
# a.__iadd__(b)
# d=b.__add__(c)
# print(a,d)
# a.extend(c)
# print(a)
#
# d2=a2.__add__(b2)
# print(d2)
# c.extend(c2)
# print(c)

#错误
# a= [['a','b']*2] * 3
# print(a)
# #列表内的 3 个引用指向同一个对象
# a[1][1]='c'  #三个元素都变了
# print(a,'\n')
#
# #正确
# # 每次迭代中都新建了一个列表，作为新的一行追加到list
# a=[['a','b'] *2 for i in range(3)]
# print(a)
# a[1][1]='c'
# print(a)

# a=['a','1']
# b=['b']
# c=('c')
# d='de'
# a+=b
# print(a)
# a+=c
# print(a)
# a+=d
# print(a)

# a=['a','Ac']
# a.sort(key=len)
# print(a)
# a.sort(key=str.lower,reverse=True)
# print(a)

# import bisect
#
# # HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
# # NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
# # for i in NEEDLES:
# #     a = bisect.bisect(HAYSTACK, i)
# #     print(a)
# a=[60, 70, 80, 90]
# def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
#     i = bisect.bisect(breakpoints, score)
#     return grades[i]
#
# for score in [33, 99, 77, 70, 89, 90, 100]:
#     print(grade(score))
#     bisect.insort(a,score)
# print(a)

from collections import deque
dq=deque(range(10),maxlen=10)
dq.rotate(-5)
print(dq)
dq.rotate(5)
print(dq)
dq.append('a')
print(dq)
dq.extend(['a'])
print(dq)
dq.extendleft(('a','b'))
print(dq)
# dq.append('a')
# print(dq)

# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020/12/22 16:35
# @file : 标准库中的生成器函数.py
# @software : PyCharm

'''
itertools:
'''

'''
用于过滤的生成器函数:

1. compress(it,selector_it)
并行处理两个可迭代的对象；如果selector_it中的元素是真值，产出it中对应的元素
'''

import itertools

# a = [1, 2, 3, 4, 5]
# b = [1, None, 0, [], {}]
# for i in itertools.compress(a, b):
#     print(i)
#
# a = 'test_str'
# b = [1, 0, 1, 0, 0, 1, 1, 1]
# for i in itertools.compress(a, b):
#     print(i)

'''
2. dropwhile(predicate,it)
处理it，跳过predicate的计算结果为真值的元素，然后产出剩下的各个元素（不再进一步检查）
'''
# for i in itertools.dropwhile(lambda n: n.lower() in 'test', 'test_str'):
#     print(i)

'''
3. filter(predicate,it)  内置函数
把it中的各个元素传给predicate，
如果predicate(item)返回真值，那么产出对应的元素；
如果predicate是None，那么只产出真值元素
'''
# print(list(filter(lambda n:n in 'teS','test_str_S')))

'''
4. filterfalse(predicate,it)
与filter函数的作用类似，不过predicate的逻辑是相反的：
predicate返回假值时产出对应的元素
'''
# print(list(itertools.filterfalse(lambda n:n in 'teS','test_str')))

'''

5. takewhile(predicate,it)
predicate返回真值时产出对应的元素，然后立即停止，不再继续检查
'''
# print(list(itertools.takewhile(lambda n: n in 'ter', 'test_str')))

'''
6. islice(it,stop)或islice(it,start,stop,step=1)
产出it的切片，作用类似于s[:stop]或s[start:stop:step]，
不过it可以是任何可迭代的对象，而且这个函数实现的是惰性操作
'''
# print(list(itertools.islice('abcdefg',0,10,2)))
# print(list(itertools.islice([1,2,3,4,5],0,10,2)))

'''
用于映射的生成器函数
itertools

accumulate(it,[func])
产出累积的总和；
如果提供了func，那么把前两个元素传给它，然后把计算结果和下一个元素传给它，以此类推，最后产出结果
'''
# print(list(itertools.accumulate([1,2,3,9],lambda n,t:n+t)))
# print(list(itertools.accumulate([1,2,3,9])))
# print(list(itertools.accumulate([1,2,3,9],min)))
# print(list(itertools.accumulate([1,2,3,9],max)))
# import operator
# print(list(itertools.accumulate([1,2,3,9],operator.mul)))

'''
（内置）enumerate(iterable,start=0)
产出由两个元素组成的元组，结构是(index,item)，
其中index从start开始计数，item则从iterable中获取
'''
# print(list(enumerate([1,2,3])))

'''
（内置）map(func,it1,[it2,...,itN])
把it中的各个元素传给func，产出结果；
如果传入N个可迭代的对象，danli，
而且要并行处理各个可迭代的对象
'''
# print(list(map(lambda n:n*n,[1,2,3])))
# print(list(map(lambda n:n+'——test','abcd')))

'''
starmap(func,it)
把it中的各个元素传给func，产出结果；
输入的可迭代对象应该产出可迭代的元素iit，
然后以func(*iit)这种形式调用func
'''
# print(list(itertools.starmap(lambda n:n+'_123','adecsedwfew')))

'''
用于合并的生成器函数
chain(it1, ..., itN) 
先产出 it1 中的所有元素，然后产出 it2 中的 所有元素，以此类推，无缝连接在一起 

chain.from_iterable(it) 
产出 it 生成的各个可迭代对象中的元素，一个 接一个，无缝连接在一起；
it 应该产出可迭代 的元素，例如可迭代的对象列表 

product(it1, ..., itN, repeat=1) 
计算笛卡儿积：从输入的各个可迭代对象中获 取元素，
合并成由 N 个元素组成的元组，与嵌 套的 for 循环效果一样；
repeat 指明重复处理 多少次输入的可迭代对象 （内置） 

zip(it1, ..., itN) 
并行从输入的各个可迭代对象中获取元素，产 出由 N 个元素组成的元组，
只要有一个可迭代 的对象到头了，就默默地停止

zip_longest(it1, ..., itN, fillvalue=None) 
并行从输入的各个可迭代对象中获取元素，
产 出由 N 个元素组成的元组，等到最长的可迭代 对象到头后才停止，
空缺的值使用 fillvalue 填充
'''
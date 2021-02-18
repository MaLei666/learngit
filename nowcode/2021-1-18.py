# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2021/1/18 7:21 下午
# @file : 2021-1-18.py
# @software : PyCharm

# 写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。

# def EchoInt():
#     flt=input()
#     if float(flt)>0:
#         flt=flt.split('.')
#         if flt[1] >= '5':
#             print(int(flt[0])+1)
#         else:
#             print(flt[0])
#     else:
#         print(0)
#
# EchoInt()

# 输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。
# data=int(input())
# bin_data=bin(data)
# print(bin_data.count('1'))

# 输入一个整数，将这个整数以字符串的形式逆序输出
# 程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001

# a=input()
# print(a[::-1])
# print(''.join(reversed(a)))

# 接受一个只包含小写字母的字符串，然后输出该字符串反转后的字符串。（字符串长度不超过1000）
# a=input()
# print(a[::-1])

# 有这样一道智力题："某商店规定：三个空汽水瓶可以换一瓶汽水。
# 小张手上有十个空汽水瓶，她最多可以换多少瓶汽水喝？"答案是5瓶，

# 方法如下：先用9个空瓶子换3瓶汽水，喝掉3瓶满的，喝完以后4个空瓶子，用3个再换一瓶，
# 喝掉这瓶满的，这时候剩2个空瓶子。然后你让老板先借给你一瓶汽水，喝掉这瓶满的，
# 喝完以后用3个空瓶子换一瓶满的还给老板。如果小张手上有n个空汽水瓶，最多可以换多少瓶汽水喝？
# 1=0
# 2=1
# 3=1
# 4=2
# 5=2
# 6=3
# 7=3
# 8=4
# 9=4
# import sys
# for i in sys.stdin:
#     if int(i)>0:
#         print(int(i) // 2)
#     else:
#         break

# 有一只兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？
# num=0
# def fb(n):
#     if n>2:
#         return fb(n-1)+fb(n-2)
#     else:
#         return 1
#
# print(fb(int(input())))

# while True:
#     n=int(input())
#     a=0
#     b=1
#     for i in range(1,n):
#         res=a+b
#         a=b
#         b=res
#     print(b)
#     break

# 输入一个表达式（用字符串表示），求这个表达式的值。
# 保证字符串中的有效字符包括[‘0’-‘9’],‘+’,‘-’, ‘*’,‘/’ ,‘(’， ‘)’,‘[’, ‘]’,‘{’ ,‘}’。且表达式一定合法。

# a='3+2*{1+2*(-4/(8-6)+7)}'
# a=a.replace('{','(')
# a=a.replace('}',')')
# a=a.replace('[','(')
# a=a.replace(']',')')
# print(eval(a))

# while True:
#     try:
#         a = int(input())
#         count = 0
#         while a:
#             if a & 1:
#                 count += 1
#             a = a >> 1
#         print(count)
#     except:
#         break

# 1010&0001
# # 0101
# # 0010
# # 0001

# import re
#
# while True:
#     try:
#         a = input()
#         a = a.split(' ')
#         cmd = (('reset', 'board', 'board fault'),
#                ('board', 'add', 'where to add'),
#                ('board', 'delete', 'no board at all'),
#                ('reboot', 'backplane', 'impossible'),
#                ('backplane', 'abort', 'install first'))
#         count = 0
#         res = None
#         if len(a) == 1:
#             if re.match(a[0], 'reset'):
#                 res = 'reset what'
#                 count+=1
#         elif len(a) == 2:
#             for i in cmd:
#                 if re.match(a[0], i[0]) and re.match(a[1], i[1]):
#                     count += 1
#                     res = i[2]
#         if count == 1 and res:
#             print(res)
#         else:
#             print('unknown command')
#     except:
#         break

# 根据输入的日期，计算是这一年的第几天。。
# while True:
#     try:
#         year,month,day=[int(i) for i in input().split(' ')]
#         months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         if not year % 4:
#             months[1] = 29
#
#         if 0 < month <= 12 and 0<day<=months[month-1]:
#             days = sum(months[:month - 1]) + day
#             print(days)
#         else:
#             print(-1)
#     except:
#         break

# while True:
#     try:
#         res=[]
#         a=input().split()
#         i=0
#         while i in range(len(a)):
#             if a[i].count('"')==2:
#                 res.append(a[i].replace('"',''))
#                 i+=1
#             elif a[i].count('"')==1:
#                 j=0
#                 data = a[i]
#                 for j in range(i+1,len(a)):
#                     data += (' '+a[j])
#                     if a[j].count('"')!=0:
#                         break
#                 res.append(data.replace('"',''))
#                 i=j+1
#             else:
#                 res.append(a[i])
#                 i+=1
#         print(len(res))
#         for i in res:
#             print(i)
#     except:
#         break

#  给定两个只包含小写字母的字符串，计算两个字符串的最大公共子串的长度。
# 注：子串的定义指一个字符串删掉其部分前缀和后缀（也可以不删）后形成的字符串。
# while True:
#     try:
#         a=input()
#         b=input()
#
#     except:
#         break

#  找出给定字符串中大写字符(即'A'-'Z')的个数。
# while True:
#     try:
#         a = input()
#         count = 0
#         for i in a:
#             if i.isupper():
#                 count += 1
#         print(count)
#     except:
#         break

#  求一个byte数字对应的二进制数字中1的最大连续数

# while True:
#     try:
#         a=int(input())
#         count=0
#         num=[0]
#         while a:
#             if a&1:
#                 count+=1
#             else:
#                 count=0
#             num.append(count)
#             a=a>>1
#         print(max(num))
#     except:
#         break

# 接受一个十六进制的数，输出该数值的十进制表示。
# while True:
#     try:
#         print(int(input(),16))
#     except:
#         break

# 输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
# 最后一个数后面也要有空格
# while True:
#     try:
#         zyz=''
#         a=int(input())
#         for i in range(2,int(a**0.5)+1):
#             while a%i==0:
#                 zyz+=(str(i)+' ')
#                 a/=i
#             if a==1:
#                 break
#         if a>1:
#             zyz += (str(int(a)) + ' ')
#         print(zyz)
#     except:
#         break

# 数据表记录包含表索引和数值（int范围的正整数），请对表索引相同的记录进行合并，
# 即将相同索引的数值进行求和运算，输出按照key值升序进行输出。
# while True:
#     try:
#         dic1={}
#         num = int(input())
#         for i in range(num):
#             b = input().split()
#             if b[0] in dic1:
#                 dic1[b[0]]+=int(b[1])
#             else:
#                 dic1[b[0]]=int(b[1])
#         d=sorted(dic1.items(),key=lambda x:int(x[0]))
#         for j,k in d:
#             print(' '.join([j,str(k)]))
#     except:
#         break

#  输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
# 保证输入的整数最后一位不是0

# while True:
#     try:
#         a=list(input()[::-1])
#         b=list(set(a))
#         b.sort(key=a.index)
#         print(''.join(b))
#     except:
#         break

#  编写一个函数，计算字符串中含有的不同字符的个数。
#  字符在ACSII码范围内(0~127)，换行表示结束符，不算在字符里。不在范围内的不作统计。多个相同的字符只计算一次
# 例如，对于字符串abaca而言，有a、b、c三种不同的字符，因此输出3。

# while True:
#     try:
#         a=iter(input())
#         b=set()
#         for i in a:
#             if 0<=ord(i)<=127:
#                 b.add(i)
#         print(len(b))
#     except:
#         break


# 输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
# while True:
#     try:
#         num=int(input())
#         a=[]
#         for i in range(num):
#             a.append(input())
#         a.sort()
#         for j in a:
#             print(j)
#     except:
#         break

#有4个线程和1个公共的字符数组。
# 线程1的功能就是向数组输出A，
# 线程2的功能就是向字符输出B，
# 线程3的功能就是向数组输出C，
# 线程4的功能就是向数组输出D。
# 要求按顺序向数组赋值ABCDABCDABCD，ABCD的个数由线程函数1的参数指定。
# import threading
# while True:
#     try:
#         a=input()
#         b=[]
#         threading.Thread()


while True:
    try:
        a=input().split(' ')
        b=int(a[0])
        c=int(a[1])
        print (b+c)
    except:
        break
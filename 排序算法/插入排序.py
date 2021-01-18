#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2021/1/3 5:47 下午
# @file : 插入排序.py
# @software : PyCharm

a = [32, 54, 65, 23, 45, 74, 79, 99, 88, 11, 34, 68, 33]
def charu(datas):
    for i in range(1,len(a)):
        for j in range(i-1,-1,-1):
            if datas[i]<datas[j]:
                datas[i],datas[j]=datas[j],datas[i]
                i-=1
            else:
                break
    return a
print(charu(a))

def charu2(datas):
    for i in range(1,len(a)):
        while i >0 :
            if datas[i]<datas[i-1]:
                datas[i],datas[i-1]=datas[i-1],datas[i]
                i-=1
            else:
                break
    return a
print(charu2(a))
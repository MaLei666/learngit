#一个学校，有3个办公室，现在有8位老师等待工位的分配
#encoding=utf-8

import random

# 定义一个列表用来保存3个办公室
offices = [[],[],[]]

# 定义一个列表用来存储8位老师的名字
names = ['A', 'B', 'C','D', 'E', 'F', 'G', 'H']

i = 0
for name in names:
    index = random.randint(0, 2)
    offices[index].append(name)

i = 1
for tempNames in offices:
    print('办公室%d的人数为:%d' % (i, len(tempNames)))
    i += 1
    for name in tempNames:
        print("%s" % name, end='')
    print("\n")
    print("-"*20)


#不定长参数
def fun(a,b,*args,**kwargs):
    print('a =',a)
    print('b =',b)
    print('args',args)
    print('kwargs',kwargs)

    for key,value in kwargs.items():
        print(key,'=',value)


# fun(1,2,3,4,s=6,q=4,w=12)      #传递的参数对应

# c=(3,4)                       #元组和字典的传参方式
# d={'s':6,'q':4,'w':10}
# fun(1,2,*c,**d)

c=(3,4)
d={'s':6,'q':4,'w':10}
fun(1,2,c,d)                     # 元组和字典不加*，显示结果时字典显示在元组里

# # 递归函数
# def cal(num):
#     i=1
#     result=1
#     while i<=num:
#         result*=i
#         i+=1
#     return result
#
# d=cal(5)
# print(d)

# # 匿名函数
# # 1.作为内置函数的参数
# def fun(a,b,opt):
#     print('a=',a)
#     print('b',b)
#     print('result=',opt(a,b))
#
# fun(1,2,lambda x,y:x*y)

# # 2.排序
# stus = [
#     {"name":"zhangsan", "age":18},
#     {"name":"lisi", "age":19},
#     {"name":"wangwu", "age":17}
# ]
# stus.sort(key=lambda x:x['age'])
# print(stus)


# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print('%d*%d=%d\t'%(i,j,i*j),end='')
#         j+=1
#     i+=1
#     print('')


#输出素数
for num in range(100,200):
    if num>1:
        for i in range(2,num):
            if (num%i) ==0:
                break
        else:
            print(num)




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




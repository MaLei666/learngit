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


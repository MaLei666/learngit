#-*-coding:utf-8-*-
# def add(x,y,f):
#     return f(x)+f(y)
#
# print(add(2,-1,abs))


# def ch(x):
#     return x*x
#
# list1=map(ch,[1,2,3,4,5])
# print(list(list1))

def odd_p(n):
    return n%2==1

print(list(filter(odd_p,[1,2,3,4,5,6])))

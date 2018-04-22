#-*-coding:utf-8-*-

#init()方法的调用
# class book:
#     def __init__(self,book1,book2):
#         self.gushi=book1
#         self.sanwen=book2
#
#     def read(self):
#         print('已阅读')
#
#     def __str__(self):
#         msg='已阅读的古诗有：'+self.gushi+'\n已阅读的散文有：'+self.sanwen
#         return msg
#
# paper1=book('古诗十九首','眠空')
# paper2=book('围城','浮生六记')
# # print('%s'%paper1.gushi)
# # print('%s'%paper1.sanwen)
# # print('%s'%paper2.gushi)
# # print('%s'%paper2.sanwen)
# print(paper1)
# print(paper2)

# #烤地瓜
# class potato:
#
#     def __init__(self):
#         self.level=0
#         self.statment='生的'
#         self.tiaoliao=[]
#
#     def __str__(self):
#         msg=self.statment+'地瓜'
#         if len(self.tiaoliao)>0:
#             msg=msg+'('
#             for temp in self.tiaoliao:
#                 msg=msg+temp+','
#             msg=msg.strip(',')
#             msg=msg+')'
#         return msg
#
#     def cook(self,time):
#         self.level+=time
#         if self.level>8:
#             self.statment='烤成灰了'
#         elif self.level>5:
#             self.statment='烤熟了'
#         elif self.level>3:
#             self.statment='半生不熟'
#         else:
#             self.statment='生的'
#
#     def addtiaoliao(self,tiaoliao):
#         self.tiaoliao.append(tiaoliao)
#
# mypotato=potato()
# print(mypotato.level)
# print(mypotato.statment)
# print(mypotato.tiaoliao)
# print("------接下来要进行烤地瓜了-----")
# print("------地瓜经烤了4分钟-----")
# mypotato.cook(4)
# print(mypotato)
# print("------地瓜又经烤了3分钟-----")
# mypotato.cook(3)
# print(mypotato)
# print("------接下来要添加配料-番茄酱------")
# mypotato.addtiaoliao("番茄酱")
# print(mypotato)
# print("------地瓜又经烤了5分钟-----")
# mypotato.cook(5)
# print(mypotato)
# print("------接下来要添加配料-芥末酱------")
# mypotato.addtiaoliao("芥末酱")
# print(mypotato)

#定义狗的种类
class jinmao():
    def fur(self):
        print('金色')

    def age(self):
        print('四个月')

class erha():
    def fur(self):
        print('黑白色')

    def age(self):
        print('两个月')

# #生成具体购买种类对象,使用函数实现
# def buydog(name):
#     if name=='金毛':
#         animal=jinmao()
#     elif name=='二哈':
#         animal=erha()
#
#     return animal

# #定义宠物店
# class animalshop():
#     def order(self,name):
#         animal=buydog(name)
#         return animal

# #定义购买狗的种类，使用类实现
# class buydog():
#     def buy(self,name):
#         if name == '金毛':
#             animal=jinmao()
#         elif name=='二哈':
#             animal=erha()
#         return animal
#
# class animalshop():
#     def __init__(self):
#         self.buydog=buydog()
#
#     def order(self,name):
#         animal=self.buydog.buy(name)
#         return animal



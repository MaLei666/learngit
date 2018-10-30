#-*-coding:utf-8-*-
# class people(object):    #创建一个类为people，people(object)为新式类
#     def __init__(self,name):        #初始化函数，默认设定
#         self.__name=name            #私有属性
#
#     def getName(self):
#         return self.__name
#
#     def setName(self,newName):
#         if len(newName)>=5:
#             self.__name=newName
#         else:
#             print ('长度需大于5')
#     def __del__(self):
#         print ('删除：%s'%self.__name)
#
# xiaoming=people('马磊')    #创建对象并用xiaoming保存引用，马磊作为初始值赋予name
# xiaoming2=people('malei')
# xiaoming.setName('wssdd')   #调用setname函数给对象设置新的名字
# print (xiaoming.getName())  #调用getname函数返回name值给print
# xiaoming2.setName('sdc22')
# print (xiaoming2.getName())
#
# del xiaoming2
# print (xiaoming.getName())
# # print (xiaoming2.getName())

# class father:
#     def __init__(self,name,age=23):
#         self.name=name
#         self.age=age
#
#     def gandie(self):
#         print ('%s的干爹是门口那撮黄土'%self.name)
#
#     def test(self):         #测试子类调用哪个
#         print ('father')
#
# class laofuqin:
#     def test(self):
#         print ('laofuqin')
#
# class son(father,laofuqin):
#     def __init__(self,name,age=23):          #调用父类方法
#         super(son, self).__init__(name,age=23)
#     # def setName(self,newName):
#     #     self.name=newName
#
# yjj=son('马垚垚')
# print (yjj.name)
# print (yjj.age)
# yjj.gandie()
#
# # yjj.setName('叶佳佳')
# # print (yjj.name)
# # yjj.gandie()
#
# # yjj.test()    #子类调用
# # print (son.__mro__)   #可以查看子类的对象搜索方法时的先后顺序

# class People(object):
#     address = '山东' #类属性
#     address2='北京'
#
#     @classmethod                    #类方法
#     def country(cls):
#         return cls.address           #实例属性
#
#     @staticmethod                   #静态方法
#     def country2():
#         return People.address2
#
# p=People()
# print (p.country())
# print (p.country2())


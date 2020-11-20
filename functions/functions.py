# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020/11/20 15:27
# @file : functions.py
# @software : PyCharm\

# 不要使用可变类型作为参数的默认值
class HauntedBus:
    """备受幽灵乘客折磨的校车"""

    # 没有指定初始乘客的 HauntedBus 实例会共享同一个乘客列表
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)
bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)
bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)
bus3 = HauntedBus()
print(bus3.passengers)
bus3.pick('Dave')
print(bus2.passengers)
print(bus2.passengers is bus3.passengers)
print(bus1.passengers)

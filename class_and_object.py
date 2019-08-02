#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-07-30 13:28
# @file : class_and_object.py
# @software : PyCharm

# _formats = {
#     'ymd' : '{d.year}-{d.month}-{d.day}',
#     'mdy' : '{d.month}/{d.day}/{d.year}',
#     'dmy' : '{d.day}/{d.month}/{d.year}'
#     }
# class Date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#     def __format__(self, code):
#         if code == '':
#             code = 'ymd'
#         fmt = _formats[code]
#         return fmt.format(d=self)


# from socket import socket, AF_INET, SOCK_STREAM
# class LazyConnection:
#     def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
#         self.address = address
#         self.family = family
#         self.type = type
#         self.connections = []
#     def __enter__(self):
#         sock = socket(self.family, self.type)
#         sock.connect(self.address)
#         self.connections.append(sock)
#         return sock
#     def __exit__(self, exc_ty, exc_val, tb):
#         self.connections.pop().close()
#
# from functools import partial
# conn = LazyConnection(('www.python.org', 80))
# # Connection closed
# with conn as s:
# # conn.__enter__() executes: connection open
#     s.send(b'GET /index.html HTTP/1.0\r\n')
#     s.send(b'Host: www.python.org\r\n')
#     s.send(b'\r\n')
#     resp = b''.join(iter(partial(s.recv, 8192), b''))

# class Date:
# __slots__ = ['year', 'month', 'day']
# def __init__(self, year, month, day):
#     self.year = year
#     self.month = month
#     self.day = day

# class A:
#     def __init__(self):
#         self._internal = 0 # An internal attribute
#         self.public = 1 # A public attribute
#     def public_method(self):
#         pass
#     def _internal_method(self):
#         pass
#
# class B:
#     def __init__(self):
#         self.__private = 0
#     def __private_method(self):
#         pass
#     def public_method(self):
#         pass
#         self.__private_method()
#
# class C(B):
#     def __init__(self):
#         super().__init__()
#         self.__private = 1 # Does not override B.__private
#         # Does not override B.__private_method()
#     def __private_method(self):
#         pass

# class Person:
#     def __init__(self, first_name):
#         self.first_name = first_name
#     # Getter function
#     @property
#     def first_name(self):
#         return self._first_name
#     # Setter function
#     @first_name.setter
#     def first_name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Expected a string')
#         self._first_name = value
#     # Deleter function (optional)
#     @first_name.deleter
#     def first_name(self):
#         raise AttributeError("Can't delete attribute")
#
# a=Person(1)
# b=a.first_name
#
# print(b)

# class Person:
#     def __init__(self, first_name):
#         self.set_first_name(first_name)
#     # Getter function
#     def get_first_name(self):
#         return self._first_name
#     # Setter function
#     def set_first_name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Expected a string')
#         self._first_name = value
#     # Deleter function (optional)
#     def del_first_name(self):
#         raise AttributeError("Can't delete attribute")
#     # Make a property from existing get/set methods
#     name = property(get_first_name, set_first_name, del_first_name)


# class Proxy:
#     def __init__(self, obj):
#         self._obj = obj
#     # Delegate attribute lookup to internal obj
#     def __getattr__(self, name):
#         return getattr(self._obj, name)
#     # Delegate attribute assignment
#     def __setattr__(self, name, value):
#         if name.startswith('_'):
#             super().__setattr__(name, value) # Call original __setattr__
#         else:
#             setattr(self._obj, name, value)
#
# class A:
#     def __init__(self):
#         self.x = 0
# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.y = 1



# class Person:
#     def __init__(self, name):
#         self.name = name
#     # Getter function
#     @property
#     def name(self):
#         return self._name
#     # Setter function
#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Expected a string')
#         self._name = value
#     # Deleter function
#     @name.deleter
#     def name(self):
#         raise AttributeError("Can't delete attribute")
#
# class SubPerson(Person):
#     @property
#     def name(self):
#         print('Getting name')
#         return super().name
#     @name.setter
#     def name(self, value):
#         print('Setting name to', value)
#         super(SubPerson, SubPerson).name.__set__(self, value)
#     @name.deleter
#     def name(self):
#         print('Deleting name')
#         super(SubPerson, SubPerson).name.__delete__(self)
#
#
# class SubPerson(Person):
#     @Person.name.getter
#     def name(self):
#         print('Getting name')
#         return super().name
#
# class SubPerson(Person):
#     @Person.name.setter
#     def name(self, value):
#         print('Setting name to', value)
#         super(SubPerson, SubPerson).name.__set__(self, value)


class Integer:
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value
    def __delete__(self, instance):
        del instance.__dict__[self.name]

class Point:
    x = Integer('x')
    y = Integer('y')

def __init__(self, x, y):
    self.x = x
    self.y = y

























































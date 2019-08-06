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


# class Integer:
#     def __init__(self, name):
#         self.name = name
#     def __get__(self, instance, cls):
#         if instance is None:
#             return self
#         else:
#             return instance.__dict__[self.name]
#     def __set__(self, instance, value):
#         if not isinstance(value, int):
#             raise TypeError('Expected an int')
#         instance.__dict__[self.name] = value
#     def __delete__(self, instance):
#         del instance.__dict__[self.name]
#
# class Point:
#     x = Integer('x')
#     y = Integer('y')
#
# def __init__(self, x, y):
#     self.x = x
#     self.y = y


# class lazyproperty:
#     def __init__(self, func):
#         self.func = func
#     def __get__(self, instance, cls):
#         if instance is None:
#             return self
#         else:
#             value = self.func(instance)
#             setattr(instance, self.func.__name__, value)
#             return value
#
# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     @lazyproperty
#     def area(self):
#         print('Computing area')
#         return math.pi * self.radius ** 2
#     @lazyproperty
#     def perimeter(self):
#         print('Computing perimeter')
#         return 2 * math.pi * self.radius
#
#
# c = Circle(4.0)
# print(c.radius)
# print(c.area)

# class Structure2:
#     _fields = []
#     def __init__(self, *args, **kwargs):
#         if len(args) > len(self._fields):
#             raise TypeError('Expected {} arguments'.format(len(self._fields)))
#         # Set all of the positional arguments
#         for name, value in zip(self._fields, args):
#             setattr(self, name, value)
#         # Set the remaining keyword arguments
#         for name in self._fields[len(args):]:
#             setattr(self, name, kwargs.pop(name))
#         # Check for any remaining unknown arguments
#         if kwargs:
#             raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))
# # Example use
# if __name__ == '__main__':
#     class Stock(Structure2):
#         _fields = ['name', 'shares', 'price']
#     s1 = Stock('ACME', 50, 91.1)
#     s2 = Stock('ACME', 50, price=91.1)
#     s3 = Stock('ACME', shares=50, price=91.1)
# # s3 = Stock('ACME', shares=50, price=91.1, aa=1)

# from abc import ABCMeta, abstractmethod
# class IStream(metaclass=ABCMeta):
#     @abstractmethod
#     def read(self, maxbytes=-1):
#         pass
#     @abstractmethod
#     def write(self, data):
#         pass
# class SocketStream(IStream):
#     def read(self, maxbytes=-1):
#         pass
#     def write(self, data):
#         pass
#
# import io
# # Register the built-in I/O classes as supporting our interface
# IStream.register(io.IOBase)
# # Open a normal file and type check
# f = open('foo.txt')
# isinstance(f, IStream) # Returns True
#
# class A(metaclass=ABCMeta):
#     @property
#     @abstractmethod
#     def name(self):
#         pass
#
#     @name.setter
#     @abstractmethod
#     def name(self, value):
#         pass
#
#     @classmethod
#     @abstractmethod
#     def method1(cls):
#         pass
#
#     @staticmethod
#     @abstractmethod
#     def method2():
#         pass

# Base class. Uses a descriptor to set a value
class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
#
# # Descriptor for enforcing types
# class Typed(Descriptor):
#     expected_type = type(None)
#     def __set__(self, instance, value):
#         if not isinstance(value, self.expected_type):
#             raise TypeError('expected ' + str(self.expected_type))
#         super().__set__(instance, value)
#
# # Descriptor for enforcing values
# class Unsigned(Descriptor):
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError('Expected >= 0')
#         super().__set__(instance, value)
#
# class MaxSized(Descriptor):
#     def __init__(self, name=None, **opts):
#         if 'size' not in opts:
#             raise TypeError('missing size option')
#         super().__init__(name, **opts)
#
#     def __set__(self, instance, value):
#         if len(value) >= self.size:
#             raise ValueError('size must be < ' + str(self.size))
#         super().__set__(instance, value)
#
# class Integer(Typed):
#     expected_type = int
#
# class UnsignedInteger(Integer, Unsigned):
#     pass
#
# class Float(Typed):
#     expected_type = float
#
# class UnsignedFloat(Float, Unsigned):
#     pass
#
# class String(Typed):
#     expected_type = str
#
# class SizedString(String, MaxSized):
#     pass
#
# class Stock:
#     # Specify constraints
#     name = SizedString('name', size=8)
#     shares = UnsignedInteger('shares')
#     price = UnsignedFloat('price')
#     def __init__(self, name, shares, price):
#         self.name = name
#         self.shares = shares
#         self.price = price


# Decorator for applying type checking
# def Typed(expected_type, cls=None):
#     if cls is None:
#         return lambda cls: Typed(expected_type, cls)
#     super_set = cls.__set__
#     def __set__(self, instance, value):
#         if not isinstance(value, expected_type):
#             raise TypeError('expected ' + str(expected_type))
#         super_set(self, instance, value)
#     cls.__set__ = __set__
#     return cls
#
# # Decorator for unsigned values
# def Unsigned(cls):
#     super_set = cls.__set__
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError('Expected >= 0')
#         super_set(self, instance, value)
#     cls.__set__ = __set__
#     return cls
#
# # Decorator for allowing sized values
# def MaxSized(cls):
#     super_init = cls.__init__
#     def __init__(self, name=None, **opts):
#         if 'size' not in opts:
#             raise TypeError('missing size option')
#         super_init(self, name, **opts)
#     cls.__init__ = __init__
#     super_set = cls.__set__
#
#     def __set__(self, instance, value):
#         if len(value) >= self.size:
#             raise ValueError('size must be < ' + str(self.size))
#         super_set(self, instance, value)
#     cls.__set__ = __set__
#     return cls
#
# # Specialized descriptors
# @Typed(int)
# class Integer(Descriptor):
#     pass
#
# @Unsigned
# class UnsignedInteger(Integer):
#     pass
#
# @Typed(float)
# class Float(Descriptor):
#     pass
#
# @Unsigned
# class UnsignedFloat(Float):
#     pass
#
# @Typed(str)
# class String(Descriptor):
#     pass
#
# @MaxSized
# class SizedString(String):
#     pass

# import collections
# class A(collections.Iterable):
#     pass
#

# class A:
# def spam(self, x):
# pass
# def foo(self):
# pass

# class A:
#     def spam(self, x):
#         pass
#     def foo(self):
#         pass
#
# class B2:
#     """ 使用__getattr__ 的代理，代理方法比较多时候"""
#     def __init__(self):
#         self._a = A()
#     def bar(self):
#         pass
#     # Expose all of the methods defined on class A
#     def __getattr__(self, name):
#         """ 这个方法在访问的attribute 不存在的时候被调用
#         the __getattr__() method is actually a fallback method
#         that only gets called when an attribute is not found"""
#         return getattr(self._a, name)

# class Date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#
# d = Date.__new__(Date)

# class Connection1:
#     """ 新方案——对每个状态定义一个类"""
#     def __init__(self):
#         self.new_state(ClosedConnectionState)
#
#     def new_state(self, newstate):
#         self._state = newstate
#
#     # Delegate to the state class
#     def read(self):
#         return self._state.read(self)
#
#     def write(self, data):
#         return self._state.write(self, data)
#
#     def open(self):
#         return self._state.open(self)
#
#     def close(self):
#         return self._state.close(self)
#
#     # Connection state base class
# class ConnectionState:
#     @staticmethod
#     def read(conn):
#         raise NotImplementedError()
#
#     @staticmethod
#     def write(conn, data):
#         raise NotImplementedError()
#
#     @staticmethod
#     def open(conn):
#         raise NotImplementedError()
#
#     @staticmethod
#     def close(conn):
#         raise NotImplementedError()
#
#     # Implementation of different states
# class ClosedConnectionState(ConnectionState):
#     @staticmethod
#     def read(conn):
#         raise RuntimeError('Not open')
#
#     @staticmethod
#     def write(conn, data):
#         raise RuntimeError('Not open')
#
#     @staticmethod
#     def open(conn):
#         conn.new_state(OpenConnectionState)
#
#     @staticmethod
#     def close(conn):
#         raise RuntimeError('Already closed')
#
# class OpenConnectionState(ConnectionState):
#     @staticmethod
#     def read(conn):
#         print('reading')
#
#     @staticmethod
#     def write(conn, data):
#         print('writing')
#
#     @staticmethod
#     def open(conn):
#         raise RuntimeError('Already open')
#
#     @staticmethod
#     def close(conn):
#         conn.new_state(ClosedConnectionState)

# d = getattr(p, 'distance')(0, 0) # Calls p.distance(0, 0)
# import operator
# operator.methodcaller('distance', 0, 0)(p)
# points = [
#     Point(1, 2),
#     Point(3, 0),
#     Point(10, -3),
#     Point(-5, -7),
#     Point(-1, 8),
#     Point(3, 2)
#     ]
# #Sort by distance from origin (0, 0)
# points.sort(key=operator.methodcaller('distance', 0, 0))




import weakref
class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
    def get_spam(self, name):
        if name not in self._cache:
            temp = Spam._new(name) # Modified creation
            self._cache[name] = temp
        else:
            temp = self._cache[name]
        return temp
    def clear(self):
        self._cache.clear()
class Spam:
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Can't instantiate directly")
    # Alternate constructor
    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name
        return self































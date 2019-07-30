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

class A:
    def __init__(self):
        self._internal = 0 # An internal attribute
        self.public = 1 # A public attribute
    def public_method(self):
        pass
    def _internal_method(self):
        pass

class B:
    def __init__(self):
        self.__private = 0
    def __private_method(self):
        pass
    def public_method(self):
        pass
        self.__private_method()

class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1 # Does not override B.__private
        # Does not override B.__private_method()
    def __private_method(self):
        pass


























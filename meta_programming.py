#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-08-06 11:58
# @file : meta_programming.py
# @software : PyCharm


# import time
# from functools import wraps
# def timethis(func):
#     '''
#     Decorator that reports the execution time.
#     '''
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(func.__name__, end-start)
#         return result
#     return wrapper
# @timethis
# def countdown(n):
#     while n > 0:
#         n -= 1
#
# countdown(100000)

# from functools import wraps
# import logging
# def logged(level, name=None, message=None):
#     """
#     Add logging to a function. level is the logging
#     level, name is the logger name, and message is the
#     log message. If name and message aren't specified,
#     they default to the function's module and name.
#     """
#     def decorate(func):
#         logname = name if name else func.__module__
#         log = logging.getLogger(logname)
#         logmsg = message if message else func.__name__
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             log.log(level, logmsg)
#             return func(*args, **kwargs)
#         return wrapper
#     return decorate
#
# # Example use
# @logged(logging.DEBUG)
# def add(x, y):
#     return x + y
#
# @logged(logging.CRITICAL, 'example')
# def spam():
#     print('Spam!')

# from functools import wraps, partial
# import logging
# # Utility decorator to attach a function as an attribute of obj
# def attach_wrapper(obj, func=None):
#     if func is None:
#         return partial(attach_wrapper, obj)
#     setattr(obj, func.__name__, func)
#     return func
#
# def logged(level, name=None, message=None):
#     '''
#     Add logging to a function. level is the logging
#     level, name is the logger name, and message is the
#     log message. If name and message aren't specified,
#     they default to the function's module and name.
#     '''
#     def decorate(func):
#         logname = name if name else func.__module__
#         log = logging.getLogger(logname)
#         logmsg = message if message else func.__name__
#
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             log.log(level, logmsg)
#             return func(*args, **kwargs)
#
#         # Attach setter functions
#         @attach_wrapper(wrapper)
#         def set_level(newlevel):
#             nonlocal level
#             level = newlevel
#
#         @attach_wrapper(wrapper)
#         def set_message(newmsg):
#             nonlocal logmsg
#             logmsg = newmsg
#         return wrapper
#     return decorate
#
# # Example use
# @logged(logging.DEBUG)
# def add(x, y):
#     return x + y
#
# def spam():
#     print('Spam!')

# from functools import wraps, partial
# import logging
# def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
#     if func is None:
#         return partial(logged, level=level, name=name, message=message)
#     logname = name if name else func.__module__
#     log = logging.getLogger(logname)
#     logmsg = message if message else func.__name__
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         log.log(level, logmsg)
#         return func(*args, **kwargs)
#     return wrapper
# # Example use
# @logged
# def add(x, y):
#     return x + y
# @logged(level=logging.CRITICAL, name='example')
# def spam():
#     print('Spam!')

import ast
class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loaded = set()
        self.stored = set()
        self.deleted = set()
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.loaded.add(node.id)
        elif isinstance(node.ctx, ast.Store):
            self.stored.add(node.id)
        elif isinstance(node.ctx, ast.Del):
            self.deleted.add(node.id)
# Sample usage
if __name__ == '__main__':
    # Some Python code
    code = '''
for i in range(10):
    print(i)
    del i
    '''
    # Parse into an AST
    top = ast.parse(code, mode='exec')
    # Feed the AST to analyze name usage
    c = CodeAnalyzer()
    c.visit(top)
    print('Loaded:', c.loaded)
    print('Stored:', c.stored)
    print('Deleted:', c.deleted)





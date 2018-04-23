#-*-coding:utf-8-*-

import re
a=re.match(r'^\d{3}\-\d{3,8}$','010-1234555')
print(a)
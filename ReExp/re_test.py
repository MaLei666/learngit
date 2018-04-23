#-*-coding:utf-8-*-

import re
# a=re.match(r'^\d{3}\-\d{3,8}$','010-1234555')
# print(a)
#
# b=re.split(r'[\s\,\;]+','a,b;;;d  z zc')
# print (b)
#
# c=re.match(r'^(\d{3})\-(\d{3,8})$','010-666666')
# print(c.group(2))

#编译
# re_num=re.compile(r'^(\d+?)(6*)$')
# print(re_num.match('010662666').groups())

# c=re.match(r'^(\d+?)(6*)$','010662666')
# #print(c.groups())

#练习
def is_valid_email(addr):

    re_addr=re.compile(r'^(\w+)(\@)(\w+)\.\w{3}$')

    if re_addr.match(addr)==None:
        print('not a valid addr')
    else:
        print('ok',re_addr.match(addr).group(1))



is_valid_email('<Tom Paris> tom@voyager.org')

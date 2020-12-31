# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020/11/21 10:30 上午
# @file : 20-11-21.py
# @software : PyCharm

import re

def check_lines(files,re_str):
    with open(files,'a+') as f:
        f.seek(0)
        lines=f.readlines()
        for each in lines:
            if re.match(re_str,each):
                return False
        f.write(re_str + '\n')
    return True

pa = r'General_LeChange-(android|iOS)_Chn_IS_V([1-9].([1-9][0-9]?).000.[R|T].' \
     r'([0-1][0-9][0-9][0-9]|[2][0][0-1][0-9])([0][1-9]|[1][0-2])([0-2]?[1-9]|[1-3][0-1]).(apk|ipa))'
f = open('data.txt', 'r')
for row in f.readlines():
    if row[-1] == '\n':
        row = row[:-1]
        if re.match(pa, row):
            if row.endswith('apk'):
                status=check_lines('android.txt',row)
            else:
                status = check_lines('iOS.txt', row)
        else:
            status = check_lines('invalid.txt', row)

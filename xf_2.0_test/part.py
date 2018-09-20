# #!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
# #-*- coding:utf-8 -*-
# # @author : MaLei
# # @datetime : 2018-09-12 15:04
# # @file : part.py
# # @software : PyCharm
#
# def part(partstat):
#     # 上传建筑消防设施部件运行状态
#     partstat = partstat[2:4] + partstat[0:2]  # 部件状态转为2进制
#     partstat = bin(int(partstat, 16))[2:].rjust(16, '0')  # 不足16位前面补0
#     # 二进制切片显示各bit对应状态
#     powerfail = partstat[7:8]
#     delayed = partstat[8:9]
#     feedback = partstat[9:10]
#     startstat = partstat[10:11]
#     monitor = partstat[11:12]
#     shield = partstat[12:13]
#     breakdown = partstat[13:14]
#     firestat = partstat[14:15]
#     playstat = partstat[15:16]
#
#     if firestat == ('0'):
#         pass
#     else:
#         print('火警', end=' ')
#     if breakdown == ('0'):
#         pass
#     else:
#         print('故障', end=' ')
#     if playstat == ('0'):
#         pass
#     else:
#         print('正常运行状态', end=' ')
#     if powerfail == ('0'):
#         pass
#     else:
#         print('电源故障', end=' ')
#     if delayed == ('0'):
#         pass
#     else:
#         print('延时状态', end=' ')
#     if feedback == ('0'):
#         pass
#     else:
#         print('反馈', end=' ')
#     if startstat == ('0'):
#         pass
#     else:
#         print('启动', end=' ')
#     if monitor == ('0'):
#         pass
#     else:
#         print('监管', end=' ')
#     if shield == ('0'):
#         pass
#     else:
#         print('屏蔽')
#
# part(input('输入部件状态： '))

import re

while True:
    pattern = re.compile('.{1,2}')
    str=input('数据：')
    print(' '.join(pattern.findall(str)))
    while KeyboardInterrupt:
        break


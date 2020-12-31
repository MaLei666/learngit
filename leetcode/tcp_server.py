# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020/11/21 11:32 上午
# @file : tcp_server.py
# @software : PyCharm

from socket import *
from datetime import datetime

# # #单进程服务器
tcpsersocket = socket(AF_INET, SOCK_STREAM)
tcpsersocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
bindaddr = ('127.0.0.1', 8081)
tcpsersocket.bind(bindaddr)
tcpsersocket.listen(5)
while True:
    newsocket, cliaddr = tcpsersocket.accept()
    try:
        while True:
            recvdata = newsocket.recv(1024)
            if recvdata:
                # bytes转string
                recvdata = recvdata.decode()
                print(recvdata)
                # 判断有没有T
                if len(recvdata.split('T')) > 1:
                    recvdata = recvdata.replace('T', ' ')
                    # 转为时间格式
                    time_str = datetime.strptime(recvdata, '%Y-%m-%d %H:%M:%S')
                    if time_str > datetime.now():
                        newsocket.send(bytes('时间晚于当前时间', encoding='utf-8'))
                    else:
                        # week返回的是0-6代表周一到周天，在返回上加一
                        week = time_str.weekday() + 1
                        days = (datetime.now() - time_str).days
                        newsocket.send(bytes('星期{},距离当前还有{}天'.format(week, days), encoding='utf-8'))
                else:
                    newsocket.send(bytes('时间格式不正确', encoding='utf-8'))
            else:
                break
    finally:
        newsocket.close()

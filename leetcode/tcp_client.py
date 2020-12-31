# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2020/11/21 11:32 上午
# @file : tcp_client.py
# @software : PyCharm

from socket import *

tcpclisocket = socket(AF_INET, SOCK_STREAM)
tcpseraddr = ('127.0.0.1', 8081)
tcpclisocket.connect(tcpseraddr)
senddata = input('输入：')
tcpclisocket.send(bytes(senddata, encoding='utf8'))
recvdata = tcpclisocket.recv(1024).decode()
print('接收：', recvdata)
tcpclisocket.close()

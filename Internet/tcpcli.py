# -*- coding: utf-8 -*-
from socket import *
tcpclisocket=socket(AF_INET,SOCK_STREAM)
tcpseraddr=('192.168.0.203',8001)
tcpclisocket.connect(tcpseraddr)
senddata=input('输入：')
tcpclisocket.send(bytes(senddata,encoding='utf8'))

recvdata=tcpclisocket.recv(1024)
print('接收：',recvdata)

tcpclisocket.close()
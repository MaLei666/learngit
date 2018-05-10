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

# connum=input('输入连接服务器的次数：')
# for i in range(int(connum)):
#     tcpclisocket=socket(AF_INET,SOCK_STREAM)
#     cliaddr=('192.168.43.51',8001)
#     tcpclisocket.connect(cliaddr)
#     print(i)


#-*-coding:utf-8-*-
from socket import *
connum=input('输入连接服务器的次数：')
for i in range(int(connum)):
    tcpclisocket=socket(AF_INET,SOCK_STREAM)
    cliaddr=('192.168.43.51',8001)
    tcpclisocket.connect(cliaddr)
    print(i)

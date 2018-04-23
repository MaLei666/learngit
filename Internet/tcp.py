# -*- coding: utf-8 -*-

# #tcpclient
# from socket import *
# tcpsersocket=socket(AF_INET,SOCK_STREAM)
# tcpseraddr=('192.168.0.203',8001)
# tcpsersocket.bind(tcpseraddr)   #绑定tcpserver的ip和端口
# tcpsersocket.listen(5)          #listem将socket变为被动，接收连接
# while True:                     #循环接收来自client的连接
#     newsocket, clientaddr = tcpsersocket.accept()   #新的客户端连接服务器，则对应产生一个新的socket
#     print(clientaddr)
#     recvdata = newsocket.recv(1024)    #接收对方数据并打印
#     print(recvdata)
#     msg='received'
#     newsocket.send(msg.encode('utf-8'))   #收到client信息后返回一条信息
#     newsocket.close()                     #关闭client的socket，不再为这个client服务
#
# tcpsersocket.close()

#tcpserver
from socket import *
tcpclisocket=socket(AF_INET,SOCK_STREAM)
cliaddr=('192.168.0.203',8001)
tcpclisocket.connect(cliaddr)           #连接服务器
while True:
    senddata = input('输入：')
    tcpclisocket.send(bytes(senddata, encoding='utf8'))
    recvdata = tcpclisocket.recv(1024)
    print('接收', recvdata)
tcpclisocket.close()

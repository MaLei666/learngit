<<<<<<< HEAD
# -*- coding: utf-8 -*-

# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

from socket import *
#from time import ctime
udpsocket=socket(AF_INET,SOCK_DGRAM)
bindaddr=('192.168.0.203',8005)  # 本地服务器ip和端口
udpsocket.bind(bindaddr)  #服务器端绑定端口
udpaddr=('192.168.0.203',8080)

while True:
    recvdata = udpsocket.recvfrom(1024)   #接收数据
    udpsocket.sendto(recvdata[0],recvdata[1])   #将接收数据发送回去显示
    print('您的小粉丝:%s'%(recvdata[0]))         #打印接收数据
    senddata=input('高冷美少女：')                #键盘接收数据
    udpsocket.sendto(bytes(senddata,encoding='utf8'),udpaddr)   #将键盘接收数据发送
udpsocket.close()




# sendaddr=('192.168.0.203',8001)
# senddata=input('输入：')
# udpsocket.sendto(bytes(senddata, encoding = "utf8"),sendaddr)


=======
#-*-coding:utf-8-*-
from socket import *
udpsocket=socket(AF_INET,SOCK_DGRAM)
bindaddr=('192.168.43.51',8001)
udpsocket.bind(bindaddr)
udpaddr=('192.168.43.51',8080)

while True:
    udpdata = input('输入：')
    udpsocket.sendto(bytes(udpdata, encoding="utf8"), udpaddr)
    recvdata=udpsocket.recvfrom(1024)
    print('接收:',recvdata)
    udpsocket.sendto(recvdata[0],recvdata[1])
udpsocket.close()


>>>>>>> a12530e6a5567d7db75cb1c5aef536f10befce0b

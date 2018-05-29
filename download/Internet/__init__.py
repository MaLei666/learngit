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



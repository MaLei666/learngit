# -*- coding: utf-8 -*-

from socket import *
from time import sleep
from threading import Thread

#处理客户端请求和数据
def clideal(newsocket,cliaddr):
    while True:
        recvdata=newsocket.recv(1024)
        if len(recvdata)>0:
            print(str(cliaddr),recvdata)
        else:
            print('close...')
            break
    newsocket.close()


def main():
    tcpsersocket=socket(AF_INET,SOCK_STREAM)
    tcpsersocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    tcpseraddr=('192.168.0.203',8001)
    tcpsersocket.bind(tcpseraddr)
    tcpsersocket.listen(2)

    try:   #try-finally 语句无论是否发生异常都将执行最后的代码。
        while True:
            print('main processing...')
            newsocket,cliaddr=tcpsersocket.accept()
            print('new processing to handle %s'%str(cliaddr))
            client=Thread(target=clideal,args=(newsocket,cliaddr))  #创建新的线程处理客户端数据
            client.start()

    finally:
        tcpsersocket.close()

if __name__ == '__main__':
    main()


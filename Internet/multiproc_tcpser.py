# -*- coding: utf-8 -*-
from socket import *
from multiprocessing import *
#处理客户端请求并处理数据
def cildeal(newsocket,cliaddr):
    while True:
        recvdata=newsocket.recv(1024)
        if len(recvdata)>0:
            print(str(cliaddr),recvdata)
        else:
            print('close...',cliaddr)
            break
    newsocket.close()

def main():
    tcpsersocket=socket(AF_INET,SOCK_STREAM)
    tcpsersocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    tcpseraddr=('192.168.0.203',8001)
    tcpsersocket.bind(tcpseraddr)
    tcpsersocket.listen(1)

    try:
        while True:
            print('main process...')
            newsocket,cliaddr=tcpsersocket.accept()
            print('build new process to handle:%s'%str(cliaddr))
            client=Process(target=cildeal,args=(newsocket,cliaddr))
            client.start()
            newsocket.close()
    finally:
        tcpsersocket.close()

if __name__ == '__main__':
    main()
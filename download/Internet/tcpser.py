#-*-coding:utf-8-*-
from socket import *
from multiprocessing import *
from time import sleep

# #单进程服务器
# tcpsersocket=socket(AF_INET,SOCK_STREAM)
# tcpsersocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# bindaddr=('192.168.43.51',8001)
# tcpsersocket.bind(bindaddr)
# tcpsersocket.listen(5)
# while True:
#     print('waiting...')
#     newsocket,cliaddr=tcpsersocket.accept()
#     print('%s data handle...'%str(cliaddr))
#     try:
#         while True:
#             recvdata=newsocket.recv(1024)
#             if len(recvdata)>0:
#                 print(str(cliaddr),recvdata)
#             else:
#                 print('closed...')
#             break
#     finally:
#         newsocket.close()
# tcpsersocket.close()

#多进程服务器
#处理客户端请求并服务
def dealcli(newsocket,cliaddr):
    while True:
        recvdata=newsocket.recv(1024)
        if len(recvdata)>0:
            print(recvdata)
        else:
            print('close...')
    newsocket.close()


def main():
    tcpsersocket=socket(AF_INET,SOCK_STREAM)
    tcpsersocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    tcpaddr=('192.168.43.51',8001)
    tcpsersocket.bind(tcpaddr)
    tcpsersocket.listen(5)

    try:
        while True:
            print('waiting...')
            newsocket,cliaddr=tcpsersocket.accept()
            print('data handle',cliaddr)
            client=Process(target=dealcli,args=(newsocket,cliaddr))
            client.start()
            newsocket.close()
    finally:
        tcpsersocket.close()

if __name__=='__main__':
    main()





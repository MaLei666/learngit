#-*-coding:utf-8-*-
from socket import *
from multiprocessing import *
from time import sleep
from datetime import datetime
# # #单进程服务器
tcpsersocket=socket(AF_INET,SOCK_STREAM)
tcpsersocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
bindaddr=('127.0.0.1',8081)
tcpsersocket.bind(bindaddr)
tcpsersocket.listen(5)
while True:
    newsocket,cliaddr=tcpsersocket.accept()
    try:
        while True:
            recvdata=newsocket.recv(1024)
            if recvdata:
                recvdata=recvdata.decode()
                if len(recvdata.split('T'))>1:
                    recvdata=recvdata.replace('T',' ')
                    time_str=datetime.strptime(recvdata,'%Y-%m-%d %H:%M:%S')
                    if time_str>datetime.now():
                        newsocket.send(bytes('时间晚于当前时间',encoding='utf-8'))
                    else:
                        week=time_str.weekday()+1
                        days=(datetime.now()-time_str).days
                        newsocket.send(bytes('星期{},距离当前还有{}天'.format(week,days),encoding='utf-8'))
                else:
                    newsocket.send(bytes('时间格式不正确',encoding='utf-8'))
                print(recvdata)
            else:
                print('closed...')
            break
    finally:
        newsocket.close()

#多进程服务器
#处理客户端请求并服务
# def dealcli(newsocket,cliaddr):
#     while True:
#         recvdata=newsocket.recv(1024)
#         if len(recvdata)>0:
#             print(recvdata)
#         else:
#             print('close...')
#     newsocket.close()
#
#


# def main():
#     tcpsersocket=socket(AF_INET,SOCK_STREAM)
#     tcpsersocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#     tcpaddr=('127.0.0.1',8081)
#     tcpsersocket.bind(tcpaddr)
#     tcpsersocket.listen(5)
#
#     try:
#         while True:
#             print('waiting...')
#             newsocket,cliaddr=tcpsersocket.accept()
#             print('data handle',cliaddr)
#             client=Process(target=dealcli,args=(newsocket,cliaddr))
#             client.start()
#             newsocket.close()
#     finally:
#         tcpsersocket.close()
#
# if __name__=='__main__':
#     main()





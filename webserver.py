#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-09-20 15:15
# @file : webserver.py
# @software : PyCharm


import errno
import socket
import threading
import time
EOLl = b'\n\n'
EOL2 = b' \n\r\n '
body ='''Hello , world ! <hl> from the5fire <Dj ango 企业开发实战》＜／ hl>  from {thread_name } '''
response_params = [
    ' HTTP/l. 0 200 OK ',
    'Date : Sun, 27 may 2018 01:01 : 01 GMT ' ,
    'Content - Type : text / plain; charset=utf-8 ',
    ' Content Length : {length} \r\n',
    body]
response = ' \r\n '.join(response_params)
def handle_connection(conn , addr):
    print(conn, addr)
    time.sleep ( 60) # 可以自行尝试打开注释,设置睡眠时间
    request = b""
    while EOLl not in request and EOL2 not in request :
        request += conn.recv(1024)  #注意设置为非阻塞模式时这里会报错,
    print ( request)
    current_thread = threading.currentThread()
    content_length = len(body.format(thread_name=current_thread.name).encode())
    print(current_thread.name)
    conn.send(response.format(thread_name=current_thread.name ,
    length=content_length).encode())
    conn.close ()
def main() :
    # socket.AF_ INET 用于服务器与服务器之间的网络通信
    # so c ket.SOCK_ STREAM 用于基于TCP 的流式socket 通信
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设立将n可复用,保证我们每次按Ctrl+C 组合键之后, 快速支启
    serversocket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
    serversocket.bind (('0.0.0.0',8000))
    # 可参考： h t tps : I I stackoverflow. comic扭estions/2444459/python-sock-listen
    serversocket.listen(10)
    print ('http://192.168.1.108:8000')
    serversocket.setblocking(0) #设置socket 为非阻塞模式

    try:
        i=0
        while True:
            try :
                conn, address= serversocket.accept()
            except socket.error as e :
                if e.args [0] != errno.EAGAIN :
                    raise
                continue
            i += 1
            print (i)
            t = threading.Thread(target=handle_connection, args=(conn, address),name = 'thread-%s' % i)
            t.start()
    finally:
        serversocket.close()
if __name__ == '__main__':

    main()


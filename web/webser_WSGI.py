# #-*-coding:utf-8-*-
# from socket import *
# from multiprocessing import Process
#
# def handlecli(clisocket):
#     recvdata=clisocket.recv(2046)
#     requestheadline=recvdata.splitlines()
#     for line in requestheadline:
#         print(line)
#
#     responseheadline='HTTP/1.1 200 OK/r/n'
#     responseheadline+='/r/n'
#     responsebody='hello world'
#
#     response=(responseheadline+responsebody)
#     clisocket.send(response)
#     clisocket.close()
#
#
# def main():
#     sersocket=socket(AF_INET,SOCK_STREAM)
#     sersocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#     seraddr=('',8001)
#     sersocket.bind(seraddr)
#     sersocket.listen(10)
#     while True:
#         clisocket,cliaddr=sersocket.accept()
#         clipro=Process(target=handlecli,args=(clisocket,))
#         clipro.start()
#         clisocket.close()
#
# if __name__ == '__main__':
#     main()

from wsgiref.simple_server import make_server   #内置一个WSGI服务器
#http处理函数
def applicat(environ,response):
    #environ为包含所有http请求信息的dict对象，response为一个发送http响应的函数
    #调用response，发送http响应的header，header只能发送一次
    #response函数接收两个参数，一个是http响应码，一个是一组list表示的HTTP header，每个header用一个包含两个str的tuple表示
    response('200 OK',[('Content-Type','text/html')])
    #body值返回给浏览器
    body= '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    #print(environ)
    # print(environ['PATH_INFO'])
    return [body.encode('utf-8')]
#创建一个服务器，IP，端口和处理函数
httpd = make_server('', 8001, applicat)
print('开始监听8001：')
#开始监听HTTP请求
httpd.serve_forever()
# -*- coding: utf-8 -*-


from socket import *
from time import sleep
from threading import Thread

from socket import *
from threading import Thread
import binascii


#处理客户端请求和数据
def clideal(newsocket,cliaddr):
    while True:

        recvdata=newsocket.recv(1024)
        if len(recvdata)>0:
            print(str(cliaddr),recvdata)

        recvdata=binascii.b2a_hex((newsocket.recv(1024)))
        print(recvdata)
        # print('连接', str(cliaddr))             # '\n',' '.join(pattern.findall(recvdata)))
                                                #pattern=re.compile('.{1,2}')
        if len(recvdata)>0:
            #切片
            startSign=recvdata[0:4]   #启动符2
            sernum=recvdata[4:24]       #流水号2，版本号2，时间标签6    10
            oriaddr=recvdata[24:36]     #源地址6
            desaddr=recvdata[36:48]     #目的地址6
            datalen=recvdata[48:52]     #应用单元数据长度2
            combyte=recvdata[52:54]     #命令字节1
            usedata=recvdata[54:-6]     #应用单元数据
            enddata=recvdata[-4:]
            redatalen=bytes('0000'.encode('utf-8'))
            recombyte=bytes('03'.encode('utf-8'))
            #校验数据
            sumdata=sernum+desaddr+oriaddr+redatalen+recombyte
            checksum=bytes(uchar_checksum(sumdata).encode('utf-8'))
            #print('校验和',checksum)

            # 返回值
            sendhex=binascii.a2b_hex(startSign+sumdata+checksum+enddata)
            print('返回',sendhex)
            newsocket.send(sendhex)

        else:
            print('close...')
            break
    newsocket.close()


def uchar_checksum(data, byteorder='little'):

    length = len(data)
    checksum = 0
    for i in range(0, length,2):
        num1=data[i:i+1]
        num2=data[i+1:i+2]
        highnum = int.from_bytes(num1,byteorder,signed=False)
        highnum=int(chr(highnum).encode('utf-8'),16)        #16进制转为10进制
        lownum=int.from_bytes(num2,byteorder,signed=False)
        lownum = int(chr(lownum).encode('utf-8'),16)
        Sum=highnum*16+lownum
        checksum=checksum+Sum

    checksum=hex(checksum)
    checksum=checksum[-2:]
    return checksum


def main():
    tcpsersocket=socket(AF_INET,SOCK_STREAM)
    tcpsersocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    tcpseraddr=('',8001)
    tcpsersocket.bind(tcpseraddr)
    tcpsersocket.listen(2)
    try:   #try-finally 语句无论是否发生异常都将执行最后的代码。
        while True:
            newsocket,cliaddr=tcpsersocket.accept()
            client=Thread(target=clideal,args=(newsocket,cliaddr))  #创建新的线程处理客户端数据
            client.start()

    finally:
        tcpsersocket.close()

if __name__ == '__main__':
    main()


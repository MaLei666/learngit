# -*- coding: utf-8 -*-
from socket import *
from threading import Thread
import binascii
import re

#处理客户端请求和数据
def clideal(newsocket,cliaddr):
    while True:
        recvdata=binascii.b2a_hex((newsocket.recv(1024)))  #客户端接收数据

        if len(recvdata)>0:
            #切片
            startSign=recvdata[0:4]     #启动符2
            sernum=recvdata[4:24]       #流水号2，版本号2，时间标签6    10
            oriaddr=recvdata[24:36]     #源地址6
            desaddr=recvdata[36:48]     #目的地址6
            datalen=recvdata[48:52]     #应用单元数据长度2
            combyte=recvdata[52:54]     #命令字节1
            usedata=recvdata[54:-6]     #应用数据单元
            enddata=recvdata[-4:]       #结束符
            redatalen=bytes('0000'.encode('utf-8'))  #应答包里应用数据单元长度
            recombyte=bytes('03'.encode('utf-8'))    #应答包命令字节

            pattern = re.compile('.{1,2}')
            print(str(cliaddr), end='  ')  # 加空格显示客户端地址和ID
            idnumshow(oriaddr)
            print('接收:', ' '.join(pattern.findall(str(recvdata))))

            #调用typeinfo函数显示上传数据类型和信息
            typeinfo(usedata)    #应用数据单元

            #校验和计算
            sumdata=sernum+desaddr+oriaddr+redatalen+recombyte  #需要计算校验和的数据
            checksum=bytes(uchar_checksum(sumdata).encode('utf-8'))
            #print('校验和',checksum)

            # 返回应答数据包
            sendhex=binascii.a2b_hex(startSign+sumdata+checksum+enddata)
            newsocket.send(sendhex)
            #print('应答',' '.join(pattern.findall(str(binascii.b2a_hex(sendhex)))))
            #print(type(sendhex))

        else:
            print('close...')
            break
    newsocket.close()

#校验和计算函数
def uchar_checksum(data, byteorder='little'):

    length = len(data)
    checksum = 0
    for i in range(0, length,2):
        num1=data[i:i+1]
        num2=data[i+1:i+2]
        highnum = int.from_bytes(num1,byteorder,signed=False) #读取高位字节转为int型
        highnum=int(chr(highnum).encode('utf-8'),16)        #int转为16进制
        lownum=int.from_bytes(num2,byteorder,signed=False)
        lownum = int(chr(lownum).encode('utf-8'),16)
        Sum=highnum*16+lownum                           #高低位运算得出十进制
        checksum=checksum+Sum
    checksum=hex(checksum)                      #十进制转为16进制
    checksum=checksum[-2:]                      #切片显示后两位校验和
    return checksum

def idnumshow(idnum):
    ID=idnum[10:12]+idnum[8:10]+idnum[6:8]+idnum[4:6]+idnum[2:4]+idnum[0:2]
    print('传输装置ID:',int(ID,16))

#显示应用数据单元中数据类型和信息函数
def typeinfo(data):
    #print(data)
    if len(data)>0:
        #切片
        classType=data[0:2]     # 类型标志 1
        #print(classType)
        typenum=data[2:4]       # 信息对象数目  1
        infoobj=data[4:]        # 信息对象
        #print(infoobj)
        #判断信息对象数目是否为1
        if typenum==bytes('01'.encode('utf-8')):
            # 根据类型标志判断信息是哪一类，分别显示
            # 上传版本号
            if classType==bytes('19'.encode('utf-8')):
                mainnum=infoobj[0:2]                        #主版本号
                secnum=infoobj[2:4]                         #次版本号
                print('上传版本号信息：主版本号%s，次版本号%s'%(mainnum,secnum))

            # 上传部件运行状态
            elif classType==bytes('02'.encode('utf-8')):
                print('上传部件运行状态：',end='')
                systype=infoobj[0:2]                        #系统类型
                sysaddr=infoobj[2:4]                        #系统地址
                parttype=infoobj[4:6]                       #部件类型
                partaddr=infoobj[6:14]                      #部件地址
                partstat=infoobj[14:18]                     #部件状态
                partdesc=infoobj[18:80]                     #部件说明
                timenum=infoobj[80:92]                      #状态发生时间

                # 系统类型分类显示
                if systype==bytes('00'.encode('utf-8')):
                    print('通用',end=' ')
                elif systype==bytes('01'.encode('utf-8')):
                    print('火灾报警系统',end=' ')
                elif systype==bytes('ob'.encode('utf-8')):
                    print('消火栓系统',end=' ')
                else:
                    print('未知系统',end=' ')

                # 部件类型分类显示
                if parttype==bytes('00'.encode('utf-8')):
                    print('通用',end=' ')
                elif parttype==bytes('01'.encode('utf-8')):
                    print('火灾报警控制器',end=' ')
                elif parttype==bytes('17'.encode('utf-8')):
                    print('手报',end=' ')
                elif parttype==bytes('28'.encode('utf-8')):
                    print('烟感',end=' ')
                elif parttype==bytes('18'.encode('utf-8')):
                    print('消火栓按钮',end=' ')
                else:
                    print('未知部件',end=' ')

                #部件状态显示
                partstat=partstat[2:4]+partstat[0:2]   #部件状态转为2进制
                partstat=bin(int(partstat,16))[2:].rjust(16,'0')  #不足16位前面补0
                #二进制切片显示各bit对应状态
                powerfail=partstat[7:8]
                delayed=partstat[8:9]
                feedback=partstat[9:10]
                startstat=partstat[10:11]
                monitor=partstat[11:12]
                shield=partstat[12:13]
                breakdown=partstat[13:14]
                firestat=partstat[14:15]
                playstat=partstat[15:16]

                if firestat==('0'):
                    print('', end=' ')
                else:
                    print('火警',end=' ')
                if breakdown==('0'):
                    print('', end=' ')
                else:
                    print('故障',end=' ')
                if playstat==('0'):
                    print('', end=' ')
                else:
                    print('正常运行状态', end=' ')
                if powerfail==('0'):
                    print('', end=' ')
                else:
                    print('电源故障',end=' ')

                if delayed==('0'):
                    print('', end=' ')
                else:
                    print('延时状态',end=' ')

                if feedback==('0'):
                    print('', end=' ')
                else:
                    print('反馈',end=' ')

                if startstat==('0'):
                    print('', end=' ')
                else:
                    print('启动',end=' ')

                if monitor==('0'):
                    print('', end=' ')
                else:
                    print('监管',end=' ')

                if shield==('0'):
                    print('', end=' ')
                else:
                    print('屏蔽',end='     ')

                #部件状态发生时间
                timeshow(timenum)

            # 上传传输装置运行状态
            elif classType==bytes('15'.encode('utf-8')):
                print('上传传输装置运行状态：',end='')
                status=infoobj[0:2]         #状态
                timenum=infoobj[2:]         #时间
                status=bin(int(status,16))[2:].rjust(8,'0')
                #运行状态数据结构
                linefault=status[1:2]
                comufault=status[2:3]
                bat2fault=status[3:4]
                bat1fault=status[4:5]
                fault=status[5:6]
                firestat=status[6:7]
                playstat=status[7:8]

                if playstat==('0'):
                    print('',end=' ')
                else:
                    print('正常运行状态',end=' ')
                if firestat==('0'):
                    print('',end=' ')
                else:
                    print('火警',end=' ')
                if fault==('0'):
                    print('',end=' ')
                else:
                    print('故障',end=' ')
                if linefault==('0'):
                    print('',end=' ')
                else:
                    print('链路故障',end=' ')
                if comufault==('0'):
                    print('',end=' ')
                else:
                    print('通信故障',end=' ')
                if bat2fault==('0'):
                    print('',end=' ')
                else:
                    print('备电故障',end=' ')
                if bat1fault==('0'):
                    print('',end=' ')
                else:
                    print('主电故障',end=' ')

                # 装置状态发生时间
                timeshow(timenum)

            #上传传输装置操作信息
            elif classType == bytes('18'.encode('utf-8')):
                print('上传传输装置操作信息：', end='')
                handinfo=infoobj[0:2]
                timenum=infoobj[4:]
                handinfo=bin(int(handinfo,16))[2:].rjust(8,'0')
                #操作信息数据结构
                testhandle=handinfo[1:2]
                reinquire=handinfo[2:3]
                checkself=handinfo[3:4]
                elifire=handinfo[4:5]
                handfire=handinfo[5:6]
                elisound=handinfo[6:7]
                reset=handinfo[7:]
                if testhandle==('0'):
                    print('',end=' ')
                else:
                    print('测试',end=' ')
                if reinquire==('0'):
                    print('',end=' ')
                else:
                    print('查岗应答',end=' ')
                if checkself==('0'):
                    print('',end=' ')
                else:
                    print('自检',end=' ')
                if elifire==('0'):
                    print('',end=' ')
                else:
                    print('警情消除',end=' ')
                if handfire==('0'):
                    print('',end=' ')
                else:
                    print('手动报警',end=' ')
                if elisound==('0'):
                    print('',end=' ')
                else:
                    print('消音',end=' ')
                if reset==('0'):
                    print('',end=' ')
                else:
                    print('复位',end=' ')
                # 操作发生时间
                timeshow(timenum)

        else:
            print('多个信息体')
    else:
        print('应用数据单元为空')

def timeshow(time):
    sencond = str(int(time[0:2], 16)).rjust(2, '0')
    minute = str(int(time[2:4], 16)).rjust(2, '0')
    hour = str(int(time[4:6], 16)).rjust(2, '0')
    day = str(int(time[6:8], 16)).rjust(2, '0')
    month = str(int(time[8:10], 16)).rjust(2, '0')
    year = '20' + str(int(time[10:12], 16)).rjust(2, '0')
    print('[', year, '年', month, '月', day, '日', ' ', hour, ':', minute, ':', sencond, ']')

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
    main()# -*- coding: utf-8 -*-





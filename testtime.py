# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep,time
from bs4 import BeautifulSoup
from socket import *
from datetime import datetime
import re,binascii

class flattest():

    def time_tip(self):
        now_time = datetime.now()
        time_str = datetime.strftime(now_time, '%S%M%H%d%m%g')
        self.time_hex = ''
        for i in range(0, len(time_str), 2):
            tip = hex(int(time_str[i:i + 2]))[2:].rjust(2, '0')
            self.time_hex += tip
        return self.time_hex

    def hzbj(self):
        print('''
        1.上传建筑消防设施系统状态
        2.上传部件运行状态
        3.上传传输装置运行状态
        4.上传传输装置操作信息
        5.手录（自动计算校验和）
        ''')
        info_type=input('选择发送信息类型：')
        self.info = ''
        self.usedatalen = ''
        self.device_type = ''
        if info_type=='1':
            self.device_type='01'
            self.usedatalen = '0C00'
            self.info0= '0101'#系统类型1，系统地址1
            self.info='0081'  #系统状态
            self.info2=''
        elif info_type=='2':
            self.device_type = '02'
            self.usedatalen = '3000'
            self.info0='01011704000101'#系统类型，地址，部件类型，地址
            self.info='0280' # 部件状态
            self.info2='EFFF56FF50C082419053C1CB000886310020A7730008D87300088631002000'  #部件说明
        elif info_type=='3':
            self.device_type='15'
            self.usedatalen = '0900'
            self.info0=''
            self.info = '41'
            self.info2=''
        elif info_type=='4':
            self.device_type='18'
            self.usedatalen = '0A00'
            self.info0=''
            self.info = '04'
            self.info2='00'
        elif info_type=='5':
            print('''
            1.上传建筑消防设施系统状态
            2.上传部件运行状态
            3.上传传输装置运行状态
            4.上传传输装置操作信息
            5.其他
                           ''')
            self.infotp=input('选择发送的信息类型：')
            self.part_status()
        self.data_deal()

    def part_status(self):
        def system(sysstat):
            # 系统状态显示
            sysstat = sysstat[2:4] + sysstat[0:2]  # 部件状态转为2进制
            sysstat = bin(int(sysstat, 16))[2:].rjust(16, '0')  # 不足16位前面补0
            # 二进制切片显示各bit对应状态
            reset=sysstat[2:3]
            set=sysstat[3:4]
            status=sysstat[4:5]
            line=sysstat[5:6]
            powerfail2=sysstat[6:7]
            powerfail = sysstat[7:8]
            delayed = sysstat[8:9]
            feedback = sysstat[9:10]
            startstat = sysstat[10:11]
            monitor = sysstat[11:12]
            shield = sysstat[12:13]
            breakdown = sysstat[13:14]
            firestat = sysstat[14:15]
            playstat = sysstat[15:16]

            if firestat == ('0'):
                pass
            else:
                print('火警', end=' ')
            if breakdown == ('0'):
                pass
            else:
                print('故障', end=' ')
            if playstat == ('0'):
                pass
            else:
                print('正常运行状态', end=' ')
            if powerfail == ('0'):
                pass
            else:
                print('主电故障', end=' ')
            if powerfail2 == ('0'):
                pass
            else:
                print('备电故障', end=' ')
            if delayed == ('0'):
                pass
            else:
                print('延时状态', end=' ')
            if feedback == ('0'):
                pass
            else:
                print('反馈', end=' ')
            if startstat == ('0'):
                pass
            else:
                print('启动', end=' ')
            if monitor == ('0'):
                pass
            else:
                print('监管', end=' ')
            if shield == ('0'):
                pass
            else:
                print('屏蔽',end=' ')
            if reset=='0':
                pass
            else:
                print('复位',end=' ')
            if set=='0':
                pass
            else:
                print('配置改变',end=' ')
            if status=='0':
                pass
            else:
                print('手动状态',end=' ')
            if line=='0':
                pass
            else:
                print('总线故障')

        def part(partstat):
            # 部件状态显示
            partstat = partstat[2:4] + partstat[0:2]  # 部件状态转为2进制
            partstat = bin(int(partstat, 16))[2:].rjust(16, '0')  # 不足16位前面补0
            # 二进制切片显示各bit对应状态
            powerfail = partstat[7:8]
            delayed = partstat[8:9]
            feedback = partstat[9:10]
            startstat = partstat[10:11]
            monitor = partstat[11:12]
            shield = partstat[12:13]
            breakdown = partstat[13:14]
            firestat = partstat[14:15]
            playstat = partstat[15:16]

            if firestat == ('0'):
                pass
            else:
                print('火警', end=' ')
            if breakdown == ('0'):
                pass
            else:
                print('故障', end=' ')
            if playstat == ('0'):
                pass
            else:
                print('正常运行状态', end=' ')
            if powerfail == ('0'):
                pass
            else:
                print('电源故障', end=' ')
            if delayed == ('0'):
                pass
            else:
                print('延时状态', end=' ')
            if feedback == ('0'):
                pass
            else:
                print('反馈', end=' ')

            if startstat == ('0'):
                pass
            else:
                print('启动', end=' ')
            if monitor == ('0'):
                pass
            else:
                print('监管', end=' ')
            if shield == ('0'):
                pass
            else:
                print('屏蔽')

        def runstatus(status):
            status = bin(int(status, 16))[2:].rjust(8, '0')
            # 运行状态数据结构
            linefault = status[1:2]
            comufault = status[2:3]
            bat2fault = status[3:4]
            bat1fault = status[4:5]
            fault = status[5:6]
            firestat = status[6:7]
            playstat = status[7:8]

            if playstat == ('0'):
                pass
            else:
                print('正常运行状态', end=' ')
            if firestat == ('0'):
                pass
            else:
                print('火警', end=' ')
            if fault == ('0'):
                pass
            else:
                print('故障', end=' ')
            if linefault == ('0'):
                pass
            else:
                print('链路故障', end=' ')
            if comufault == ('0'):
                pass
            else:
                print('通信故障', end=' ')
            if bat2fault == ('0'):
                pass
            else:
                print('备电故障', end=' ')
            if bat1fault == ('0'):
                pass
            else:
                print('主电故障')

        def useinfo(handinfo):
            handinfo = bin(int(handinfo, 16))[2:].rjust(8, '0')
            # 操作信息数据结构
            testhandle = handinfo[1:2]
            reinquire = handinfo[2:3]
            checkself = handinfo[3:4]
            elifire = handinfo[4:5]
            handfire = handinfo[5:6]
            elisound = handinfo[6:7]
            reset = handinfo[7:]
            if testhandle == ('0'):
                pass
            else:
                print('测试', end=' ')
            if reinquire == ('0'):
                pass
            else:
                print('查岗应答', end=' ')
            if checkself == ('0'):
                pass
            else:
                print('自检', end=' ')
            if elifire == ('0'):
                pass
            else:
                print('警情消除', end=' ')
            if handfire == ('0'):
                pass
            else:
                print('手动报警', end=' ')
            if elisound == ('0'):
                pass
            else:
                print('消音', end=' ')
            if reset == ('0'):
                pass
            else:
                print('复位')

        partstatus = input('输入状态信息：')
        if self.infotp=='1':
            self.device_type='01'
            self.usedatalen = '0C00'
            self.info0 = '0101'  # 系统类型1，系统地址1
            self.info=partstatus
            self.info2=''
            system(partstatus)
        elif self.infotp=='2':
            self.device_type='02'
            self.usedatalen = '3000'
            self.info0 = '01011704000101'  # 系统类型，地址，部件类型，地址
            self.info=partstatus
            self.info2='EFFF56FF50C082419053C1CB000886310020A7730008D87300088631002000'  #部件说明
            part(partstatus)
        elif self.infotp == '3':
            self.device_type='15'
            self.usedatalen = '0900'
            self.info0=''
            self.info=partstatus
            self.info2=''
            runstatus(partstatus)
        elif self.infotp=='4':
            self.device_type='18'
            self.usedatalen = '0A00'
            self.info0 = ''
            self.info=partstatus
            self.info2='00'
            useinfo(partstatus)
        elif self.infotp=='5':
            all_data=input('输入整条数据')
            check_data=all_data.replace(' ','')[4:-6]
            checknum=self.uchar_checksum(check_data)
            self.senddata='4040'+check_data+checknum+'2323'
            # print(self.senddata)
            # self.part_status()
            self.tcpcli()

    def data_deal(self):
        self.startSign = '4040'  # 启动符2、  2
        version = 'BB000001'  #流水号2、版本号2   4
        sendtime = self.time_tip()  # =时间标签6
        oriaddr = '010000000000'  # 源地址6
        desaddr = '000000000000'  # 目的地址6
        self.typetip = self.device_type  # 类型标志1
        datalen = self.usedatalen  # 应用单元数据长度2
        combyte = '02' # 命令字节1
        infonum = '01'  #信息对象数目
        infobody=self.info0+self.info+self.info2+self.time_tip() # 信息体
        # print(infobody,datalen)

        check_data=version+sendtime+oriaddr+desaddr+datalen+combyte+self.typetip+infonum+infobody
        # print('校验数据:', ' '.join(pattern.findall(self.check_data)))

        self.checknum = self.uchar_checksum(check_data).rjust(2,'0')  # 校验和
        self.enddata = '2323'  # 结束符

        self.senddata=self.startSign+check_data+self.checknum+self.enddata
        # print((self.senddata))
        self.tcpcli()

    # 校验和计算函数
    def uchar_checksum(self,check_data):
        length = len(check_data)
        checksum = 0
        for i in range(0, length, 2):
            num1 = int(check_data[i:i + 2],16)
            checksum += num1
        checksum=hex(checksum)[-2:]
        # print(checksum)
        return checksum



    def tcpcli(self):
        tcpclisocket = socket(AF_INET, SOCK_STREAM)
        # tcpseraddr = ('47.92.90.52', 8001)
        tcpseraddr = ('192.168.0.144', 8001)
        tcpclisocket.connect(tcpseraddr)
        pattern = re.compile('.{1,2}')
        print('发送数据:', ' '.join(pattern.findall(self.senddata)))
        # print(type(self.senddata))
        tcpclisocket.send(bytearray.fromhex(self.senddata))
        recvdata = binascii.b2a_hex(tcpclisocket.recv(1024))
        print('接收:', ' '.join(pattern.findall(str(recvdata))))

        choose=input('是否继续发送？y/n： ')
        if choose=='n':
            pass
        elif choose=='y':
            sys=input('是否换子系统？y/n： ')
            if sys=='n':
                self.hzbj()
            # else:
            #     self.xitong()


        tcpclisocket.close()

ceshi=flattest()

ceshi.hzbj()






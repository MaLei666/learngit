# -*- coding: utf-8 -*-
from datetime import datetime
import re
from socket import *
import binascii


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
        self.device_type=''
        type=input('选择发送信息类型：')
        if type=='1':
            self.device_type='01'
        elif type=='2':
            self.device_type='02'
        elif type=='3':
            self.device_type='15'
        elif type=='4':
            self.device_type='18'
        elif type=='5':
            self.device_type=input('数据：')
        return self.device_type

    def data_deal(self):
        def info_body():
            infoall=''
            usedatalen=''
            if typetip == '02':
                usedatalen='3000'
                info = '010117040001010280EFFF56FF50C082419053C1CB000886310020A7730008D87300088631002000'
                timetip = self.time_tip()
                infoall = info + timetip
            elif typetip == '15':
                usedatalen='0900'
                info = '41'
                timetip = self.time_hex
                infoall = info + timetip
            elif typetip == '18':
                usedatalen='0A00'
                info = '0400'
                timetip = self.time_hex
                infoall = info + timetip
            return usedatalen,infoall


        self.startSign = '4040'  # 启动符2、  2
        version = 'BB000001'  #流水号2、版本号2   4
        sendtime = self.time_tip()  # =时间标签6
        oriaddr = '010000000000'  # 源地址6
        desaddr = '000000000000'  # 目的地址6
        typetip = self.hzbj()  # 类型标志1
        datalen = info_body()[0]  # 应用单元数据长度2
        combyte = '02' # 命令字节1
        infonum = '01'  #信息对象数目
        infobody=info_body()[1] # 信息体
        # print(infobody,datalen)

        self.pattern = re.compile('.{1,2}')
        self.check_data=version+sendtime+oriaddr+desaddr+datalen+combyte+typetip+infonum+infobody
        # print('校验数据:', ' '.join(pattern.findall(self.check_data)))

        self.checknum = self.uchar_checksum()  # 校验和
        self.enddata = '2323'  # 结束符

        self.senddata=self.startSign+self.check_data+self.checknum+self.enddata
        # print((self.senddata))
        print('发送数据:', ' '.join(self.pattern.findall(self.senddata)))


    # 校验和计算函数
    def uchar_checksum(self):
        length = len(self.check_data)
        checksum = 0
        for i in range(0, length, 2):
            num1 = int(self.check_data[i:i + 2],16)
            checksum += num1
        checksum=hex(checksum)[-2:]
        # print(checksum)
        return checksum

    def tcpcli(self):
        tcpclisocket = socket(AF_INET, SOCK_STREAM)
        tcpseraddr = ('47.92.90.52', 8001)
        tcpclisocket.connect(tcpseraddr)

        tcpclisocket.send(bytearray.fromhex(self.senddata))
        recvdata = binascii.b2a_hex(tcpclisocket.recv(1024))
        print('接收:', ' '.join(self.pattern.findall(str(recvdata))))

        tcpclisocket.close()

ceshi=flattest()
ceshi.data_deal()
ceshi.tcpcli()



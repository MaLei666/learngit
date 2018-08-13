# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep,time
from bs4 import BeautifulSoup
from socket import *
from datetime import datetime
import re,binascii

class flattest():
    def __init__(self):
        # 模拟登陆云平台，
        options = webdriver.FirefoxOptions()
        options.add_argument(
            'user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
        self.browser = webdriver.Firefox(firefox_options=options)
        URL = 'http://xiaofang.safecity119.com/'
        self.browser.get(URL)
        self.browser.maximize_window()  # 把打开的浏览器最大化

    def login(self,name):
        # 登录
        elem1 = self.browser.find_element_by_name('UName')
        elem2 = self.browser.find_element_by_name('PWord')
        elem1.send_keys(name)
        elem2.send_keys('111111')
        elem1.send_keys(Keys.RETURN)
        sleep(3)

    def choose_flat(self,):
        print('''
              1. 北京云平台
              2. 玉林云平台
              3. 丽江云平台
              4. 嘉禾国信大厦
              5. 玉林市第一人民医院
             ''' )
        flat=input('要登录的平台：')
        if flat=='1':
            self.name='bjzkadmin'
        elif flat=='2':
            self.name='ylxfadmin'
        elif flat=='3':
            self.name='ljxfadmin'
        elif flat=='4':
            self.name='jhgxds'
        elif flat=='5':
            self.name='ylsdyrmyy'
        self.login(name=self.name)
        sleep(3)
        return self.name

    def xitong(self,):
        comein=input('是否进入接警页面?(y/n)：')
        if comein=='n':
            pass
        elif comein=='y':
            print('''
            1、火灾报警
            2、无线火灾
            3、故障电弧
            4、智慧用电
            5、室内消防水
            6、室外消火栓
            ''')
            self.num=input('选择子系统：')
            if self.num=='1':
                self.browser.find_element_by_xpath('''//div[@onclick="document.location.href='/user/fireAlarm.do?formAction=list&fireType=0'"]''').click()
                self.port=8001
            else:
                print('嘤嘤嘤~没做呢')
            # elif num=='2':
            #     self.browser.find_element_by_xpath('''//''').click()
            # elif num=='3':
            #     self.browser.find_element_by_xpath('''//''').click()
            # elif num=='4':
            #     self.browser.find_element_by_xpath('''//''').click()
            # elif num=='5':
            #     self.browser.find_element_by_xpath('''//''').click()
            # elif num=='6':
            #     self.browser.find_element_by_xpath('''//''').click()

    def hzbj(self):
        print('''
        1.上传建筑消防设施系统状态
        2.上传部件运行状态
        3.上传传输装置运行状态
        4.上传传输装置操作信息
        5.手录（自动计算校验和）
        ''')
        type=input('选择发送信息类型：')
        self.device_type = ''
        if type=='1':
            self.device_type='01'
        elif type=='2':
            self.device_type='02'
        elif type=='3':
            self.device_type='15'
        elif type=='4':
            self.device_type='18'
        elif type=='5':
            self.device_type=input()
        return self.device_type

    def time_tip(self):
        now_time = datetime.now()
        time_str = datetime.strftime(now_time, '%S%M%H%d%m%g')
        self.time_hex = ''
        for i in range(0, len(time_str), 2):
            tip = hex(int(time_str[i:i + 2]))[2:].rjust(2, '0')
            self.time_hex += tip
        return self.time_hex

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
        choose=input('是否继续发送？y/n： ')
        if choose=='n':
            pass
        elif choose=='y':
            sys=input('是否换子系统？y/n： ')
            if sys=='n':
                self.data_deal()
                self.tcpcli()
            else:
                self.xitong()


        tcpclisocket.close()

ceshi=flattest()
ceshi.choose_flat()
ceshi.xitong()
ceshi.data_deal()
ceshi.tcpcli()






# #获取单位实时火警对应位置并点击进入
# elem = browser.find_element_by_xpath('''//*[@class='title']/div[@onclick="document.location.href='/user/fireAlarm.do?formAction=list&fireType=0&css1=1&css2=1'"]''')
# elem.click()
# sleep(3)
# elem = browser.find_element_by_xpath('''//*[@id='fireAlarms']/tr[1]/td[11]/a[@href="/user/fireAlarm.do?formAction=getGpsMap&orgId=114"]''')
# elem.click()
# sleep(3)
# # 获取当前所有窗口句柄（窗口A、B）,切换到窗口A
# handles = browser.window_handles
# browser.switch_to_window(handles[0])
# sleep(3)
# #警情处理
# elem = browser.find_element_by_xpath('''//*[@id='fireAlarms']/tr[1]/td[11]/span[@class="jingqingchuli"]''')
# elem.click()
# elem = browser.find_element_by_xpath('''//*[@id='form1']/input[@id="d"]''')
# elem.click()
# sleep(3)
# elem = browser.find_element_by_xpath('''//*[@id='form1']/span[@class="content_3_span"]''')
# elem.click()



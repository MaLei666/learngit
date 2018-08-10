# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep,time
from bs4 import BeautifulSoup
from socket import *
from datetime import datetime

class flattest():
    def __init__(self):
        # 模拟登陆云平台，
        options = webdriver.FirefoxOptions()
        options.add_argument(
            'user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
        self.browser = browser=webdriver.Firefox(firefox_options=options)
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
        print('要登录的平台：')
        flat=input()
        if flat=='bj':
            self.name='bjzkadmin'
        elif flat=='yl':
            self.name='ylxfadmin'
        elif flat=='lj':
            self.name='ljxfadmin'
        elif flat=='jh':
            self.name='jhgxds'
        elif flat=='rmyy':
            self.name='ylsdyrmyy'
        self.login(name=self.name)
        sleep(3)
        return self.name

    def xitong(self,):
        print('是否进入接警页面?(y/n)')
        jiejing=input()
        if jiejing=='n':
            pass
        elif jiejing=='y':
            print('''
            1、火灾报警
            2、无线火灾
            3、故障电弧
            4、智慧用电
            5、室内消防水
            6、室外消火栓
            ''')
            self.num=input()
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

    def tcpcli(self):
        tcpclisocket = socket(AF_INET, SOCK_STREAM)
        tcpseraddr = ('47.92.90.52', self.port)
        tcpclisocket.connect(tcpseraddr)
        senddata = input('输入：')
        tcpclisocket.send(bytes(senddata, encoding='utf8'))

        recvdata = tcpclisocket.recv(1024)
        print('接收：', recvdata)

        tcpclisocket.close()

    def time_tip(self):
        now_time = datetime.now()
        time_str = datetime.strftime(now_time, '%S%M%H%d%m%g')
        self.time_hex = ''
        for i in range(0, len(time_str), 2):
            tip = hex(int(time_str[i:i + 2]))[2:].rjust(2, '0')
            self.time_hex += tip

    def data_deal(self,senddata):
        startSign = hex  # 启动符2,流水号2
        sernum = senddata[4:24]  # 流水号2，版本号2，时间标签6    10
        oriaddr = senddata[24:36]  # 源地址6
        desaddr = senddata[36:48]  # 目的地址6
        datalen = senddata[48:52]  # 应用单元数据长度2
        combyte = senddata[52:54]  # 命令字节1
        usedata = senddata[54:-6]  # 应用数据单元
        enddata = senddata[-4:]  # 结束符

    def hzbj(self):

        print('''
        选择发送信息类型：
        1.上传建筑消防设施系统状态
        2.上传部件运行状态
        3.上传传输装置运行状态
        4.上传传输装置操作信息
        5.手录（自动计算校验和）
        ''')
        self.type=input()
        if self.type=='1':
            self.device_type=1
        elif self.type=='2':
            self.device_type=2
        elif self.type=='3':
            self.device_type=15
        elif self.type=='4':
            self.device_type=18
        elif self.type=='5':
            self.device_type=input('类型标志：')








ceshi=flattest()
# ceshi.choose_flat()
# ceshi.xitong()

ceshi.time_tip()








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

# #爬取百度文库，失败，what happened！
# browser=webdriver.ChromeOptions()
# browser.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
# driver=webdriver.Chrome(chrome_options=browser)
# driver.maximize_window()
# driver.get('https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html')
# #点击继续阅读
# elem = driver.find_elements_by_xpath('''//*[@class="foldpagewg-text-con"]/div[@class="foldpagewg-text"]''')
# driver.execute_script('arguments[0].scrollIntoView();', elem[-1])
# elem.click()
# for i in range(3):
#     elem = driver.find_element_by_xpath('''//*[@class="pagerwg-root"]/div[@class="pagerwg-button"]''')
#     elem.click()
#爬取数据
# html=driver.page_source
# bf1=BeautifulSoup(html,'lxml')
# title=bf1.find_all('div',class_='doc-title')
# print(title)
#
#
# page=driver.find_elements_by_xpath()

# -*- coding: utf-8 -*-
import requests
from urllib import request
from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import etree
import subprocess as sp
import random
import re
import time

# def get_proxys(page=1):
#     #自动保持cookie,不需要自己维护cookie内容
#     s = requests.Session()
#     #高匿ip地址
#     url='http://www.xicidaili.com/nn/%d' %page
#     #完善header
#     header= {'Upgrade-Insecure-Requests':'1',
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
#     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Accept-Encoding':'gzip, deflate, sdch, br',
#     'Accept-Language':'zh-CN,zh;q=0.8',
#     }
#     #get请求，应答解码
#     response=s.get(url=url,headers=header)
#     response.encoding='utf-8'
#     #获取网页信息
#     html=response.text
#     #获取id为ip_list的table
#     bf1=BeautifulSoup(html,'lxml')
#     bf2=BeautifulSoup(str(bf1.find_all(id="ip_list")),'lxml')
#     iplist=bf2.table.contents
#     #存储代理列表
#     prolist=[]
#     #爬取每个代理的信息
#     for index in range(len(iplist)):
#         #空行与有用数据交替，第一个元素为空行
#         if index%2==1 and index!=1:
#             dom=etree.HTML(str(iplist[index]))
#             ip=dom.xpath('//td[2]')
#             port=dom.xpath('//td[3]')
#             protocol=dom.xpath('//td[6]')
#             prolist.append(protocol[0].text.lower()+'#'+ip[0].text+'#'+port[0].text)
#     #返回代理列表
#     return prolist
#
# '''
# 检查代理ip连通性
# ip——代理ip地址
# losetime——匹配丢包数
# wastetime——匹配平均时间
# average_time——代理ip平均耗时
# '''
# def check_ip(ip,losetime,wastetime):
#     # 命令 -n 要发送的回显请求数 -w 等待每次回复的超时时间(毫秒)
#     cmd="ping -n 3 -w 3 %s"
#     #执行命令
#     p=sp.Popen(cmd % ip,stdin=sp.PIPE,stdout=sp.PIPE,stderr=sp.PIPE,shell=True)
#     #获得返回信息并解码
#     out=p.stdout.read().decode('gbk')
#     #丢包数
#     losetime=losetime.findall(out)
#     #当匹配到丢包信息失败，默认为三次请求全部丢包，丢包数目lose赋值为3
#     if len(losetime)==0:
#         lose=3
#     else:
#         lose=int(losetime[0])
#     #如果丢包数目大于2，认为连接超时，返回平均耗时1000ms
#     if lose>2:
#         #返回false
#         return 1000
#     #如果丢包数目小于等于2，获取平均耗时时间
#     else:
#         #平均时间
#         average=wastetime.findall(out)
#         #当匹配耗时时间信息失败，默认三次请求严重超时，返回平均耗时1000ms
#         if len(average)==0:
#             #返回false
#             return 1000
#         else:
#             average_time=int(average[0])
#             return average_time
# '''
# 初始化正则表达式
# losetime——匹配丢包数
# wastetime——匹配平均时间
# '''
# def initpattern():
#     #匹配丢包数，平均时间
#     #丢失，平均的格式要和接收数据包格式一样，等号前后有空格，不然匹配不上
#     losetime=re.compile(u"丢失 = (\d+)", re.IGNORECASE)
#     wastetime=re.compile(u"平均 = (\d+)ms",re.IGNORECASE)
#     return losetime,wastetime
#
if __name__ == '__main__':
#     #初始化正则表达式
#     losetime,wastetime=initpattern()
#     #获取ip代理
#     proxy_list=get_proxys(1)
#     #如果平均时间超过200ms，重新选择代理
#     while True:
#         #从100个ip中随机选取一个ip作为代理访问
#         proxy=random.choice(proxy_list)
#         split_proxy=proxy.split('#')
#         #获取ip
#         ip=split_proxy[1]
#         #检查ip
#         average_time=check_ip(ip,losetime,wastetime)
#         if average_time>200:
#             #去掉不能使用的ip
#             print(ip,'连接失败，重新获取')
#             proxy_list.remove(proxy)
#         if average_time<200:
#             break
#     #去掉已经使用的ip
#     proxy_list.remove(proxy)
#     proxy_dict={split_proxy[1]+':'+split_proxy[2]}
#     print('使用代理：',proxy_dict)

    #使用代理ip访问网址
    #使用代理ip，打开url
    browser = webdriver.FirefoxOptions()
    # browser.add_argument('--proxy-server=http://60.177.230.250:18118')
    browser.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
    driver = webdriver.Firefox(firefox_options=browser)
    driver.maximize_window()
    driver.get('https://wenku.baidu.com/view/59d488ac85868762caaedd3383c4bb4cf7ecb783.html?from=search')

#点击继续阅读显示全部页
    #定位元素，元素聚焦
    elem=driver.find_elements_by_xpath('''//*[@id="html-reader-go-more"]/p[@class="banner-more-title"]''')
    #拖动到可见元素
    driver.execute_script('arguments[0].scrollIntoView();', elem[-1])
    #element为可点击元素地址，elements为列表，不可点击
    #点击继续阅读
    elem=driver.find_element_by_xpath('''//*[@id="html-reader-go-more"]/p[@class="down-arrow goBtn"]''')
    elem.click()

#爬取文章并保存
    #创建txt文件
    file=open('爬取文章.txt','w',encoding='utf-8')
    html=driver.page_source
    #print(html)
    bf1=BeautifulSoup(html,'lxml')
    pages=bf1.find_all('div',id='reader-container-inner-1')
    #print(pages)
    #查出文档一共有多少页
    #查找页数对应行的标签，输出为列表
    page_count=bf1.find_all('span',class_='page-count')
    #选择列表第一个元素，string只能取标签为单个节点的数据，取后切片获得页数
    page_count=page_count[0].string[1:]
    page_count=int(page_count)+1
    #前三页为默认显示，先打印出来
    for each_page in range(1,4):
        class_page='mod reader-page complex reader-page-'+str(each_page)
        #print(class_page)
        texts=bf1.find_all(class_=class_page)
        soup_texts=BeautifulSoup(str(texts),'lxml')
        text=soup_texts.find_all(class_='ie-fix')
        download_text=BeautifulSoup(str(text),'lxml')
        print(class_page)
        write_flag=True
        for each in download_text.div.text.replace('/xa0',''):
            if each == 'h':
                write_flag = False
            if write_flag == True and each != '':
                file.write(each)
            if write_flag == True and each == '\r':
                file.write('\n')
        file.write('\n\n')

    # 后面页数为隐藏显示，后打印
    for each_page in range(4,page_count):
        class_page='mod reader-page complex hidden-doc-banner reader-page-'+str(each_page)
        #查找每页标签位置并提取数据
        texts = bf1.find_all(class_=class_page)
        soup_texts = BeautifulSoup(str(texts), 'lxml')
        download_text=[]
        text = soup_texts.find_all('div',class_='ie-fix')
        download_text = BeautifulSoup(str(text), 'lxml')
        print(class_page)
        write_flag = True
        # 跳转到打印好的页面,使下一页可以显示数据
        # 无法正常滑动
        elem = driver.find_elements_by_xpath('''//*[@id="reader-container-inner-1"]//div[@class="ie-fix"]''')
        print(elem)
        driver.execute_script('arguments[0].scrollIntoView();', elem[-1])
        time.sleep(1)
        for i in download_text.div.text.replace('/xa0', ''):
            if i == 'h':
                write_flag = False
            if write_flag == True and i != '':
                file.write(i)
            if write_flag == True and i == '\r':
                file.write('\n')
        file.write('\n\n')

    file.close()









#隐含输入字段
    # driver=webdriver.PhantomJS(executable_path='D:/下载/phantomjs_xpgod/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    # driver.get(url)
    # driver.implicitly_wait(1)
    # links=driver.find_elements_by_tag_name('a')
    # for link in links:
    #     if not link.is_displayed():
    #         print(link.get_attribute('href'),'是蜜罐圈套')
    # fields=driver.find_elements_by_tag_name('input')
    # for field in fields:
    #     if not field.is_displayed():
    #         print(field.get_attribute('name'),'值不改变')
# -*- coding: utf-8 -*-
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import etree
import subprocess as sp
import random
import re

def get_proxys(page=1):
    #自动保持cookie,不需要自己维护cookie内容
    s = requests.Session()
    #高匿ip地址
    url='http://www.xicidaili.com/nn/%d' %page
    #完善header
    header= {'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    }
    #get请求，应答解码
    response=s.get(url=url,headers=header)
    response.encoding='utf-8'
    #获取网页信息
    html=response.text
    #获取id为ip_list的table
    bf1=BeautifulSoup(html,'lxml')
    bf2=BeautifulSoup(str(bf1.find_all(id="ip_list")),'lxml')
    iplist=bf2.table.contents
    #存储代理列表
    prolist=[]
    #爬取每个代理的信息
    for index in range(len(iplist)):
        #空行与有用数据交替，第一个元素为空行
        if index%2==1 and index!=1:
            dom=etree.HTML(str(iplist[index]))
            ip=dom.xpath('//td[2]')
            port=dom.xpath('//td[3]')
            protocol=dom.xpath('//td[6]')
            prolist.append(protocol[0].text.lower()+'#'+ip[0].text+'#'+port[0].text)
    #返回代理列表
    return prolist

'''
检查代理ip连通性
ip——代理ip地址
losetime——匹配丢包数
wastetime——匹配平均时间
average_time——代理ip平均耗时
'''
def check_ip(ip,losetime,wastetime):
    # 命令 -n 要发送的回显请求数 -w 等待每次回复的超时时间(毫秒)
    cmd="ping -n 3 -w 3 %s"
    #执行命令
    p=sp.Popen(cmd % ip,stdin=sp.PIPE,stdout=sp.PIPE,stderr=sp.PIPE,shell=True)
    #获得返回信息并解码
    out=p.stdout.read().decode('gbk')
    print(out)
    #丢包数
    losetime=losetime.findall(out)
    #当匹配到丢包信息失败，默认为三次请求全部丢包，丢包数目lose赋值为3
    if len(losetime)==0:
        lose=3
    else:
        lose=int(losetime[0])
    #如果丢包数目大于2，认为连接超时，返回平均耗时1000ms
    if lose>2:
        #返回false
        return 1000
    #如果丢包数目小于等于2，获取平均耗时时间
    else:
        #平均时间
        average=wastetime.findall(out)
        return average
        #当匹配耗时时间信息失败，默认三次请求严重超时，返回平均耗时1000ms
        # if len(average)==0:
        #     #返回false
        #     return 1000
        # else:
        #     average_time=int(average[0])
        #     return average_time
'''
初始化正则表达式
losetime——匹配丢包数
wastetime——匹配平均时间
'''
def initpattern():
    #匹配丢包数，平均时间
    losetime=re.compile(u'丢失=(\d+)',re.IGNORECASE)
    wastetime=re.compile(u'平均=(\d+)ms',re.IGNORECASE)
    return losetime,wastetime

if __name__ == '__main__':
    #初始化正则表达式
    losetime,wastetime=initpattern()
    #获取ip代理
    proxy_list=get_proxys(1)
    #如果平均时间超过200ms，重新选择代理
    while True:
        #从100个ip中随机选取一个ip作为代理访问
        proxy=random.choice(proxy_list)
        split_proxy=proxy.split('#')
        #获取ip
        ip=split_proxy[1]
        #检查ip
        average_time=check_ip(ip,losetime,wastetime)
        print(average_time)
        if average_time>200:
            #去掉不能使用的ip
            print(ip,'连接失败，重新获取')
            proxy_list.remove(proxy)
        if average_time<200:
            break
    #去掉已经使用的ip
    proxy_list.remove(proxy)
    proxy_dict={split_proxy[0]:split_proxy[1]+':'+split_proxy[2]}
    print('使用代理：',proxy_dict)






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
# -*- coding: utf-8 -*-
import requests,random,re,json,time,urllib
from urllib import request
from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import etree
import subprocess as sp
from selenium import webdriver
from pyquery import pyquery as p
# from pyExcelerator import *
from urllib.parse import quote
from bs4 import BeautifulSoup


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
        #当匹配耗时时间信息失败，默认三次请求严重超时，返回平均耗时1000ms
        if len(average)==0:
            #返回false
            return 1000
        else:
            average_time=int(average[0])
            return average_time
'''
初始化正则表达式
losetime——匹配丢包数
wastetime——匹配平均时间
'''
def initpattern():
    #匹配丢包数，平均时间
    #丢失，平均的格式要和接收数据包格式一样，等号前后有空格，不然匹配不上
    losetime=re.compile(u"丢失 = (\d+)", re.IGNORECASE)
    wastetime=re.compile(u"平均 = (\d+)ms",re.IGNORECASE)
    return losetime,wastetime

def proxy_choose():
    # 初始化正则表达式
    # losetime, wastetime = initpattern()
    # 获取ip代理列表
    proxy_list = get_proxys(1)
    # # 如果平均时间超过200ms，重新选择代理
    # while True:
    #     # 从100个ip中随机选取一个ip作为代理访问
    #     proxy = random.choice(proxy_list)
    #     split_proxy = proxy.split('#')
    #     # 获取ip
    #     ip = split_proxy[1]
    #     # 检查ip
    #     average_time = check_ip(ip, losetime, wastetime)
    #     if average_time > 200:
    #         # 去掉不能使用的ip
    #         print(ip, '连接失败，重新获取')
    #         proxy_list.remove(proxy)
    #     if average_time < 200:
    #         break
    # # 去掉已经使用的ip
    proxy=proxylist()[1]
    proxy_list.remove(proxy)
    # proxy_dict = {split_proxy[1] + ':' + split_proxy[2]}
    # proxy_ip = str(split_proxy[1] + ':' + split_proxy[2])
    # # print(proxy_ip)
    # print('使用代理：', proxy_dict)
    return proxy_list

def proxylist():
    losetime, wastetime = initpattern()
    proxy_list=proxy_choose()
    while True:
        if len(proxy_list)<=20:
            proxy_choose()
            proxy_list = list(proxy_choose())
        else:
            # 从代理ip池中随机选取一个ip作为代理访问
            proxy = random.choice(proxy_list)
            split_proxy = proxy.split('#')
            # 获取ip
            ip = split_proxy[1]
            port=int(split_proxy[2])
            # 检查ip
            average_time = check_ip(ip, losetime, wastetime)
            if average_time > 200:
                # 去掉不能使用的ip
                print(ip, '连接失败，重新获取')
                proxy_list.remove(proxy)
            if average_time < 200:
                break
    # 去掉已经使用的ip
    proxy_list.remove(proxy)
    proxy_dict = {split_proxy[1] + ':' + split_proxy[2]}
    print('使用代理：', proxy_dict,len(proxy_list))

    # 使用代理ip访问网址
    # 谷歌浏览器设置代理ip
    # browser = webdriver.ChromeOptions()
    # # browser.add_argument('--proxy-server=http://' + ip)
    # browser.add_argument('--proxy-server=http://223.241.78.194:8010')
    # browser.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0"')
    # os.environ["webdriver.chrome.driver"] = chromedriver
    # driver = webdriver.Chrome(chromedriver, chrome_options=chome_options)

    # 火狐设置代理ip
    webdriver.DesiredCapabilities.FIREFOX[
        'firefox.page.settings.userAgent'] = "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0"
    profile = webdriver.FirefoxProfile()
    profile.set_preference('network.proxy.type', 1)  # 默认值0，就是直接连接；1就是手工配置代理。
    profile.set_preference('network.proxy.http', ip)
    profile.set_preference('network.proxy.http_port', port)
    profile.set_preference('network.proxy.ssl', ip)
    profile.set_preference('network.proxy.ssl_port', port)
    profile.update_preferences()
    driver = webdriver.Firefox(profile)
    return driver,proxy

#判断是否为错误网页
def falsepage():
    b = choose_ip()
    if b == True:
        #如果为错误网页，从代理ip池中随机选择一个，换代理后重新打开网页
        proxylist()
        driver.get(URL)




#验证码识别
#先写个手动识别吧……emm……写完代码再搞自动识别吧……嘤嘤嘤…………
def checknum():
    num=input('输入验证码:')
    number=driver.find_element_by_name('c')
    number.send_keys(num)
    time.sleep(1)
    enter=driver.find_element_by_xpath('''//*[@class="p5"]/a[@id="submit"]''')
    enter.click()

#搜索公众号
def searchnum():
    # 获取输入框，输入英文微信公众号，搜索显示
    elem1_value = driver.find_element_by_name('query')
    time.sleep(1)
    elem1_value.send_keys('python6359')
    time.sleep(1)
    elem2 = driver.find_element_by_xpath('''//*[@class="querybox"]/input[@class="swz2"]''')
    elem2.click()

#进入公众号
def mainpage():
    mainpage=driver.find_element_by_xpath('''//div[@class="txt-box"]//a[@target="_blank"]''')
    mainpage.click()

#爬取文章
def text_download():
    #标题
    title=driver.find_elements_by_class_name('weui_media_title')
    #发表时间
    time_updata=driver.find_elements_by_class_name('weui_media_extra_info')
    #标题对应地址
    artical_url=driver.find_elements_by_xpath('''//h4[@class="weui_media_title"]''')
    # artical_url.click()
    print(title,time_updata,artical_url)
    #文章内容
    #存储文章到本地

#如果出现代理服务器拒绝连接，从ip池随机选择一个ip
def choose_ip():
    try:
        driver.find_element_by_id('errorPageContainer')
        b=True
    except:
        b=False
    return b



if __name__ == '__main__':
    URL = ('http://weixin.sogou.com/')
    # URL=('http://www.whatismyip.com.tw/')
    # 使用代理ip打开网页
    driver=proxylist()[0]
    driver.get(URL)
    time.sleep(2)

    #判断是否为错误网页
    falsepage()

    # 查看本机ip
    # driver.get("http://httpbin.org/ip")
    # driver.maximize_window()
    # driver.quit()

    #出现验证码界面
    #判定界面有没有name=c的元素存在
    try:
        driver.find_element_by_name('c')
        a=True
    except:
        a=False
    #如果有这个元素，则出现了验证码界面
    if a==True:
        checknum()
        time.sleep(1)
        mainpage()
    #如果没有这个元素，则直接出现了公众号列表
    elif a==False:
        mainpage()

    #进入公众号列表后，有可能出现验证码界面
    try:
        driver.find_element_by_id('input')
        a = True
    except:
        a = False
    # 如果有这个元素，则出现了验证码界面
    if a == True:
        checknum()
        time.sleep(1)
        text_download()
    elif a == False:
        time.sleep(1)
        text_download()









    # #获取公众号主页
    # mainpage=driver.find_element_by_xpath('''//*[@class="tit"]/a[@target="_blank"]''')
    # mainpage.click()
    # timeout=5
    # s=requests.Session()
    # #Excel第一行数据
    # excel_data=[u'编号',u'时间',u'文章标题',u'文章地址',u'文章简介']
    # #定义Excel操作句柄
    # # self.excel_w=Workbook()

    # # 搜索入口地址，搜索公众号,获取主页
    # response = s.get(url=sogou_search, headers=headers, timeout=timeout,ip=proxy_dict)
    # html = response.text
    # bf1 = BeautifulSoup(html, 'lxml')
    # print(bf1)
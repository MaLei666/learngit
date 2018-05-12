# -*- coding: utf-8 -*-
from urllib import request
from urllib import parse
import json
from urllib import error
import chardet
from selenium import webdriver

# if __name__ == "__main__":
#     # 向指定的url发送请求，并返回服务器响应的类文件对象
#     #response = request.urlopen("http://fanyi.baidu.com/")
#     req=request.Request("http://fanyi.baidu.com/")
#     response = request.urlopen(req)
#     print(response)
#     html = response.read()
#     charset=chardet.detect(html)['encoding']  #获取html编码方式
#     #print(charset)
#     print(html.decode(charset))
#     print(response.getcode())   #HTTP的状态码，如果返回200表示请求成功
#     print(response.geturl())    #url的字符串
#     print(response.info())      #meta标记的元信息，包括一些服务器的信息

# #向指定url发送数据获得翻译结果
# if __name__ == '__main__':
#     # 对应上图的Request URL
#     Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
#     # 创建Form_Data字典，存储上图的Form Data
#     Form_Data = {}
#     Form_Data['action'] = 'FY_BY_CLICKBUTTION'
#     Form_Data['client'] = 'fanyideskweb'
#     Form_Data['doctype'] = 'json'
#     Form_Data['from'] = 'AUTO'
#     Form_Data['i'] = 'translate'
#     Form_Data['keyfrom'] = 'fanyi.web'
#     Form_Data['salt'] = '1524659357271'
#     Form_Data['sign'] = '6cd4b2e534bd5b89cd11af54d4dd483e'
#     Form_Data['smartresult'] = 'dict'
#     Form_Data['to'] = 'AUTO'
#     Form_Data['typoResult'] = 'false'
#     Form_Data['version'] = '2.1'
#
#     data = parse.urlencode(Form_Data).encode('utf-8')       # 使用urlencode方法转换标准格式
#     response = request.urlopen(Request_URL,data)           # 向指定url发送data数据
#     html = response.read().decode('utf-8')                  # 读取信息并解码
#     translate_results = json.loads(html)                    # 使用JSON
#     #print(translate_results)
#     translate_results = translate_results['translateResult'][0][0]['tgt']   # 找到翻译结果
#     print("翻译的结果是：%s" % translate_results)              # 打印翻译信息

# if __name__ == '__main__':
#     # URLError
#     url='http://www.iloveyou.com/'                  #一个不存在的连接
#     # HTTPError
#     url = 'http://www.douyu.com/Jack.html'      #请求的资源没有在服务器上找到,www.douyu.com这个服务器是存在的，但是我们要查找的Jack.html资源是没有的
#     req=request.Request(url)
#     try:
#         response=request.urlopen(req)
#         # html=response.read().decode('utf-8')
#         # print(html)
#     # except error.URLError as e:
#     #     print(e.reason)
#     # except error.HTTPError as e:
#     #     print(e.code)
#     except error.URLError as e:
#         if hasattr(e,'code'):
#             print('httperror',e.code)
#         elif hasattr(e,'reason'):
#             print('urlerror',e.reason)


# #User Agent
# if __name__ == '__main__':
#     url='http://www.csdn.net/'      #CSDN不更改User Agent是无法访问的
#     #1. 填入headers参数
#     # head={}                         #创建字典，写入参数
#     # head['user_agent']='Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'
#     # req=request.Request(url,headers=head)       #创建Request对象
#
#     #2.创建完成之后,使用add_header()
#     req=request.Request(url)
#     req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0')
#     response=request.urlopen(req)               #传入创建好的Request对象
#     html=response.read().decode('utf-8')        #读取响应信息并解码
#     print(html)

#代理ip
if __name__ == '__main__':
    url='http://www.whatismyip.com.tw/'
    proxy={'http':'60.177.229.230:18118'}       #设置代理ip
    proxy_support=request.ProxyHandler(proxy)   #创建ProxyHandler
    opener=request.build_opener(proxy_support)  #创建opener
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0')]
    request.install_opener(opener)              #安装opener
    response=request.urlopen(url)               #使用自己安装好的Opener
    html=response.read().decode('utf-8')        #读取相应信息并解码
    print(html)
    browser = webdriver.FirefoxOptions()

    driver = webdriver.Firefox(firefox_options=browser)
    driver.maximize_window()
    driver.get(url=url)
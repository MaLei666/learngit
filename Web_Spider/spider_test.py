# -*- coding: utf-8 -*-
from urllib import request
import chardet
from urllib import parse
import json

# if __name__ == "__main__":
#     # 向指定的url发送请求，并返回服务器响应的类文件对象
#     req=request.Request("http://fanyi.baidu.com/")
#     response = request.urlopen(req)
#     html = response.read()
#     charset=chardet.detect(html)['encoding']
#     #print(charset)
    # print(html.decode(charset))
    # print(response.getcode())   #HTTP的状态码，如果返回200表示请求成功
    # print(response.geturl())    #url的字符串
    # print(response.info())      #meta标记的元信息，包括一些服务器的信息

#向指定url发送数据获得翻译结果
if __name__ == '__main__':
    # 对应上图的Request URL
    Request_URL = 'http://fanyi.baidu.com/v2transapi'
    # 创建Form_Data字典，存储上图的Form Data
    Form_Data = {}
    Form_Data['from'] = 'en'
    Form_Data['query'] = 'range'
    Form_Data['sign'] = '993057.771088'
    Form_Data['simple_means_flag'] = '3'
    Form_Data['to'] = 'zh'
    Form_Data['token'] = '1461a162cbae310b72f87880882038fa'
    Form_Data['transtype'] = 'translang'
    # 使用urlencode方法转换标准格式
    data = parse.urlencode(Form_Data).encode('utf-8')
    # 传递Request对象和转换完格式的数据
    response = request.urlopen(Request_URL, data)
    # 读取信息并解码
    html = response.read().decode('utf-8')
    # 使用JSON
    translate_results = json.loads(html)
    # 找到翻译结果
    translate_results = translate_results['translateResult'][0][0]['tgt']
    # 打印翻译信息
    print("翻译的结果是：%s" % translate_results)





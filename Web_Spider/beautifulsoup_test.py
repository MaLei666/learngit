# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib import request
import chardet
import re,sys

# #获取一章的数据
# if __name__ == '__main__':
#     download_url='http://www.biqukan.com/1_1094/5403177.html'
#     head={}
#     head['User-Agent']='Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'
#     download_req=request.Request(url=download_url,headers=head)
#     download_response=request.urlopen(download_req)
#     download_html=download_response.read().decode('gbk')
#     souptext=BeautifulSoup(download_html,'lxml')
#     text=souptext.find_all(id='content', class_='showtxt')
#     souptext=BeautifulSoup(str(text),'lxml')
#     print(souptext.div.text.replace('\xa0',''))
#     # charset = chardet.detect(download_html)['encoding']  # 获取html编码方式
#     # print(charset)

#获取所有章节数据，下载到txt文件中
if __name__ == '__main__':
    #创建txt文件
    file=open('超品相师.txt','w',encoding='utf-8')
    #小说目录地址
    target_url='http://www.biqukan.com/1_1225/'
    #创建head字典，设置User-Agent
    head = {}
    head['User-Agent']='Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19'
    #请求网址为小说目录地址，将请求信息中header替换为设置的header
    target_req=request.Request(url=target_url,headers=head)
    #向指定url发送设定好的请求信息，并返回服务器相应的类文件对象,使用read读取后解码
    target_response=request.urlopen(target_req)
    target_html=target_response.read().decode('gbk','ignore')

    #创建beautifulsoup对象，存储网页源代码
    listmain_soup=BeautifulSoup(target_html,'lxml')
    #print(listmain_soup)
    #搜索文档树，找div标签中class为listmain的内容，标签名和属性名一起使用来查找
    chapter=listmain_soup.find_all('div',class_='listmain')
    #创建beautifulsoup对象，存储过滤后的代码
    download_soup=BeautifulSoup(str(chapter),'lxml')
    #print(download_soup)

    #计算章节个数，遍历文档树，dl标签的content属性将dl的子节点以列表形式输出
    #列表包含一行值和换行符交替，首尾均为换行符，长度=(len-1)/2,为啥减8呢
    num=(len(download_soup.dl.contents)-1)/2-8
    # print(download_soup.dl.contents)
    index=1

    #记录内容标志位,只要正文卷的链接，最新章节列表剔除
    begin_flag=False
    #遍历dl标签下所有子节点
    for child in download_soup.dl.children:
        #滤除回车
        if child != '\n':
            #获取标签内部文字，找到正文卷，使能标志位，u'string'  表示已经是 unicode 编码的 'string' 字符串
            if child.string==u'《超品相师》正文卷':
                begin_flag=True
            #确定是正文卷，并且标签<a>内不为空，爬取链接并下载链接内容
            if begin_flag==True and child.a!=None:
                #拼接下载地址为网站地址+<a>标签中href属性中的地址
                download_url='http://www.biqukan.com'+child.a.get('href')
                #请求信息拼接
                download_req=request.Request(url=download_url,headers=head)
                #向指定URL发送请求信息并接收返回信息，read解码
                download_response=request.urlopen(download_req)
                download_html=download_response.read().decode('gbk','ignore')
                #下载章节标题名为子节点标签内部文字
                download_name=child.string
                #创建beautifulsoup对象，
                soup_texts=BeautifulSoup(download_html,'lxml')
                texts=soup_texts.find_all(id = 'content', class_ = 'showtxt')
                soup_text=BeautifulSoup(str(texts),'lxml')
                write_flag=True
                file.write(download_name+'\n\n')
                #爬取内容写入文件
                for each in soup_text.div.text.replace('/xa0',''):
                    if each=='h':
                        write_flag=False
                    if write_flag==True and each!='':
                        file.write(each)
                    if write_flag==True and each=='\r':
                        file.write('\n')
                file.write('\n\n')
                #打印爬取进度
                print(sys.stdout.write('已下载：%.3f%%'%float(index/num)+'\r'))
                sys.stdout.flush()
                index+=1
    file.close()

                # print(download_name+':'+download_url)


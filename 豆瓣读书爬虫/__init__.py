# -*- coding: utf-8 -*-
import requests,time,pymysql,re,random
from bs4 import BeautifulSoup




# def cookie_get():
#     #保存cookie到文件
#     filecook='cookie.txt'
#     # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
#     cookie=cookiejar.MozillaCookieJar(filecook)
#     # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
#     handler=request.HTTPCookieProcessor(cookie)
#     # 通过CookieHandler创建opener
#     opener=request.build_opener(handler)
#     res=opener.open('https://book.douban.com/')
#     # ignore_discard的意思是即使cookies将被丢弃也将它保存下来；
#     # ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入
#     cookie.save(ignore_discard=True,ignore_expires=True)

#连接数据库
connection=pymysql.connect(host='localhost',user='root',password='zkyr1006',charset='utf8')
with connection.cursor() as cursor:
    sql = "USE python;"
    cursor.execute(sql)
connection.commit()


def login(url):
# 文件中获取cookie并访问
    cookies={}
    s = requests.session()
    with open('E:\example\豆瓣读书爬虫\cookie.txt')as file:
        raw_cookies=file.read()
        for line in raw_cookies.split(';'):
            key,value=line.split('=',1)
            cookies[key]=value
    proxie = {'http': 'http://14.118.254.31:6666'}
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'}
    res=s.get(url=url,cookies=cookies,headers=headers,proxies=proxie)
    return res

def sorturl():
    url='https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
    # url='http://www.whatismyip.com.tw/'
    web=login(url)
    # print(web.text)
    urls=[]
    soup=BeautifulSoup(web.text,'lxml')
    #通过id名和子标签进行查找,>前后要有空格，不然失效
    tags=soup.select('#content > div > div.article > div > div > table > tbody > tr > td > a')
    # print(tags)
    for tag in tags:
        tag=tag.string
        tag_url='https://book.douban.com/tag/'+str(tag)
        urls.append(tag_url)
    # print(urls)
    # 连接存入
    with open('sort_artical.txt','w') as file:
        for link in urls:
            file.write(link+'\n')
    return urls
# sorturl()

#爬取书籍详细信息
def book_info():
    urls=sorturl()
    #每个进入每个分类的书籍列表
    for url in urls:
        #存放每一本书的数据
        data=[]
        booklist=login(url.strip())
        soup=BeautifulSoup(booklist.text.encode('utf-8'),'lxml')
        books=soup.select('''#subject_list > ul > li > div.info > h2 > a''')

        #获取每本书信息
        for book in books:
            book_url=book.get('href')
            book_data=login(book_url)
            booksoup=BeautifulSoup(book_data.text.encode('utf-8'),'lxml')
            info=booksoup.select('#info')  #select返回为列表
            infos = list(info[0].strings)
            infos=list(infos[0].replace('\n','')
            title=booksoup.select('#wrapper > h1 > span')[0].string.replace('\n','')
            author=booksoup.select('#info > a')[0].string.replace('\n','')
            money = infos[infos.index('定价：') + 1]
            # index输出关键字在字符串中出现的位置，从0开始
            publish=infos[infos.index('出版社：')+1] #输出出版社后面的一个字符串，为出版公司
            pages=infos[infos.index('页数：')+1]
            years = infos[infos.index('出版年：') + 1]
            ISBN = infos[infos.index('ISBN：') + 1]
            people=booksoup.select('#interest_sectl > div > div > div > div > span > a > span')[0].get_text
            score=booksoup.select('#interest_sectl > div > div > strong')[0].get_text
            data.append([title,author,money,publish,pages,years,ISBN,people,score])
        #存入数据库
        with connection.cursor() as cursor:
            sql = '''INSERT INTO douban_books (
        title,author,money,publish,pages,years,ISBN,people,score)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
            cursor.executemany(sql, data)
            connection.commit()
            del data
            time.sleep(random.randint(0, 9))  # 防止IP被封


start = time.clock()
book_info()
end = time.clock()
with connection.cursor() as cursor:
    print("Time Usage:", end -start)
    count = cursor.execute('SELECT * FROM allbooks')
    print("Total of books:", count)

if connection.open:
    connection.close()



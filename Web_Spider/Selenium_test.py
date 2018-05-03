# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup


# #模拟提交搜索
# browser = webdriver.Firefox()
# #打开请求的URL，webdriver会等到页面全部加载完毕后返回
# browser.get('http://www.baidu.com/')
# assert '百度一下，你就知道' in browser.title
# #find_element_by_*方法寻找网页元素
# elem=browser.find_element_by_name('wd')
# print(elem)
# #模拟键盘输入
# elem.send_keys('python')
# #模拟回车
# elem.send_keys(Keys.RETURN)
# #打印提交后页面信息
# #print(browser.page_source)

# #模拟登陆云平台，火灾报警远程监控系统演示
# options=webdriver.ChromeOptions()
# options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
# browser=webdriver.Chrome(chrome_options=options)
# URL='http://xiaofang.safecity119.com/'
# browser.get(URL)
# browser.maximize_window()   #把打开的浏览器最大化
# #登录
# elem1=browser.find_element_by_name('UName')
# elem2=browser.find_element_by_name('PWord')
# elem1.send_keys('bjzkadmin')
# elem2.send_keys('111111')
# elem1.send_keys(Keys.RETURN)
# sleep(3)
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

#爬取百度文库，失败，what happened！
browser=webdriver.ChromeOptions()
browser.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
driver=webdriver.Chrome(chrome_options=browser)
driver.maximize_window()
driver.get('https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html')
#点击继续阅读
elem = driver.find_elements_by_xpath('''//*[@class="foldpagewg-text-con"]/div[@class="foldpagewg-text"]''')
driver.execute_script('arguments[0].scrollIntoView();', elem[-1])
elem.click()
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

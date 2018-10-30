# -*- coding: utf-8 -*-
import re,requests
from bs4 import BeautifulSoup

def get_lt(r):
    url='https://www.csdn.net/'
    page=r.get(url=url,headers=headers)
    html=page.text
    soup=BeautifulSoup(html,'lxml')
    lt=soup.find_all(name='lt')
    return lt

headers={'User-Agent':"Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"}
r=requests.session()
lt=get_lt(r)
post_url='https://passport.csdn.net/account/login'
post_data={
    'lt':lt,
    'username':'18401570769',
    'password': 'conglingkaishi0',
    'rememberMe': 'true',

}
login_page=r.post(post_url,data=post_data,headers=headers)
login_code=login_page.text
print(login_page.status_code)
# print(login_code)





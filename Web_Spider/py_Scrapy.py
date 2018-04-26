# -*- coding: utf-8 -*-
from urllib import request
from http import cookiejar

if __name__ == '__main__':
    cookie=cookiejar.CookieJar()

    handler=request.HTTPCookieProcessor(cookie)
    opener=request.build_opener(handler)
    response=opener.open('http://www.baidu.com')
    for item in cookie:
        print('name：',item.name)
        print('value：',item.value)
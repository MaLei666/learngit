# -*- coding: utf-8 -*-
import pytesseract
from PIL import Image,ImageFilter,ImageEnhance
# from claptcha import claptcha
from selenium import webdriver
import requests
import re
from bs4 import BeautifulSoup
import cv2
import matplotlib.pyplot as plt


r=requests.get('http://127.0.0.1:8000/')
html=r.text
#找出包含图片源地址的这一段字符串
soup=BeautifulSoup(html,'lxml')
# print(soup)
img_addr='http://127.0.0.1:8000'+soup.img['src']

#以二进制的方式(content而非text)保存图片源地址内容
img=requests.get(img_addr).content
with open('img_test.png','wb') as f:
    f.write(img)

# # 简单识别
# test_image=Image.open('img_test.png')
# code=pytesseract.image_to_string(image=test_image)
# print(code)

# 稍微复杂
test_image=Image.open('img_test.png')
test_image=ImageEnhance.Contrast(test_image)
sharp_img=test_image.enhance(6.0)
sharp_img.save('img_test.png')

# 转为灰度
image_grey=sharp_img.convert('L')
image_grey=ImageEnhance.Contrast(image_grey)
img_grey=image_grey.enhance(5.0)
img_grey.save('1.png')

# 二值化
threshold = 140
table = []
for i in range(256):
 if i < threshold:
  table.append(0)
 else:
  table.append(1)
image_peak=img_grey.point(table,'1')
image_peak.save('2.png')

# # 干扰线降噪
# def interference_line(img, img_name):
#   filename =  './out_img/' + img_name.split('.')[0] + '-interferenceline.jpg'
#   h, w = img.shape[:2]
#   # ！！！opencv矩阵点是反的
#   # img[1,2] 1:图片的高度，2：图片的宽度
#   for y in range(1, w - 1):
#     for x in range(1, h - 1):
#       count = 0
#       if img[x, y - 1] > 245:
#         count = count + 1
#       if img[x, y + 1] > 245:
#         count = count + 1
#       if img[x - 1, y] > 245:
#         count = count + 1
#       if img[x + 1, y] > 245:
#         count = count + 1
#       if count > 2:
#         img[x, y] = 255
#   cv2.imwrite(filename,img)
#   return img
# im=cv2.imread('3.png')
# # im=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# interference_line(im,'2.png')

# # 滤波
# image_fil=image_peak.filter(ImageFilter.MedianFilter)
# for i in range(3):
#     image_fil=image_fil.filter(ImageFilter.MedianFilter)
# image_fil.save('3.png')
# image=Image.open('3.png')
image=Image.open('2.png')
code=pytesseract.image_to_string(image=image)
print(code)


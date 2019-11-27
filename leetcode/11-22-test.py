#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-11-22 20:26
# @file : 11-22-test.py
# @software : PyCharm
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        a = bin(n)[2:]
        print(a)
        print(a[::-1])
        b=a.zfill(32)
        c=b[::-1]
        print(c)


a=Solution()
a.reverseBits(0b00000010100101000001111010011100)
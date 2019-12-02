#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei
# @datetime : 2019-12-02 15:18
# @file : 12-02-test.py
# @software : PyCharm
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        re_list=[]
        for i in range(1,n+1):
            if i%3==0:
                if i%5!=0:
                    re_list.append('Fizz')
                else:
                    re_list.append('FizzBuzz')
            elif i%5==0:
                re_list.append('Buzz')
            else:
                re_list.append(str(i))
        return re_list

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a=list(str(n))
        b=0
        for i in a:
            b+=int(i)*int(i)
        print(b)

a=Solution()
# print(a.fizzBuzz(1))
# print(a.strStr('aaaabba','c'))
print(a.isHappy(22))
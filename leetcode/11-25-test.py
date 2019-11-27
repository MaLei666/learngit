#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-11-24 17:20
# @file : 11-25-test.py
# @software : PyCharm

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_int_list={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        unique_dict={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        int_roman=0
        for i in range(len(s)):
            if s[i:i+1] is not '' and s[i:i+1] in ['I','X','C']:
                if s[i+1:i+2] is not '' and unique_dict.get(s[i]+s[i+1]) :
                    int_roman+=unique_dict.get(s[i]+s[i+1])
                    s=s[:i]+s[i+1:]
                else:
                    int_roman+=roman_int_list.get(s[i])
            elif s[i:i + 1] is '':
                break
            else:
                int_roman += roman_int_list.get(s[i])
        print(int_roman)


s=Solution()
s.romanToInt('IVIII')

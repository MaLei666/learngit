#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-11-19 18:27
# @file : 11-19-test.py
# @software : PyCharm

class Solution(object):
    def firstUniqChar(self, s):
        min_char=len(s)
        for i in 'abc':
            num=s.find(i)
            print(num)
            if num!=-1 and num==s.rfind(i):
                min_char=min(min_char,num)
        a= min_char if min_char!=len(s) else -1
        print('===',a)

    # def firstUniqChar(self, s: str) -> int:
    #     # 先假设最小索引为最后的字符索引
    #     min_unique_char_index = len(s)
    #
    #     # 已知字符串由小写字母构成，则遍历a-z
    #     for c in "abcdefghijklmnopqrstuvwxyz":
    #         i = s.find(c)
    #         # 分别从目标的字符串头和字符串尾查找对应字母的索引；如果两索引相等，则说明是单一字符
    #         if i != -1 and i == s.rfind(c):
    #             # 更新最新的最小索引
    #             min_unique_char_index = min(min_unique_char_index, i)
    #
    #     # 如果返回值不为最后字符的索引，则返回最小索引值
    #     # 否则，根据题意，返回-1
    #     return min_unique_char_index if min_unique_char_index != len(s) else -1



a=Solution()
a.firstUniqChar("aabb")
#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-11-26 20:43
# @file : 11-26-test.py
# @software : PyCharm

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Solution1:
        # min_str=[len(s) for s in strs]
        # if len(min_str)>=1:
        #     min_str_index=min_str.index(min(min_str))
        #     min_str=strs[min_str_index]
        #     # strs.pop(min_str_index)
        #     same_str=''
        #     for i in range(len(min_str)):
        #         for m in strs:
        #             if m[:i+1]==min_str[:i+1]:
        #                 pass
        #             else:
        #                 return same_str
        #         same_str+=min_str[i]
        #     return same_str
        # else:
        #     return ''

        # Solution2:
        # same_value=''
        # for i in zip(*strs):
        #     print(i)
        #     i_set=set(i)
        #     if len(i_set)==1:
        #         same_value+=i[0]
        #     else:
        #         break
        # return same_value

        # Solution3:
        if not strs:
            return ""
        strs.sort()
        n = len(strs)
        a = strs[0]
        b = strs[n - 1]
        res = ""
        for i in range(len(a)):
            if i < len(b) and a[i] == b[i]:
                res += a[i]
            else:
                break
        return res







a=Solution()
print(a.longestCommonPrefix(["dog","racecar","car"]))


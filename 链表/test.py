#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2021/1/3 10:53 下午
# @file : test.py
# @software : PyCharm

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        last=None
        while pHead:
            tmp=pHead.next
            pHead.next=last
            last=pHead
            pHead=tmp
        return last

a
print(Solution().ReverseList())
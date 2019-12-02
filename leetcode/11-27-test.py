#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-11-27 12:03
# @file : 11-27-test.py
# @software : PyCharm
import datetime
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        else:
            num_list=[1]*n
            num_list[0],num_list[1]=0,0
            for i in range(2,int(n**0.5+1)):
                if num_list[i]==1:
                    num_list[i*i:n:i]=[0]*len(num_list[i*i:n:i])
            return sum(num_list)

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre=None
        while head:
            # 记录当前节点的下一个节点
            tmp=head.next
            # 然后将当前节点指向pre
            head.next=pre
            # pre和cur节点都前进一位
            pre=head
            head=tmp
        return pre


a=Solution()
print(a.reverseList([1,2,3,4]))
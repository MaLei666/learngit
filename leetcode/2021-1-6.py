#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2021/1/6 5:14 下午
# @file : 2021-1-6.py
# @software : PyCharm

# a=[4,5,1,6,2,7,3,8]
#
# class Solution():
#     def GetLeastNumbers_Solution(self, tinput, k):
#         if len(tinput)>=k:
#             for i in range(1, len(tinput)):
#                 while i > 0:
#                     if tinput[i] < tinput[i - 1]:
#                         tinput[i], tinput[i - 1] = tinput[i - 1], tinput[i]
#                         i -= 1
#                     else:
#                         break
#             return tinput[:k]
#         else:
#             return []
#
# print(Solution().GetLeastNumbers_Solution(a,4))

a=[1793111,1704885,1533399,1841885,1106030,]
class Solution:
    def findKth(self,a,n, K):
        self.quick(a,0,n-1)
        return a

    def quick(self,a,left,right):
        if left>=right:
            return 0
        i=left
        j=right
        base=a[left]
        while i!=j:
            if a[j]<base:
                j-=1
            elif a[j]>base:
                a[i],a[j]=a[j],a[i]
                i+=1
            if a[i]>base:
                i+=1
            elif a[i]<base:
                a[i],a[j]=a[j],a[i]
                j-=1
        self.findKth(a,left,i-1)
        self.findKth(a,i+1,right)
        return a


print(Solution().findKth(a,5,2))
# print(Solution().findKth(a,0,4,3))


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        pre = pHead
        cur = pre.next
        last = cur.next
        pre.next = None
        while last != None:
            cur.next = pre
            pre = cur
            cur = last
            last = last.next
        cur.next = pre
        return cur


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        pre = pHead
        cur = pre.next
        last = cur.next
        pre.next = None

        while last != None:
            cur.next = pre
            pre = cur
            cur = last
            last = last.next
        cur.next = pre
        return cur
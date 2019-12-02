#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-11-29 10:32
# @file : 11-29-test.py
# @software : PyCharm

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # Solution1:
        # return s.reverse()

        # Solution2:
        len_s=len(s)
        for i in range(int(len_s/2)):
            s[i],s[len_s-1-i]=s[len_s-1-i],s[i]
        return s

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        xor_result=a^b
        and_result=a&b<<1

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Solution1:
        # commen=[]
        # if len(nums1)>=len(nums2):
        #     short_list=nums2
        #     long_list=nums1
        # else:
        #     short_list=nums1
        #     long_list=nums2
        #
        # for i in short_list:
        #     if i in long_list:
        #         commen.append(i)
        #         long_list.remove(i)
        # return commen

        # for i in set(short_list):
            # short_count=short_list.count(i)
            # long_count=long_list.count(i)
            # if i in long_list:
            #     if short_count<=long_count:
            #         commen.extend([i]*short_count)
            #     else:
            #         commen.extend([i]*long_count)
        # return commen

        # Solution2:
        nums1.sort()
        nums2.sort()
        commen=[]
        i,j=0,0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                commen.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return commen

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        test=5
        nums=0
        while n//test>=1:
            nums+=n//test
            test*=5
        print(nums)

        while n>=5:
            n//=5
            nums+=n








a=Solution()
# print(a.reverseString(["h","e","l","l","o"]))
# print(a.intersect(nums1 = [1,2,3,4,2,6,9], nums2 = [1,1,3,4,2,1,2]))
print(a.trailingZeroes(200))
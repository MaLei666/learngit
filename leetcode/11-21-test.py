#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-11-21 22:50
# @file : 11-21-test.py
# @software : PyCharm

class Solution(object):
    def rotate(self, nums, k):
        for i in range(k):
            nums.insert(0,nums.pop())
        print(nums)

    def rotate2(self,nums,k):
        n = len(nums)
        k %= n
        nums[:]=nums[-k:]+nums[:-k]
        print(nums)

    def rotate3(self,nums,k):
        n = len(nums)
        k %= n
        nums[:]=nums[::-1]
        print(nums)
        nums[:k]=nums[:k][::-1]
        print(nums[:k],nums)
        nums[k:]=nums[k:][::-1]
        print(nums[k:],nums)

a=Solution()
a.rotate3([1,2,3,4,5],3)

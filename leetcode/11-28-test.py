#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-11-28 21:06
# @file : 11-28-test.py
# @software : PyCharm

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)>len(set(nums)):
            return True
        else:
            return False

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # s_list=sorted(list(s))
        # t_list=sorted(list(t))
        return sorted(s)==sorted(t)

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution1:
        # try :
        #     nums.index(0)
        #     check_num =sum(range(1, max(nums) + 1)) - sum(nums)
        #     if check_num==0:
        #         return max(nums)+1
        #     else:
        #         return check_num
        # except:
        #     return 0

        # Solution2:
        # 高斯公式
        # expect_sum=len(nums)*(len(nums)+1)//2
        # actual_sum=sum(nums)
        # return expect_sum-actual_sum

        # Solution3:
        # 任一数字，异或自己 肯定等于 0
        # 异或具有交换率->a^b^c=a^c^b
        # 通过循环1-n的列表，可知index为连续的，例如[0，1，2，3]，列表非连续，例如[4，2，0，1]
        # 两个列表中会出现重叠部分，0，1，2，均出现两次，由于交换律，可知异或后均为0，剩下的为缺失数字和n值
        # 设定一个初始值为n值，与列表n值抵消，最后所得为缺失值
        missing_num=len(nums)
        for index,value in enumerate(nums):
            missing_num ^=index^value
        return missing_num






a=Solution()
# print(a.containsDuplicate([1,2,3]))
# print(a.isAnagram(s = "rat", t = "car"))
print(a.missingNumber([0,1]))
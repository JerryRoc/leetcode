# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 16:01:06 2018

@author: pg255026
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 1

        for x in nums:
            if x != nums[n - 1]:
                nums[n] = x
                n += 1
        
        return n if nums else 0
    
    
    def removeDuplicates_myfirst(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 0:
            return length
        
        lv = nums[0]
        ii = 1
        for i in range(1,length):
            if nums[ii] == lv:
                nums.pop(ii)
            else:
                lv = nums[ii]
                ii += 1
        return ii
            



if __name__ == '__main__':
    nums = [1,1,2]
    
    ret = Solution().removeDuplicates(nums)

    print(nums[:ret])

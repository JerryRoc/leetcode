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
        length = len(nums)
        if length <= 0:
            return length
        
        lv = nums[0]
        for 



if __name__ == '__main__':
    nums = [1,1,2]
    
    ret = Solution().removeDuplicates(nums)

    print(nums[:ret])

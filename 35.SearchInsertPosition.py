# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 18:16:44 2018

@author: pg255026
"""

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums)-1
        
        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid+1
            else:
                hi = mid-1
        
        return lo if target <= nums[lo] else lo+1
    
    
    
    def searchInsert_myfirst(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        length = len(nums)
        
        for i in range(length):
            if nums[i]>=target:
                return i
            continue
        return length


if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 7
    
    ret = Solution().searchInsert(nums, target)

    out = str(ret);
    print(out)

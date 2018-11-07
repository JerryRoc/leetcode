# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:55:56 2018

@author: pg255026
"""

class Solution:
    def search_best(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = int((lo + hi) / 2)
            if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
                lo = mid + 1
            else:
                hi = mid
        return lo if target in nums[lo:lo+1] else -1
    
    def search_myfirst(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        p1,p2 = 0,len(nums)-1
        if (p2 == -1) or (target<nums[p1] and target>nums[p2]): return -1
        if nums[p1] == target:                  return p1
        if nums[p2] == target:                  return p2
        
        while p1<p2:
            mid = int((p1+p2+1)/2)
            if nums[mid] == target:
                return mid
            if (nums[p1]<nums[p2] and (target>nums[p2] or target<nums[p1])) or (nums[p1]>nums[p2] and nums[mid]<nums[p1] and target>nums[p2] and target<nums[p1]):
                return -1
            elif (p2!=mid)and((nums[p1]<nums[p2] and target>nums[p1] and target<nums[mid]) or (nums[p1]>nums[p2] and nums[mid]<nums[p1] and (target>nums[p1] or target< nums[mid])) or (nums[p1]>nums[p2] and nums[mid]>nums[p1] and target>nums[p1] and target< nums[mid])):
                p2 = mid
            else: #(nums[p1]<nums[p2] and target>nums[mid] and target<nums[p2]) or (nums[p1]>nums[p2] and ()):
                p1 = mid
        return -1
        
nums, target = [1,3], 2
rst = Solution().search_best(nums, target)
print(rst)

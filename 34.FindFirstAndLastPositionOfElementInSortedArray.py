# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 16:57:53 2018

@author: pg255026
"""

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.binarySearch(nums, target, 0, len(nums) - 1, True)
        right = self.binarySearch(nums, target, 0, len(nums) - 1, False)
        return [left, right]
        
    def binarySearch(self, nums, target, left, right, getLeft):
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if nums[mid] == target:
            if getLeft:
                if mid == 0 or (mid > 0 and nums[mid - 1] != target):
                    return mid
                return self.binarySearch(nums, target, left, mid - 1, getLeft)
            else:
                if mid == len(nums)-1 or (mid < len(nums)-1 and nums[mid + 1] != target):
                    return mid
                return self.binarySearch(nums, target, mid + 1, right, getLeft)
                    
        if nums[mid] > target:
            return self.binarySearch(nums, target, left, mid - 1, getLeft)
        if nums[mid] < target:
            return self.binarySearch(nums, target, mid + 1, right, getLeft)
    
    
    def searchRange_mysecond(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def _search(nums,target,func):
            left, right = 0, len(nums)-1
            while left<right:
                mid = int((left+right+1)/2)
                if nums[left]==target:
                    return left
                elif func(target,nums[mid]):
                    right = mid - 1
                    continue
                elif func(nums[mid],target):
                    left = mid + 1
                else: # mid == target
                    if nums[mid-1] == target:
                        right = mid - 1
                    else:
                        return mid
                    continue
            return left if left<len(nums) and nums[left]==target else -1
        if not len(nums):
            return [-1,-1]
        rst1 = _search(nums,target,lambda a,b:True if a<b else False)
        rst2 = _search(nums[::-1],target,lambda a,b:True if a>b else False)
        rst2 = len(nums)-rst2-1 if rst2 != -1 else -1
        return [rst1,rst2]
    
    def searchRange_myfirst(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def _search(nums,target):
            left, right = 0, len(nums)-1
            while left<right:
                mid = int((left+right+1)/2)
                if nums[left]==target:
                    return left
                elif target < nums[mid]:
                    right = mid - 1
                    continue
                elif target > nums[mid]:
                    left = mid + 1
                else: # mid == target
                    if nums[mid-1] == target:
                        right = mid - 1
                    else:
                        return mid
                    continue
            return left if left<len(nums) and nums[left]==target else -1
        def _search2(nums,target):
            left, right = 0, len(nums)-1
            while left<right:
                mid = int((left+right+1)/2)
                if nums[left]==target:
                    return left
                elif target > nums[mid]:
                    right = mid - 1
                    continue
                elif target < nums[mid]:
                    left = mid + 1
                else: # mid == target
                    if nums[mid-1] == target:
                        right = mid - 1
                    else:
                        return mid
                    continue
            return left if left<len(nums) and nums[left]==target else -1
        if not len(nums):
            return [-1,-1]
        rst1 = _search(nums,target)
        rst2 = _search2(nums[::-1],target)
        rst2 = len(nums)-rst2-1 if rst2 != -1 else -1
        return [rst1,rst2]
    


nums = [5,7,7,8,8,10]
target = 8

rst = Solution().searchRange(nums,target)
print(rst)
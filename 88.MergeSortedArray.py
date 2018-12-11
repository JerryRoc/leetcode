# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 18:27:04 2018

@author: pg255026
"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()
        return nums1
        
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

rst = Solution().merge( nums1, m, nums2, n)
print(rst)
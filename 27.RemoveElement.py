# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 17:17:29 2018

@author: pg255026
"""

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for v in nums:
            if v == val:
                pass
            else:
                nums[i] = v
                i += 1
        
        
        return i


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return nums[:len_of_list]



if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    
    ret = Solution().removeElement(nums, val)

    out = integerListToString(nums, len_of_list=ret)
    print(out)

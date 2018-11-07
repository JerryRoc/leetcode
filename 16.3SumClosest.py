# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 09:38:45 2018

@author: pg255026
"""

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = []
        nums.sort()
        for i,num in enumerate (nums[0:-2]):
            l = i + 1
            r  = len(nums) - 1
            if nums[l] + nums[l + 1] + num > target:
                res.append(nums[l] + nums[l + 1] + num)
            elif nums[r] + nums[r - 1] + num < target:
                res.append(nums[r] + nums[r - 1] + num)
            else:
                while l < r:
                    res.append(nums[l] + nums[r] + num)
                    if nums[l] + nums[r] + num < target:
                        l += 1
                    elif nums[l] + nums[r] + num > target:
                        r -= 1
                    else:
                        return target
        res.sort(key=lambda x:abs(x-target))
        return res[0]
    
    def threeSumClosest_myfirst(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L = len(nums)
        nums.sort()
        rst = nums[0]+nums[1]+nums[-1]
        
        for fixed in range(L-2):
            i, j = fixed+1, L-1
            while i<j:
                tmp = nums[fixed]+nums[i]+nums[j]
                if abs(target-tmp)<abs(target-rst):
                    rst = tmp
                if tmp-target == 0:
                    return target
                if tmp-target > 0:
                    j -= 1
                else:
                    i += 1
        return rst
                    
        
        
        


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    
    ret = Solution().threeSumClosest(nums, target)

    out = str(ret);
    print(out)

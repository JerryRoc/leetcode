# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 10:22:42 2018

@author: pg255026
"""

class Solution:
    def fourSum(self, nums, target):  
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        def findNSum(l,r,target,N,result,rst):
            if N>r-l+1 or N<2 or target < nums[l]*N or target > nums[r]*N:
                return
            if N == 2:
                while l<r:
                    s = nums[l]+nums[r]
                    if s == target:
                        rst.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]: # drop duplicate inside
                            l += 1
                    elif s<target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l,r-N+2):
                    if i == l or (i > l and nums[i-1] != nums[i]): # drop duplicate outside
                        findNSum(i+1,r,target-nums[i],N-1,result+[nums[i]],rst)
        rst = []
        findNSum(0, len(nums)-1, target, 4, [], rst)
        return rst
        
        
        
    def fourSum_myfirst(self, nums, target):  # Time Limit Exceeded at first
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        length = len(nums)
        rst = []
        for ind1 in range(length-3):
            if ind1>0 and nums[ind1]==nums[ind1-1]:
                    continue
            num1 = nums[ind1]
            for ind2 in range(ind1+1,length-2):
                if ind2>ind1+1 and nums[ind2]==nums[ind2-1]:
                    continue
                num2 = nums[ind2]
                ind3,ind4 = ind2+1,length-1
                while ind3<length-1 and ind4>ind2 and ind4>ind3:
                    num3,num4 = nums[ind3],nums[ind4]
                    if target-num1-num2 > num4*2 or target-num1-num2 < num3*2: # break time limit Exceeded
                        break
                    if target == num1+num2+num3+num4 and [num1,num2,num3,num4] not in rst:
                        rst.append([num1,num2,num3,num4])
                        ind3 += 1        # else condition will cover
                        while ind3<ind4 and nums[ind3]==nums[ind3-1]:
                            ind3 += 1
                    elif target < num1+num2+num3+num4:
                        ind4 -= 1
                    else:
                        ind3 += 1
        
        
        return rst


if __name__ == '__main__':
    nums = [-3,-2,-1,0,0,1,2,3]
    target = 0
    
    rst = Solution().fourSum(nums,target)
    print(str(rst).replace('], [',']\n['))
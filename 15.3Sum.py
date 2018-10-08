# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 14:01:19 2018

@author: pg255026
"""

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res
        
        
    def threeSum_myfirst(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        
        dic = {}
        for num in nums:
            dic[num] = 1 if num not in dic else dic[num]+1
        
        def _2sum(d,target):
            
            rst = [[int(target/2),int(target/2)]] if target%2 == 0 and int(target/2) in d and d[int(target/2)]>1 else []
            
            for k in d:
                if k<target/2 and target-k in d:
                    rst.append([k,target-k])
            return rst
        
        rst = []
        for k in list(dic.keys()):
            if dic[k] == 1:
                dic.pop(k)
            else:
                dic[k] = dic[k]-1
            rst = rst + [[k,i,j] for i,j in _2sum(dic,0-k)]
            if k in dic:
                dic.pop(k)
        return rst
            
        
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    rst = Solution().threeSum(nums)
    print(str(rst))
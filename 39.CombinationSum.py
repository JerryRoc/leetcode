# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 18:12:19 2018

@author: pg255026
"""

class Solution:
    def NSum(self,candidates,target,N,temp,result):
        if N == 1:
            if target in candidates:
                temp.append(target)
                result.append(temp)
            return
        
        elif N == 2:
            #candidates = sorted(list(set(candidates)))
            i,j = 0,len(candidates)-1
            if target<2*candidates[i] or (j>0 and (target > 2*candidates[j])):
                return
            while i<=j:
                if target == candidates[i]+candidates[j]:
                    result.append(temp + [candidates[i],candidates[j],])#if temp not in result: result.append(temp)
                    i += 1
                elif target > candidates[i]+candidates[j]:
                    i += 1
                else:
                    j -= 1
            return
        
        else: #N >2
            #candidates = sorted(list(set(candidates)))
            for i in range(len(candidates)):
                if candidates[i]*N<=target:
                    self.NSum(candidates[i:],target-candidates[i],N-1,temp+[candidates[i],],result)
            return
                    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        rst = []
        candidates = sorted(list(set(candidates)))
        
        for n in range(1,target//min(candidates)+1):
            if candidates[0]*n<=target:
                self.NSum(candidates,target,n,[],rst)
        return rst

candidates = [3,2,6,7]
target = 11
rst = Solution().combinationSum(candidates,target)
print(rst)
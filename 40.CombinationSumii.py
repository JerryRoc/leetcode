# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:42:57 2018

@author: pg255026
"""

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        rst = []
        
        def dfs(remain,ele,idx_can):
            if remain == 0:
                rst.append(ele)
                return
            
            for i in range(idx_can,len(candidates)):
                can = candidates[i]
                if i>idx_can and can == candidates[i-1]:
                    continue
                if remain >= can:
                    dfs(remain-can,ele+[can,],i+1)
                else:
                    return
                pass
            return
        
        dfs(target,[],0)
        return rst
    
    def combinationSum2_mysecond(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        rst = []
        
        def dfs(remain,ele,candidates):
            if not candidates:
                return
            for i in range(len(candidates)):
                can = candidates[i]
                if (i-1 >= 0) and (can == candidates[i-1]):
                    continue
                if remain == can:
                    rst.append(ele+[can,])
                elif remain-can > 0:
                    dfs(remain-can,ele+[can,],candidates[i+1:])
                else: #<0
                    return
            return
        
        dfs(target,[],candidates)
        return rst
    
    def combinationSum2_myfirst(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        rst = []
        
        def dfs(remain,ele,candidates):
            if not candidates:
                return
            for i in range(len(candidates)):
                can = candidates[i]
                if (i-1 >= 0) and (can == candidates[i-1]):
                    continue
                if remain == can:
                    rst.append(ele+[can,])
                elif remain-can > 0:
                    dfs(remain-can,ele+[can,],candidates[i+1:])
            return
        
        dfs(target,[],candidates)
        return rst
        



candidates, target = [10,1,2,7,6,1,5], 8
rst = Solution().combinationSum2(candidates, target)
print(rst)
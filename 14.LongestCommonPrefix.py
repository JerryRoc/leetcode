# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 14:41:41 2018

@author: pg255026
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(len(strs)==0):
            return ''
        if(len(strs)==1):
            return strs[0]
        
        def f_mincom(w1,w2):
            ind = len(w1)
            while w1[:ind] != w2[:ind]:
                ind -= 1
            return w1[:ind]
        
        l = sorted(strs,key=len)
        compre = l[0]
        
        for word in l[1:]:
            compre = f_mincom(compre,word)
        return compre


l = ["flower","flow","flight"]
rst = Solution().longestCommonPrefix(strs = l)
print(rst)
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 17:22:54 2018

@author: pg255026
"""

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=='':
            return 0
        
        l = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i+l] == needle:
                    return i
            
        return -1
    
    
    
    def strStr_myfirst(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=='':
            return 0
        
        l = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+l] == needle:
                return i
            
        return -1


if __name__ == '__main__':
    haystack = 'hello'
    needle = 'll'
    
    ret = Solution().strStr(haystack, needle)

    out = str(ret);
    print(out)
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 13:49:32 2018

@author: pg255026
"""

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda x, y: x*26 + y, [ord(c) - ord('A') + 1 for c in s]) # from functools import reduce # PY3
    
    def titleToNumber_myfirst(self, s):
        """
        :type s: str
        :rtype: int
        """
        L, rst = len(s), 0
        
        for i in range(L):
            rst += (ord(s[i])-64)*26**(L-i-1)
        return rst

if __name__ == '__main__':
    s = 'ZY'
    
    ret = Solution().titleToNumber(s)

    out = str(ret);
    print(out)

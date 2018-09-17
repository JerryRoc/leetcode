# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 14:58:22 2018

@author: pg255026
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for c in s:
            if c in list('([{'):
                stack.append(c)
            else:
                if len(stack)==0:
                    return False
                c2 = stack.pop()
                if (c2+c) in ['()','[]','{}']:
                    continue
                else:
                    return False
        return True if len(stack)==0 else False
        

def stringToString(input):
    return input


if __name__ == '__main__':
    s = stringToString(']');
    
    ret = Solution().isValid(s)

    out = (ret);
    print(out)

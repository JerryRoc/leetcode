#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 22:16:19 2018

@author: gret
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            out = int(''.join(reversed(str(x*-1))))
            return 0 if (out>2**31-1)|(out<-2**31) else -1*out
        else:
            out = int(''.join(reversed(str(x))))
            return 0 if (out>2**31-1)|(out<-2**31) else out
        

    
    def reverse_myfirst(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        elif (x>2**31-1)|(x<-2**31):
            return 0
        elif x<0:
            flag = 1
            inp = abs(x)
        else:
            flag = 0
            inp = x
        
        s=0
        while inp:
            s = s*10 + inp%10
            inp = int(inp/10)
        if (s>2**31-1)|(s<-2**31):
            return 0
        return s if flag==0 else -s
        

if __name__ == '__main__':
    x = int('1534236469');
    
    ret = Solution().reverse(x)

    out = str(ret);
    print(out)

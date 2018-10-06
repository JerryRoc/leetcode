#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 11:49:19 2018

@author: gret
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n-1)  :
            c = s[0]
            cnt = 1
            out = ''
            for i in range(1,len(s)):
                if s[i]==c:
                    cnt += 1
                else:
                    out = out+str(cnt)+str(c)
                    cnt = 1
                    c = s[i]
            
            s = out+str(cnt)+str(c)
        return s
        
        
    def countAndSay_myfirst(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        else:
            s = self.countAndSay(n-1)
            
            c = s[0]
            cnt = 1
            out = ''
            for i in range(1,len(s)):
                if s[i]==c:
                    cnt += 1
                else:
                    out = out+str(cnt)+str(c)
                    cnt = 1
                    c = s[i]
            
            return out+str(cnt)+str(c)
        


if __name__ == '__main__':
            n = 5
            
            ret = Solution().countAndSay(n)

            out = str(ret)
            print(out)

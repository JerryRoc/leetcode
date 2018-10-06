#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 23:04:38 2018

@author: gret
"""

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {
                'M':1000,
                'D':500,
                'C':100,
                'L':50,
                'X':10,
                'V':5,
                'I':1}
        out = d[s[0]]
        pre = out
        
        if len(s)==1:
            return out
        
        for c in s[1:]:
            num = d[c]
            out = out+num
            if num>pre:
                out = out-2*pre
            pre = num
        
        return out
                    
    
    
    def romanToInt_myfirst(self, s):
        """
        :type s: str
        :rtype: int
        """
        def trans(s):
            d = {
                    'M':1000,
                    'D':500,
                    'C':100,
                    'L':50,
                    'X':10,
                    'V':5,
                    'I':1}
            return d[s]
        inp = s
        order = 'MDCLXVI'
        out = 0
        for c in order:
            while inp.find(c)>-1:
                if len(inp)==1:
                    out = out + trans(inp)
                    break
                ind = inp.find(c)
                if ind<0:
                    continue
                if ind==0:
                    out = out + trans(inp[0])
                    
                else:
                    out = out + trans(inp[ind])
                    out = out - trans(inp[0])*ind
                inp = inp[ind+1:]
                    
        return out

def stringToString(input):
    return input


if __name__ == '__main__':
    s = stringToString('MCMXCIV');
    
    ret = Solution().romanToInt(s)
    
    out = str(ret);
    print(out)

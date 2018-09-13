#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 22:52:05 2018

@author: gret
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)==str(x)[::-1]
    
    def isPalindrome_myfirst(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        s1 = ''.join(reversed(s))
        return s==s1

def main():
    x = int('-121');
    
    ret = Solution().isPalindrome(x)

    out = (ret);
    print(out)

if __name__ == '__main__':
    main()
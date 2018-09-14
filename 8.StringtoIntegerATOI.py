# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 15:11:45 2018

@author: pg255026
"""

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        return 0




if __name__ == '__main__':
    str = '123 with word';
    
    ret = Solution().myAtoi(str)

    out = str(ret);
    print(out)

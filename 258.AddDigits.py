# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 15:12:55 2018

@author: pg255026
"""

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        else:
            sum_ = 0
            while num>0:
                sum_ += num%10
                num = int(num/10)
            return self.addDigits(sum_)

num = 38
rst = Solution().addDigits(num)
print(rst)
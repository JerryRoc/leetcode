# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 15:56:17 2018

@author: pg255026
"""
import time

def timeit(func):
    def wrapper(*argv,**argc):
        tm = time.time()
        rst = func(*argv,**argc)
        print('%fs'%(time.time()-tm))
        return rst
    return wrapper

class Solution:
    @timeit
    def divide_bestread(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

    @timeit
    def divide_mysecond(self, dividend, divisor): # fastest
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = 1 if (dividend>0 and divisor>0) or(dividend<0 and divisor<0) else -1
        dividend, divisor, temp,i, rst = abs(dividend), abs(divisor), abs(divisor),1, 0
        while dividend >= divisor:
            if dividend>=temp:
                dividend -= temp
                rst += i
                i <<= 1
                temp <<= 1
            else:
                i >>= 1
                temp >>= 1
        return max(min(flag*rst,2147483647),-2147483648)
    
    @timeit
    def divide_myfirst(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        flag = 1 if (dividend>0 and divisor>0) or(dividend<0 and divisor<0) else -1
        dividend, divisor, rst = abs(dividend), abs(divisor), 0
        if divisor == 1:
            rst = dividend
        else:
            while dividend > 0:
                 rst += 1
                 dividend -= divisor
            rst = rst if dividend == 0 else rst-1
        return max(min(flag*rst,2147483647),-2147483648)
        

dividend, divisor = 214748364700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,1
rst = Solution().divide_mysecond(dividend, divisor)
print(rst)
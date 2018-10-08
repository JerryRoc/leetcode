# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 11:42:09 2018

@author: pg255026
"""

import time

def timeit(func):
    def wrapper(*args,**kw):
        st = time.time()
        rst = func(*args,**kw)
        print('Elasped Time: %.3fs'%(time.time()-st))
        return rst
    return wrapper


class Solution:
    @timeit
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M" , "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        res = M[int(num/1000)] + C[int((num%1000)/100)] + X[int((num%100)/10)] + I[int(num%10)]
        return res
    
    def intToRoman_myfirst(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = {
                1   :'I',
                4   :'IV',
                5   :'V',
                9   :'IX',
                10  :'X',
                40  :'XL',
                50  :'L',
                90  :'XC',
                100 :'C',
                400 :'CD',
                500 :'D',
                900 :'CM',
                1000:'M',}
        rst = ''
        for _ in range(len(dic)):
            digit = max(dic)
            char = dic.pop(digit)
            if digit <= num:
                it = num//digit
                num = num%digit
                rst = rst+char*it
        return rst
            
            

if __name__ == '__main__':
    num = 1994
    
    ret = Solution().intToRoman(num)

    out = (ret);
    print(out)

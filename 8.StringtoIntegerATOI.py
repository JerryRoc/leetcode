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
        s = str.strip()
        if not s:
            return 0
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        else:
            sign = 1
        res = 0
        for i, ch in enumerate(s):
            if not ch.isdigit():
                break
            else:
                res = res*10 + int(ch)
        if sign*res <= -2**31:
            return -2**31
        elif sign*res >= 2**31-1:
            return 2**31-1
        else:
            return sign*res
    
    
    
    
    
    
    
    
    
    def myAtoi_myfirst(self, str):
        """
        :type str: str
        :rtype: int
        """
        if (len(str) == 0): 
            return 0
        
        flag = 0
        rst = ''
        for c in str:
            if (c==' '):
                #print('c==space')
                if flag == 0:
                    continue
                else:
                    break
            if c in list('+-'):
                if flag == 0:
                    flag = 1
                    rst = rst+c
                    continue
                else:
                    break
            if (c in list('0123456789')):
                #print('c==num')
                flag=2
                rst = rst+c
                continue
            else:
                #print('c==chara')
                if flag==0:
                    return 0
                else:
                    break
        
        try:
            num = int(rst)
        except:
            num=0
        
        if num<=-2**31:
            return -2**31
        elif num>=2**31-1:
            return 2**31-1
        else:
            return num
                




if __name__ == '__main__':
    s = '-5-';
    
    ret = Solution().myAtoi(s)

    out = str(ret);
    print(out)

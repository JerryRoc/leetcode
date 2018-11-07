# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 09:53:50 2018

@author: pg255026
"""

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        dic = {
                '2':'abc',
                '3':'def',
                '4':'ghi',
                '5':'jkl',
                '6':'mno',
                '7':'pqrs',
                '8':'tuv',
                '9':'wxyz',}
        rst = ['']
        for c in digits:
            rst = [tmp+number for tmp in rst for number in dic[c]]
        return rst
        

if __name__ == '__main__':
    digits = "23"
    
    ret = Solution().letterCombinations(digits)

    out = str(ret);
    print(out)
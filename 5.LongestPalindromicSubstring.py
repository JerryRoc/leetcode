# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 17:42:08 2018

@author: pg255026
"""


"""
palindromic means?
"""
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <1:
            return ""
        
        # hash
        dictA = dict()
        for i,c in enumerate(s):
            if c in dictA:
                dictA[c] = dictA[c]+[i,]
            else:
                dictA[c] = [i,]
        
        best = -1
        pos = []
        for c,inds in dictA.items():
            if inds[-1] - inds[0]>best:
                pos = [inds[-1] , inds[0]]
                best = inds[-1] - inds[0]
        if len(pos)>0:
            return s[pos[1]:(pos[0]+1)]
        else:
            return ''

def stringToString(input):
    return input


if __name__ == '__main__':
    s = stringToString('babad');
    
    ret = Solution().longestPalindrome(s)

    out = (ret);
    print(out)



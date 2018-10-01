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
        if s == s[::-1]: # s is already a palindrome
            return s
        Len   = 1
        start = 0
        for i in range(1, len(s)): # index values of string
            p1, p2 = i - Len, i + 1  
            if p1 >= 1:
                temp = s[p1 - 1:p2]
                if temp == temp[::-1]:
                    start = p1 - 1
                    Len += 2
                    continue
            # even?
            if p1 >= 0:
                temp = s[p1:p2]
                if temp == temp[::-1]:
                    start = p1
                    Len += 1
        return s[start:start + Len]
        
    def longestPalindrome_mysecond_fromcenter(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if s == s[::-1]:
            return s
        
        def _longest_palindrom(s,i,j):
            if s[i] != s[j]:
                return 1,i,i
            while (s[i]==s[j]):
                i -= 1
                j += 1
                if (i<0)|(j>=len(s)):
                    break
            i,j = i+1,j-1
            return j-i+1,i,j
        
        best = s[0]
        for i in range(1,length):
            len_odd, ind1_odd, ind2_odd    = _longest_palindrom(s,i,i)
            len_even, ind1_even, ind2_even = _longest_palindrom(s,i-1,i)
            Len = max(len_odd,len_even)
            if Len >len(best):
                best = s[ind1_odd:(ind2_odd+1)] if len_odd>len_even else s[ind1_even:(ind2_even+1)]
            
        return best
    
    def longestPalindrome_myfirst(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length <=1:
            return s
        
        best = s[0]
        for i in range(1,length):
            #odd 
            delta = 1
            while (i-delta>=0)&(i+delta<length):
                if s[i-delta] != s[i+delta]:
                    break
                else:
                    if delta*2+1 > len(best):
                        best = s[(i-delta):(i+delta+1)]
                    delta += 1
            # even
            delta = 0
            while (i-delta-1>=0)&(i+delta<length):
                if s[i-delta-1] != s[i+delta]:
                    break
                else:
                    if delta*2+2 > len(best):
                        best = s[(i-delta-1):(i+delta+1)]
                    delta += 1
            pass
            
        return best
        
        

def stringToString(input):
    return input


if __name__ == '__main__':
    s = stringToString('bb');
    
    ret = Solution().longestPalindrome_mysecond_fromcenter(s)

    out = (ret);
    print(out)



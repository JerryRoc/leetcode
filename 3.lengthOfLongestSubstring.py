# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 11:42:40 2018

@author: pg255026
"""

class Solution:
    def lengthOfLongestSubstring(self, s): #_sliding_opt2
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0 :
            return 0
        
        winner,i,j = 0,0,0
        dictA = {}
        
        while (i<length)&(j<length):
            if s[j] not in dictA:
                dictA[s[j]] = j
                j+=1
                winner = max(winner,j-i)
                
            else:
                i = max(i,dictA[s[j]]+1)
                dictA[s[j]] = j
                j+=1
                winner = max(winner,j-i)
        return winner
    
    def lengthOfLongestSubstring_best(self, s): 
        """
        :type s: str
        :rtype: int
        """    
        s_letter = set([w for w in s])
        s_dict = dict.fromkeys(s_letter,-1)
        tmp_len = 0
        record_len = 0
        start_point = -1
        for i,le in enumerate(s):
            tmp_point = s_dict[le]
            if tmp_point <= start_point:
                s_dict[le] = i
                tmp_len += 1
            else:
                start_point = tmp_point
                s_dict[le] = i
                if tmp_len > record_len:
                    record_len = tmp_len
                tmp_len = i-tmp_point
        if tmp_len > record_len:
            record_len = tmp_len
        return record_len
    
    def lengthOfLongestSubstring_sliding_opt(self, s): 
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0 :
            return 0
        
        winner,i,j = 0,0,0
        dictA = {}
        
        while (i<length)&(j<length):
            if s[j] not in dictA:
                dictA[s[j]] = j
                j+=1
                winner = max(winner,j-i)
            else:
                for ii in range(i,dictA[s[j]]):
                    dictA.pop(s[ii])
                i = dictA[s[j]]+1
                dictA[s[j]] = j
                j+=1
        return winner
    
    
    
    def lengthOfLongestSubstring_sliding(self, s): 
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0 :
            return 0
        
        winner,i,j = 0,0,0
        setA = set()
        
        while (i<length)&(j<length):
            if s[j] not in setA:
                setA.add(s[j])
                j+=1
                winner = max(winner,j-i)
            else:
                setA.add(s[j])
                setA.remove(s[i])
                i+=1
        return winner
        
        
        
        
    def lengthOfLongestSubstring_slower(self, s): 
        """
        :type s: str
        :rtype: int
        """
        winner = 0
        ###### char ind  len
        cand = ['',dict(),0]
        
        for c in list(s):
            if c not in cand[1]:
                cand[0] = cand[0] + c
                cand[1][c] = cand[2]
                cand[2] += 1
            elif cand[1][c] == cand[2]-1:
                winner = max(cand[2],winner)
                cand = [c,{c:0},1]
            else:
                winner = max(cand[2],winner)
                ind = cand[1][c]
                cand[0] = cand[0][(ind+1):]+c
                cand[2] = len(cand[0])
                cand[1] = dict(zip(cand[0],range(cand[2])))
        
        return max(winner,len(cand[0]))
    
    
    def lengthOfLongestSubstring_slow(self, s): # too slow
        """
        :type s: str
        :rtype: int
        """
        winner = 0
        cand = ['',set()]
        
        for c in list(s):
            print(c,cand)
            if c not in cand[1]:
                cand[0] = cand[0] + c
                cand[1].add(c)
            else:
                length = len(cand[0])
                ind = cand[0].find(c)
                winner = max(winner,length)
                cand[0] = c if c == cand[0][-1] else cand[0][(ind+1):]+c
                cand[1] = set(cand[0])
            print(cand)
        
        return max(winner,len(cand[0]))

def stringToString(input):
    return input


if __name__ == '__main__':
    s = stringToString("tmmzuxt");
    
    ret = Solution().lengthOfLongestSubstring(s)

    out = str(ret);
    print(out)

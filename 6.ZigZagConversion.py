# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 17:33:00 2018

@author: pg255026
"""

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        strs = ["" for i in range(numRows)]
        zigzag = True
        j = -1
        for c in s:
            j += 1 if zigzag else -1
            strs[j] += c
            if j == numRows - 1:
                zigzag = False
            if j == 0:
                zigzag = True
        res = ""
        return res.join(strs)
        
        
        
    def convert_myfirst(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        if (length <2)|(numRows==1):
            return s
        
        ind_add = 1
        l = [(0,(0,0))] # orig_index,new_index
        last_index = (0,0)
        
        for i in range(1,length):
            if ((ind_add > 0)&(last_index[0]<numRows-1))|((ind_add < 0)&(last_index[0]==0)):
                ind_add = 1
                last_index = (last_index[0]+1,last_index[1])
                l.append((i,last_index))
            else:
                ind_add = -1
                last_index = (last_index[0]-1,last_index[1]+1)
                l.append((i,last_index))
                    
        rst = ''.join([s[i] for i,j in sorted(l,key=lambda x:x[1][0])])
        return rst
        
        
        
        



if __name__ == '__main__':
    s = 'PAYPALISHIRING'
    numRows = 4
    
    ret = Solution().convert(s, numRows)

    out = (ret);
    print(out)

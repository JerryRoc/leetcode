# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 15:28:20 2018

@author: pg255026
"""
import  json

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        s1 = len(nums1)
        s2 = len(nums2)
        
        flag = 0 if (s1+s2) %2 ==0 else 1
        st = int((s1+s2-1)/2) if flag else int((s1+s2)/2-1)
        ed = int((s1+s2-1)/2) if flag else int((s1+s2)/2)
        
        if (s1 == 0):
            return (nums2[st]+nums2[ed])/2
        
        if (s2 == 0):
            return (nums1[st]+nums1[ed])/2
        
        i = 0
        p1=0
        p2=0
        data = []
        while i<= ed:
            if (p1<s1)&(p2<s2):
                if nums1[p1]>nums2[p2]:
                    if i>=st:
                        data.append(nums2[p2])
                    p2+=1
                else:
                    if i>=st:
                        data.append(nums1[p1])
                    p1+=1
            else:
                if p1<s1:
                    
                    if i>=st:
                        data.append(nums1[p1])
                    p1+=1
                else:
                    
                    if i>=st:
                        data.append(nums2[p2])
                    p2+=1
            i+=1
        if flag:
            return data[0]
        else:
            return (data[0]+data[1])/2

def stringToIntegerList(input):
    return json.loads(input)

if __name__ == '__main__':
    nums1 = stringToIntegerList('[1]');
    nums2 = stringToIntegerList('[2,3,4,5]');
    
    ret = Solution().findMedianSortedArrays(nums1, nums2)
    
    out = str(ret);
    print(out)

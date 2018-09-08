# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 09:55:54 2018

@author: pg255026
"""

def twosum(nums,target):
    dictA = {}
    for i,num in enumerate(nums):
        if num in dictA:
            dictA[num] = dictA[num]+[i,]
        else:
            dictA[num] = [i,]
    
    if (target%2 == 0) & (int(target/2) in dictA):
        if len(dictA[int(target/2)]) == 2:
            return dictA[int(target/2)]
    
    for num in dictA:
        if num!= target/2:
            if target-num in dictA:
                return dictA[num]+dictA[target-num]


if __name__ == '__main__':
    nums = [-18,12,3,0]
    target = -6
    
    print(twosum(nums,target))
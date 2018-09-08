# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 10:31:29 2018

@author: pg255026
"""
import json

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2): 
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummay = ListNode(0)
        current = dummay
        
        p,q = l1,l2
        carry = 0
        
        while(p != None)|(q != None):
            sum_ = (0 if p ==None else p.val) + (0 if q == None else q.val) + carry
            carry = 1 if sum_ > 9 else 0
            current.next = ListNode(sum_-10 if carry else sum_)
            current = current.next
            p = p if p == None else p.next
            q = q if q == None else q.next
        
        if carry:
            current.next = ListNode(1)
        else:
            pass
        
        return dummay.next
        
    
    
    
    
    def addTwoNumbers_iter(self, l1, l2): # too slow
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(l1 == None)&(l2 == None):
            return None
        sum_ = (0 if l1 == None else l1.val) + (0 if l2 == None else l2.val)
        if sum_ > 9:
            rst = ListNode(sum_-10)
            if l1.next == None:
                l1.next = ListNode(1)
            else:
                l1.next.val = l1.next.val +1
            rst.next = self.addTwoNumbers(l1.next if l1 != None else l1,l2.next if l2 != None else l2)
        else:
            rst = ListNode(sum_)
            rst.next = self.addTwoNumbers(l1.next if l1 != None else l1,l2.next if l2 != None else l2)
        return rst
    
    def addTwoNumbers_wrong(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # create result head
        sum_ = l1.val+l2.val
        if sum_ > 9:
            flag=1
            rst = ListNode(sum_-10)
        else:
            flag=0
            rst = ListNode(sum_)
        
        # create centre node
        v1,v2,v0 = l1.next,l2.next,rst
        while (v1 != None) & (v2 != None):
            sum_ = v1.val+v2.val+flag
            if sum_ > 9:
                flag=1
                v0.next = ListNode(sum_-10)
            else:
                flag=0
                v0.next = ListNode(sum_)
            v1,v2,v0 = v1.next,v2.next,v0.next
        
        # create final node
        if (v1 == None) & (v2 == None):
            if flag == 0:
                return rst
            else:
                v0.next = ListNode(1)
                return rst
        
        if v1 == None:
            if (v2.val == 9) & (flag == 1):
                v0.next = ListNode(0)
                v0.next.next = ListNode(1)
            else:
                v0.next = ListNode(v2.val+flag)
        else:
            if (v1.val == 9) & (flag == 1):
                v0.next = ListNode(0)
                v0.next.next = ListNode(1)
            else:
                v0.next = ListNode(v1.val+flag)
        return rst
                

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"



if __name__ == '__main__':


    l1 = stringToListNode('[9,9,9]');
    l2 = stringToListNode('[1]');
            
    ret = Solution().addTwoNumbers(l1, l2)

    out = listNodeToString(ret);
    print(out)

        
        
        
        
        
        
        
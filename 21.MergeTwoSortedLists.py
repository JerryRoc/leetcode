# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 15:13:13 2018

@author: pg255026
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = tail = ListNode(None)
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next, tail, l1 = l1, l1, l1.next
            else:
                tail.next, tail, l2 = l2, l2, l2.next
        tail.next = (l1 or l2) if (l1 or l2) else None
        return dummy.next
        
    
    def mergeTwoLists_my_first(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        ptr1 = l1
        ptr2 = l2
        
        while (ptr1 != None)|(ptr2 != None):
            num1 = None if ptr1 == None else ptr1.val
            num2 = None if ptr2 == None else ptr2.val
            
            if (num1!=None)&(num2!=None):
                if num1<num2:
                    ptr.next = ListNode(num1)
                    ptr = ptr.next
                    ptr1 = ptr1.next
                else:
                    ptr.next = ListNode(num2)
                    ptr = ptr.next
                    ptr2 = ptr2.next
            elif num1!=None:
                ptr.next = ListNode(num1)
                ptr = ptr.next
                ptr1 = ptr1.next
            else:
                ptr.next = ListNode(num2)
                ptr = ptr.next
                ptr2 = ptr2.next
                
        
        return dummyRoot.next

def stringToIntegerList(input):
    if input.find('->')>-1:
        return [int(s_n) for s_n in input.split('->')]
    else:
        return [int(input)]

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
    l1 = stringToListNode('-9->3');
    l2 = stringToListNode('5->7');
    
    ret = Solution().mergeTwoLists(l1, l2)

    out = listNodeToString(ret);
    print(out)

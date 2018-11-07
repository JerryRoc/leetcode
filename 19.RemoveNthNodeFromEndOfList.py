# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 10:51:11 2018

@author: pg255026
"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyRoot = ListNode(0)
        dummyRoot.next = head
        
        p1,p2 = dummyRoot,dummyRoot
        
        for i in range(n):
            p1 = p1.next
            
        while p1.next != None:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return dummyRoot.next
        
        
        

def stringToListNode(numbers):
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
    head = stringToListNode([1,2,3,4,5])
    n = 1
    
    rst = Solution().removeNthFromEnd(head,n)
    print(listNodeToString(rst))
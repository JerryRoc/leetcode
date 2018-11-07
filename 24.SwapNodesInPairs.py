# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 15:31:27 2018

@author: pg255026
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyRoot = ListNode(0)
        dummyRoot.next = head
        p = dummyRoot
        
        while p.next and p.next.next is not None:
            p1,p2 = p.next, p.next.next
            p.next, p2.next, p1.next = p2, p1, p2.next
            p = p.next.next
        return dummyRoot.next

def stringToListNode(numbers):
    # Generate list from the input
#    numbers = stringToIntegerList(input)

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
    head = stringToListNode([1,2,3,4]);
    ret = Solution().swapPairs(head)
    out = listNodeToString(ret);
    print(out)

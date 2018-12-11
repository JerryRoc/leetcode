# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 16:43:32 2018

@author: pg255026
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def list2node(list):
    dummy = ListNode(0)
    p = dummy
    for num in list:
        p.next = ListNode(num)
        p = p.next
    return dummy.next
        
def node2list(node):
    p = ListNode(0)
    p.next = node
    
    rst,i = [],0
    while p.next and i<10:
        rst.append(p.next.val)
        p = p.next
        i += 1
    return rst
    

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k<2:
            return head
        
        ret = head
        for i in range(k-1):
            ret = ret.next
            if ret is None:
                return head
            
        prev, current = None, head
        for i in range(k):
            _next = current.next
            current.next = prev
            prev = current
            current = _next
        
        head.next = self.reverseKGroup(current, k)
        return ret
    
    def list2node_r(self,list):
        dummy = ListNode(0)
        p = dummy
        for num in list[::-1]:
            p.next = ListNode(num)
            p = p.next
        return dummy.next,p
    
    def reverseKGroup_myfirst(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k==1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        p_pre,p = dummy,dummy
        stack,stack_i = [],0
        
        while p.next:
            stack.append(p.next.val)
            stack_i += 1
            if stack_i >= k: # reverse
                kg_head,kg_tail = self.list2node_r(stack)
                stack,stack_i = [],0
                p_pre.next = kg_head
                kg_tail.next = p.next.next
                p_pre = kg_tail
            p = p.next
        return dummy.next
    
    def rev_list(self,dummy_head,end):
        ppre,p,pnext = dummy_head.next,dummy_head.next.next,dummy_head.next.next.next
        while ppre!=end:
            p.next = ppre
            ppre,p = p,pnext
            if not pnext: pnext = pnext.next
        dummy_head.next.next = p
        dummy_head.next = ppre
        return
    
    def reverseKGroup_mysecond(self, head, k): # time limit exceeded
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k==1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        p_pre,p = dummy,dummy
        stack_i = 0
        
        def rev_list(dummy_head,end):
            ppre,p,pnext = dummy_head.next,dummy_head.next.next,dummy_head.next.next.next
            i=k
            while i:
                p.next = ppre
                ppre,p = p,pnext
                if not pnext: pnext = pnext.next
                i-=1
            dummy_head.next.next = p
            dummy_head.next = ppre
            return
        
        while p.next:
            stack_i += 1
            if stack_i >= k: # reverse
                self.rev_list(p_pre,p.next)
                stack_i,p_pre = 0,p
                continue
            p = p.next
        return dummy.next
        
        
head, k = list2node([2, 1, 4, 3, 5]), 2
print(node2list(head))
rst = Solution().reverseKGroup_mysecond(head,k)
print(node2list(rst))









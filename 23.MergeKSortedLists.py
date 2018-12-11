# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 17:33:48 2018

@author: pg255026
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def list2node(list):
    def list2node(list):
        dummy = ListNode(0)
        p = dummy
        for ele in list:
            p.next = ListNode(ele)
            p = p.next
        return dummy.next
    
    rst = []
    for ele in list:
        rst.append(list2node(ele))
    return rst

def node2list(node):
    dummy = ListNode(0)
    dummy.next = node
    p = dummy
    rst = []
    while p.next:
        rst.append(p.next.val)
        p = p.next
    return rst

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head,a=ListNode(0),[]
        for hhead in lists:
            p=hhead
            while p:
                a.append(p)
                p=p.next
        a.sort(key=lambda x:x.val)
        p=head
        for q in a:
            p.next=q
            p=p.next
        return head.next
    
    def mergeKLists_myfinal(self, lists): # 132ms
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ps = lists[:]
        rst = ListNode(0)
        p_rst = rst
        
        cands = {}
        for p in ps:
            if p: cands[p.val] = [p,] if p.val not in cands else cands[p.val]+[p,]
        
        while cands:
            # fetch element
            cand= min(cands) # TODO: can be optimized
            p = cands[cand].pop(0)
            p_rst.next = p
            p_rst = p_rst.next
            if not cands[cand]: cands.pop(cand)
            
            # insert new element
            if p.next:
                p = p.next
                cands[p.val] = [p,] if p.val not in cands else cands[p.val]+[p,]
        return rst.next
        
        
    def mergeKLists_mysecond(self, lists): #Time Limit Exceeded
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummys = []#[ListNode(0) for _ in lists]
        for ele in lists:
            dummy = ListNode(0)
            dummy.next = ele
            dummys.append(dummy)
        
        rst = ListNode(0)
        p_rst = rst
        ps = dummys[:]
        
        def _valid(lists):
            for p in lists:
                if p.next:
                    return True
            return False
        
        while _valid(ps):
            cand = []
            for i,p in enumerate(ps):
                if p.next and (not cand or (cand and p.next.val<cand[0]) ):
                    cand = [p.next.val,i]
            if cand:
                ps[cand[1]],p_rst.next = ps[cand[1]].next,ListNode(cand[0])
                p_rst = p_rst.next
            else:
                break
        return rst.next
    
    def mergeKLists_myfirst(self, lists): #Time Limit Exceeded
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummys = []#[ListNode(0) for _ in lists]
        for ele in lists:
            dummy = ListNode(0)
            dummy.next = ele
            dummys.append(dummy)
        
        rst = ListNode(0)
        p_rst = rst
        ps = dummys[:]
        
        def _valid(lists):
            for p in lists:
                if p.next:
                    return True
            return False
        
        while _valid(ps):
            cands = sorted([[p.next.val,i] for i,p in enumerate(ps) if p.next])
            if len(cands)>0:
                cand = sorted(cands,key=lambda r:r[0])[0]
                ps[cand[1]],p_rst.next = ps[cand[1]].next,ListNode(cand[0])
                p_rst = p_rst.next
            else:
                break
            
            pass
        return rst.next

lists = [
        [1,4,5],
        [1,3,4],
        [2,6]
        ]

lists = list2node(lists)
rst = Solution().mergeKLists(lists)
print(node2list(rst))


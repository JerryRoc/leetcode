# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 18:15:09 2018

@author: pg255026
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def stringToTreeNode(inputValues):
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not q and not p:
            return True
        if not q or not p:
            return False
        
        if p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False

p,q = stringToTreeNode([1,2,1]), stringToTreeNode([1,2,1])
rst = Solution().isSameTree(p,q)
print(rst)



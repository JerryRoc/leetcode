# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 17:41:13 2018

@author: pg255026
"""

class Solution:
    def _noDuplication(self,l):
        dictA = {}
        for c in l:
            if (c in dictA) and (c != '.'):
                return False
            dictA[c] = 1
        return True
        
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # rule 1: Each row must contain the digits 1-9 without repetition.
        for l in board:
            if not self._noDuplication(l): return False
        
        # rule 2: Each column must contain the digits 1-9 without repetition.
        for l in list(zip(*board)):
            if not self._noDuplication(l): return False
        
        # rule 3: Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        for i in range(3):
            for j in range(3):
                l = [r[j*3:j*3+3] for r in board[3*i:3*i+3]]
                l = l[0]+l[1]+l[2]
                if not self._noDuplication(l): return False
        return True
    
board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]

rst = Solution().isValidSudoku(board)
print(rst)
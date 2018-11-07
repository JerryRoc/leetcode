# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 16:02:21 2018

@author: pg255026
"""
import time

def timeit(func):
    def wrapper(*argv,**argc):
        tm = time.time()
        rst = func(*argv,**argc)
        print('%fs'%(time.time()-tm))
        return rst
    return wrapper

class Solution:
    @timeit
    def generateParenthesis_solution(self, n):
        def gen(N):
            if N == 0: return ['']
            ans = []
            for c in range(N):
                for left in gen(c):
                    for right in gen(N-1-c):
                        ans.append('({}){}'.format(left, right))
            return ans
        return gen(n)
    
    @timeit
    def generateParenthesis_solution2(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans
    
    @timeit
    def generateParenthesis_solution2_mod(self, n):
        def backtrack(S, left, right, ans = []):
            if left > 0:
                backtrack(S+'(', left-1, right)
            if right > left:
                backtrack(S+')', left, right-1)
            if not right:
                ans.append(S)
            return ans
        return backtrack('',n,n)
    
    @timeit
    def generateParenthesis_bestread(self, n):
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    parens += p,
            return parens
        return generate('', n, n)
    
    @timeit
    def generateParenthesis_fast(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(len(dp)):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[-1]
    
    @timeit
    def generateParenthesis_myfirst(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def check(s):
            rst = 0
            dicChar = {'(':1,')':-1}
            for c in s:
                rst = rst+dicChar[c]
                if rst < 0:
                    return False
            return True
        
        def insert(s,i):
            list_s = s.split('(')
            list_s[i]=list_s[i]+')'
            return '('.join(list_s)
            
        rst = ['('*n]
        for _ in range(n):
            rst = [insert(s,i+1) for s in rst for i in range(n)  if check(insert(s,i+1))]
            rst = list(set(rst))
        return rst

        


if __name__=='__main__':
    n = 3
    
    rst = Solution().generateParenthesis_solution2_mod(n)
    print(str(rst))
# ==========================================================
# 509. Fibonacci Number
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 587 ms (Beats 37%)
# Memory     : 12.2 MB (Beats 90%)
# Link       : https://leetcode.com/problems/fibonacci-number/
# ==========================================================

class Solution(object):
    def fib(self, n):
        if n <=1:
            return n
        else:
            return self.fib(n-1)+self.fib(n-2)

        
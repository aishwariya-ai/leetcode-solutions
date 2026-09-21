# ==========================================================
# 263. Ugly Number
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 12.3 MB (Beats 90%)
# Link       : https://leetcode.com/problems/ugly-number/
# ==========================================================

class Solution(object):
    def isUgly(self, n):
        if n<=0:
            return False
        for num in [2,3,5]:
            while n%num==0:
                n=n//num
        return n==1
        
        
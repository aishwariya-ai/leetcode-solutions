# ==========================================================
# 342. Power of Four
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 12.5 MB (Beats 19%)
# Link       : https://leetcode.com/problems/power-of-four/
# ==========================================================

class Solution(object):
    def isPowerOfFour(self, n):
        if n<=0:
            return False
        while n%4==0:
            n=n//4
        return n==1
        
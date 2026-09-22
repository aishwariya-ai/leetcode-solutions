# ==========================================================
# 69. Sqrt(x)
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 3 ms (Beats 64%)
# Memory     : 12.3 MB (Beats 90%)
# Link       : https://leetcode.com/problems/sqrtx/
# ==========================================================

class Solution(object):
    def mySqrt(self, x):
        if x<2:
            return x
        left=1
        right=x
        while left<=right:
            mid=(left+right)//2
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                left=mid+1
            else:
                right=mid-1
        return right
        
        
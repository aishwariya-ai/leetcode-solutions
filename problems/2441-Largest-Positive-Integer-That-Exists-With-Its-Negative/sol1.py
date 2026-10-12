# ==========================================================
# 2441. Largest Positive Integer That Exists With Its Negative
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 12.6 MB (Beats 11%)
# Link       : https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
# ==========================================================

class Solution(object):
    def findMaxK(self, nums):
        seen=set(nums)
        maxnum=-1
        for i in nums:
            if i>0 and -i in seen:
                maxnum=max(maxnum,i)
        return maxnum

    
        
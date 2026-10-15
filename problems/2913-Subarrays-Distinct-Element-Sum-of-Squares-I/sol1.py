# ==========================================================
# 2913. Subarrays Distinct Element Sum of Squares I
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 27 ms (Beats 90%)
# Memory     : 12 MB (Beats 100%)
# Link       : https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/
# ==========================================================

class Solution(object):
    def sumCounts(self, nums):
        total=0
        for i in range(len(nums)):
            distinct=set()
            for j in range(i,len(nums)):
                distinct.add(nums[j])
                total+=len(distinct)**2
        return total



        
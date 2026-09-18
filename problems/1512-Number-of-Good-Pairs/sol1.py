# ==========================================================
# 1512. Number of Good Pairs
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 12.3 MB (Beats 89%)
# Link       : https://leetcode.com/problems/number-of-good-pairs/
# ==========================================================

class Solution(object):
    def numIdenticalPairs(self, nums):
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    count+=1
        return count
        
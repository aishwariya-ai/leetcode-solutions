# ==========================================================
# 747. Largest Number At Least Twice of Others
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 19.2 MB (Beats 48%)
# Link       : https://leetcode.com/problems/largest-number-at-least-twice-of-others/
# ==========================================================

class Solution(object):
    def dominantIndex(self, nums):
        maximum=max(nums)
        index=-1
        for i in range(len(nums)):
            if nums[i]==maximum:
                index=i
            elif nums[i]*2>maximum:
                return -1
        return index

        
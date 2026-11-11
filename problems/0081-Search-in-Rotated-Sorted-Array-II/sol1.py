# ==========================================================
# 81. Search in Rotated Sorted Array II
# Difficulty : Medium
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 19.5 MB (Beats 88%)
# Link       : https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# ==========================================================

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        if target in nums:
            return True
        else:
            return False
        
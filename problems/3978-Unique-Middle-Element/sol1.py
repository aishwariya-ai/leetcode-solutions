# ==========================================================
# 3978. Unique Middle Element
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 2 ms (Beats 31%)
# Memory     : 19.2 MB (Beats 70%)
# Link       : https://leetcode.com/problems/unique-middle-element/
# ==========================================================

class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        count=0
        left=0
        right=len(nums)-1
        mid=(right-left)//2
        for n in nums:
            if n == nums[mid]:
                count+=1
        if count==1:
            return True
        else:
            return False

        
# ==========================================================
# 3866. First Unique Even Element
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 3 ms (Beats 37%)
# Memory     : 19.3 MB (Beats 45%)
# Link       : https://leetcode.com/problems/first-unique-even-element/
# ==========================================================

class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        for n in nums:
            if n %2==0:
                count=0
                for i in nums:
                    if i == n:
                        count+=1
                if count==1:
                    return n
        return -1
        
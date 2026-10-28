# ==========================================================
# 1464. Maximum Product of Two Elements in an Array
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 476 ms (Beats 5%)
# Memory     : 12.3 MB (Beats 67%)
# Link       : https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
# ==========================================================

class Solution(object):
    def maxProduct(self, nums):
        maximum=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                total=(nums[i]-1)*(nums[j]-1)
                maximum=max(maximum,total)
        return maximum


    
        
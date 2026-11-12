# ==========================================================
# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 15 ms (Beats 5%)
# Memory     : 19.1 MB (Beats 94%)
# Link       : https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
# ==========================================================

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maximum=1
        l=len(nums)
        for i in range(l):
            inc=1
            dec=1
            for j in range(i+1,l):
                if nums[j]>nums[j-1]:
                    inc+=1
                    dec=1
                elif nums[j]<nums[j-1]:
                    dec+=1
                    inc=1
                else:
                    inc=1
                    dec=1
                maximum=max(maximum,inc,dec)
        return maximum


            
# ==========================================================
# 3550. Smallest Index With Digit Sum Equal to Index
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 4 ms (Beats 64%)
# Memory     : 12.4 MB (Beats 62%)
# Link       : https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/
# ==========================================================

class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            sum1=0
            newnum=nums[i]
            while newnum>0:
                digit=newnum%10
                sum1+=digit
                newnum=newnum//10
            if sum1==i:
                return i
        return -1
        
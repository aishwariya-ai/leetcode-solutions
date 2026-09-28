# ==========================================================
# 674. Longest Continuous Increasing Subsequence
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 13.2 MB (Beats 93%)
# Link       : https://leetcode.com/problems/longest-continuous-increasing-subsequence/
# ==========================================================

class Solution(object):
    def findLengthOfLCIS(self, nums):
        length=1
        maxnum=nums[0]
        maxlength=1
        for i in range(1,len(nums)):
            if nums[i]>maxnum:
                length+=1
            else:
                length=1
            maxnum=nums[i]
            if(length>maxlength):
                maxlength=length
        return maxlength
            
        
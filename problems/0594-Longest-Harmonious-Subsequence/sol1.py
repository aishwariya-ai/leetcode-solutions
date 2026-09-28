# ==========================================================
# 594. Longest Harmonious Subsequence
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 23 ms (Beats 97%)
# Memory     : 14.2 MB (Beats 73%)
# Link       : https://leetcode.com/problems/longest-harmonious-subsequence/
# ==========================================================

class Solution(object):
    def findLHS(self, nums):
        count={}
        for n in nums:
            if n in count:
                count[n]+=1
            else:
                count[n]=1
        maxlength=0
        for num in count:
            if num+1 in count:
                length=count[num]+count[num+1]
                if length>maxlength:
                    maxlength=length
        return maxlength

# ==========================================================
# 278. First Bad Version
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 19 ms (Beats 29%)
# Memory     : 12.1 MB (Beats 99%)
# Link       : https://leetcode.com/problems/first-bad-version/
# ==========================================================

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        left=0
        right=n
        while left<right:
            mid=(left+right)//2
            if isBadVersion(mid):
                right=mid
            else:
                left=mid+1
        return left

        


        
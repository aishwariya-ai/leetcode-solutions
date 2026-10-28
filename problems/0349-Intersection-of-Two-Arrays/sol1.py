# ==========================================================
# 349. Intersection of Two Arrays
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 21 ms (Beats 11%)
# Memory     : 11.9 MB (Beats 100%)
# Link       : https://leetcode.com/problems/intersection-of-two-arrays/
# ==========================================================

class Solution(object):
    def intersection(self, nums1, nums2):
        newlist=[]
        for n in nums2:
            if n in nums1:
                if n not in newlist:
                    newlist.append(n)
        return newlist
        
        
# ==========================================================
# 349. Intersection of Two Arrays
# Difficulty : Easy
# Language   : Python
# Solution   : #2
# Runtime    : 22 ms (Beats 11%)
# Memory     : 12.2 MB (Beats 95%)
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
        
        
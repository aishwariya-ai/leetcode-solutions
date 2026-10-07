# ==========================================================
# 11. Container With Most Water
# Difficulty : Medium
# Language   : Python
# Solution   : #1
# Runtime    : 131 ms (Beats 8%)
# Memory     : 20.7 MB (Beats 65%)
# Link       : https://leetcode.com/problems/container-with-most-water/
# ==========================================================

class Solution(object):
    def maxArea(self, height):
        left=0
        right=len(height)-1
        maxarea=0
        while left<right:
            area=(right-left) * min(height[left],height[right])
            maxarea=max(maxarea,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxarea
        
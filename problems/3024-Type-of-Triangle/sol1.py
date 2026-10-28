# ==========================================================
# 3024. Type of Triangle
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 1 ms (Beats 15%)
# Memory     : 12.3 MB (Beats 88%)
# Link       : https://leetcode.com/problems/type-of-triangle/
# ==========================================================

class Solution(object):
    def triangleType(self, nums):
        count={}
        nums.sort()
        if nums[0]+nums[1]<=nums[2]:
            return "none"

        for n in nums:
            count[n]=count.get(n,0)+1
        if len(count)==1:
            return "equilateral"
        elif len(count)==2:
            return "isosceles"
        else:
            return "scalene"
        
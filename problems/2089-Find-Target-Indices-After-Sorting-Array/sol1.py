# ==========================================================
# 2089. Find Target Indices After Sorting Array
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 12.3 MB (Beats 89%)
# Link       : https://leetcode.com/problems/find-target-indices-after-sorting-array/
# ==========================================================

class Solution(object):
    def targetIndices(self, nums, target):
        newarr=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            if nums[i]==target:
                newarr.append(i)
        return newarr

        
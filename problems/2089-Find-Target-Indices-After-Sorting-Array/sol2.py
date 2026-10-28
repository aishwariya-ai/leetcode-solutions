# ==========================================================
# 2089. Find Target Indices After Sorting Array
# Difficulty : Easy
# Language   : Python
# Solution   : #2
# Runtime    : 1 ms (Beats 48%)
# Memory     : 12.2 MB (Beats 89%)
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

        
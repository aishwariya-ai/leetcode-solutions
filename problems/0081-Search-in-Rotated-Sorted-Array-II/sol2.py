# ==========================================================
# 81. Search in Rotated Sorted Array II
# Difficulty : Medium
# Language   : Python
# Solution   : #2
# Runtime    : 0 ms (Beats 100%)
# Memory     : 19.5 MB (Beats 88%)
# Link       : https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# ==========================================================

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left=0
        right=len(nums)-1
        while left<=right:
            mid= left+(right-left)//2
            if nums[mid]==target:
                return True
            if nums[left]==nums[mid] and nums[mid]==nums[right]:
                left+=1
                right-=1
                continue
            if nums[left]<=nums[mid]:
                if nums[left]<=target < nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]<target <=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return False


        
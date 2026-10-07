# ==========================================================
# 15. 3Sum
# Difficulty : Medium
# Language   : Python
# Solution   : #1
# Runtime    : 767 ms (Beats 43%)
# Memory     : 18.4 MB (Beats 61%)
# Link       : https://leetcode.com/problems/3sum/
# ==========================================================

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result=[]
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            if i > 0 and nums[i]==nums[i - 1]:
                continue
            while left<right:
                total= nums[i]+nums[left]+nums[right]
                if total == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total <0:
                    left+=1
                else:
                    right-=1
        return result
            

        
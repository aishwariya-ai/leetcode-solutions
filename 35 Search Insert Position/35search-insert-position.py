from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        if target in nums:   # Keep your original check
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        else:
            nums.append(target)
            nums.sort()
            for i in range(len(nums)):
                if nums[i] == target:
                    return i

class Solution(object):
    def smallestEqual(self, nums):
        for i in range(len(nums)):
            digit = i % 10
            if digit == nums[i]:
                return i
        return -1
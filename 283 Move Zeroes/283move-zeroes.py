class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j=0
        length=len(nums)
        for i in range(length):
            if (nums[i]!=0):
                nums[i],nums[j]=nums[j],nums[i]
                j=j+1
        return nums
        
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr=sorted(list(set(nums)))
        length=len(arr)
        if len(arr)>=3:
           return arr[-3]
        else:
            return arr[-1]
class Solution(object):
    def getConcatenation(self, nums):
        ans=nums[:]

        for i in nums:
            ans.append(i)
        return ans
        
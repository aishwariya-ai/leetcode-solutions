class Solution(object):
    def heightChecker(self, heights):
        nums=sorted(heights)
        count=0
        for i in range(len(heights)):
            if(nums[i]!=heights[i]):
                count+=1
        return count
        
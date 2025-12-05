class Solution(object):
    def maxArea(self, nums):
        res=0
        l=0
        r=len(nums)-1
        while l<r:
            area=(r-l)*min(nums[l],nums[r])
            res=max(res,area)
            if nums[l]<nums[r]:
                l+=1
            else:
                r-=1
        return res

        
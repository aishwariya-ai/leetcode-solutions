class Solution(object):
    def findSubarrays(self, nums):
        seen=set()
        total=0
        for i in range(len(nums)-1):
            total=nums[i]+nums[i+1]
            if total in seen:
                return True
            seen.add(total)
        return False
       
        
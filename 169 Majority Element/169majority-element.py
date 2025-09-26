class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        key=math.floor(n//2)
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
        for num,j in count.items():
            if j>key:
                return num


        
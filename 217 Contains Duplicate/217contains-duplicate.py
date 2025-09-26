class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count={}
        for n in nums:
            count[n]=count.get(n,0)+1
        for val,i in count.items():
            if i>1:
                return True   
        return False   
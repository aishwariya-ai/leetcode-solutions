class Solution(object):
    def sortedSquares(self, nums):
        sort=[]
        for n in nums:
            sort.append(n**2)
        return sorted(sort)

        
        
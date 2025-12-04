class Solution(object):
    def maxProduct(self,nums):
        res=max(nums)
        curmin=1
        curmax=1
        for n in nums:
            if n==0:
                curmin=1
                curmax=1
                continue
            temp=n*curmax
            curmax=max(n*curmax,n*curmin,n)
            curmin=min(temp,n*curmin,n)
            res=max(res,curmax,curmin)
        return res
        
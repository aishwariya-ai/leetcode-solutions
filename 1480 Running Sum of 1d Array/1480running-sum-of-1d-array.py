class Solution(object):
    def runningSum(self, nums):
        runningsum=0
        runningsumlist=[]
        for n in nums:
            runningsum+=n
            runningsumlist.append(runningsum)
        return  runningsumlist
        
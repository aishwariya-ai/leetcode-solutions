class Solution(object):
    def findDisappearedNumbers(self, nums):
        arr=set(nums)
        finalarr=[]
        for i in range(1,len(nums)+1):
            if(i not in arr):
                finalarr.append(i)
        return finalarr


        
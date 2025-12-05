class Solution(object):
    def hammingWeight(self, num):
        nums=bin(num)
        new=nums[2:]
        count=0
        for n in new:
            if(int(n)%2==1):
                count+=1
        return count
        
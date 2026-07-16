class Solution(object):
    def differenceOfSums(self, n, m):
        sumnot=0
        sum=0
        for i in range(1,n+1):
            if(i%m!=0):
                sumnot+=i
            if(i%m==0):
                sum+=i
        total=sumnot-sum
        return total

        
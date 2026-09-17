class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result=[]
        maximum=max(candies)
        for n in candies:
            if (n+extraCandies)>=maximum:
                result.append(True)
            else:
                result.append(False)
        return result

        

        
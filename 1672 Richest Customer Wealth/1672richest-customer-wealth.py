class Solution(object):
    def maximumWealth(self, accounts):
        maximum=[]
        for acc in accounts:
            maximum.append(sum(acc))
        return max(maximum)

        
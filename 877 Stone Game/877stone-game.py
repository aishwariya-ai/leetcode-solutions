class Solution(object):
    def stoneGame(self, piles):
        odd_sum=0
        even_sum=0
        for i in range(len(piles)):
            if i%2==0:
                even_sum+=piles[i]
            else:
                odd_sum+=piles[i]
        if(even_sum != odd_sum):
            return True

        
        
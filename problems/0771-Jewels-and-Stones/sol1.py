# ==========================================================
# 771. Jewels and Stones
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 12.4 MB (Beats 57%)
# Link       : https://leetcode.com/problems/jewels-and-stones/
# ==========================================================

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        jewels = [i for i in jewels]
        count = 0
        for i in stones:
            if i in jewels:
                count+=1
        return count
        
        
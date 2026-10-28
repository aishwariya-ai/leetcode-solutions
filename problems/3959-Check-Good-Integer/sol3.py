# ==========================================================
# 3959. Check Good Integer
# Difficulty : Easy
# Language   : Python
# Solution   : #3
# Runtime    : 1 ms (Beats 46%)
# Memory     : 12.1 MB (Beats 99%)
# Link       : https://leetcode.com/problems/check-good-integer/
# ==========================================================

class Solution(object):
    def checkGoodInteger(self, n):
        digitsum=0
        squaresum=0
        while n>0:
            digit=n%10
            digitsum+=digit
            squaresum+=digit**2
            n=n//10
        if (squaresum-digitsum)>=50:
            return True
        else:
            return False
        
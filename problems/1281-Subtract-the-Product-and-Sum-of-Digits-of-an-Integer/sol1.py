# ==========================================================
# 1281. Subtract the Product and Sum of Digits of an Integer
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 12.5 MB (Beats 17%)
# Link       : https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
# ==========================================================

class Solution(object):
    def subtractProductAndSum(self, n):
        product=1
        sum1=0
        while n>0:
            remainder=n%10
            product*=remainder
            sum1+=remainder
            n=n//10
        return product-sum1
    
    

        
        
# ==========================================================
# 507. Perfect Number
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 7 ms (Beats 59%)
# Memory     : 12.4 MB (Beats 75%)
# Link       : https://leetcode.com/problems/perfect-number/
# ==========================================================

class Solution(object):

    def checkPerfectNumber(self, num):

        if num <= 1:
            return False
        total = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                total += i
                total += num // i
            i += 1
        return total == num
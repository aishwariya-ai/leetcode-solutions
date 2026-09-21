# ==========================================================
# 231. Power of Two
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 12.3 MB (Beats 55%)
# Link       : https://leetcode.com/problems/power-of-two/
# ==========================================================

class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        while n > 0:
            if n == 1:
                return True
            if n % 2 != 0:
                break
            n //= 2
        return False

        
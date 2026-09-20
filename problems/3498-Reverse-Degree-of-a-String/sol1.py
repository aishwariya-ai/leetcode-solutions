# ==========================================================
# 3498. Reverse Degree of a String
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 12 ms (Beats 40%)
# Memory     : 12.4 MB (Beats 56%)
# Link       : https://leetcode.com/problems/reverse-degree-of-a-string/
# ==========================================================

class Solution(object):
    def reverseDegree(self, s):
        total = 0
        for i in range(len(s)):
            alphabet = ord('z') - ord(s[i]) + 1
            string = i + 1
            total += alphabet * string
        return total
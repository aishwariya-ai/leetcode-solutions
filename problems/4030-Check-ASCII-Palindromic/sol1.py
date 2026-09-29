# ==========================================================
# 4030. Check ASCII Palindromic
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 4 ms (Beats 56%)
# Memory     : 12.4 MB (Beats 54%)
# Link       : https://leetcode.com/problems/check-ascii-palindromic/
# ==========================================================

class Solution(object):
    def isPalindromic(self, s):
        binary=""
        for char in s:
            binary+=format(ord(char),'08b')
        return binary==binary[::-1]
        
        
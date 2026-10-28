# ==========================================================
# 3863. Minimum Operations to Sort a String
# Difficulty : Medium
# Language   : Python
# Solution   : #1
# Runtime    : 411 ms (Beats 27%)
# Memory     : 14.6 MB (Beats 73%)
# Link       : https://leetcode.com/problems/minimum-operations-to-sort-a-string/
# ==========================================================

class Solution(object):
    def minOperations(self, s):
        small=min(s)
        large=max(s)
        length=len(s)
        if list(s)==sorted(s):
            return 0
        if length==2:
            return -1
        if s[0]==small or s[-1]==large:
            return 1
        if any(char==large or char==small for char in s[1:-1]):
            return 2
        return 3

        
        
        
        
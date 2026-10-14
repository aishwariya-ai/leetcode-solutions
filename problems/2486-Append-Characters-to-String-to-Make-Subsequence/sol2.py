# ==========================================================
# 2486. Append Characters to String to Make Subsequence
# Difficulty : Medium
# Language   : Python
# Solution   : #2
# Runtime    : 47 ms (Beats 33%)
# Memory     : 12.8 MB (Beats 100%)
# Link       : https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/
# ==========================================================

class Solution(object):
    def appendCharacters(self, s, t):
        left=0
        right=0
        while left<len(s) and right<len(t):
            if s[left]==t[right]:
                right+=1
            left+=1
        return len(t)-right
            
        
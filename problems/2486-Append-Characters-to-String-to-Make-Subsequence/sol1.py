# ==========================================================
# 2486. Append Characters to String to Make Subsequence
# Difficulty : Medium
# Language   : Python
# Solution   : #1
# Runtime    : 45 ms (Beats 40%)
# Memory     : 12.9 MB (Beats 96%)
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
            
        
# ==========================================================
# 2914. Minimum Number of Changes to Make Binary String Beautiful
# Difficulty : Medium
# Language   : Python
# Solution   : #1
# Runtime    : 18 ms (Beats 66%)
# Memory     : 19.6 MB (Beats 53%)
# Link       : https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/
# ==========================================================

class Solution:
    def minChanges(self, s: str) -> int:
        count=0
        for i in range(0,len(s),2):
            if s[i]!=s[i+1]:
                count+=1
        return count

        
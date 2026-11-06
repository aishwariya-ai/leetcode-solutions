# ==========================================================
# 1207. Unique Number of Occurrences
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 19.2 MB (Beats 67%)
# Link       : https://leetcode.com/problems/unique-number-of-occurrences/
# ==========================================================

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count={}
        for i in arr:
            count[i]=count.get(i,0)+1
        if len(set(count.values()))==len(count):
            return(True)
        else:
            return(False)
        
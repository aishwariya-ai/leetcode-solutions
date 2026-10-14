# ==========================================================
# 389. Find the Difference
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 6 ms (Beats 26%)
# Memory     : 12.2 MB (Beats 100%)
# Link       : https://leetcode.com/problems/find-the-difference/
# ==========================================================

class Solution(object):
    def findTheDifference(self, s, t):
        s=sorted(s)
        t=sorted(t)
        i=0
        j=0
        while i<len(s):
            if s[i]!=t[i]:
                return t[j]
            i+=1
            j+=1
        return t[-1]


        
        
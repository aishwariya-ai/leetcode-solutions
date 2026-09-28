# ==========================================================
# 1614. Maximum Nesting Depth of the Parentheses
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 12.2 MB (Beats 91%)
# Link       : https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
# ==========================================================

class Solution(object):
    def maxDepth(self, s):
        count=0
        maxcount=0
        for i in s:
            if i=='(':
                count+=1
                if count>maxcount:
                    maxcount=count
            elif i==')':
                count-=1
        return maxcount
            

        
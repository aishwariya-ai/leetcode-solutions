# ==========================================================
# 1021. Remove Outermost Parentheses
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 7 ms (Beats 51%)
# Memory     : 12.4 MB (Beats 64%)
# Link       : https://leetcode.com/problems/remove-outermost-parentheses/
# ==========================================================

class Solution(object):

    def removeOuterParentheses(self, s):
        result = ""
        depth = 0
        for char in s:
            if char == '(':
                if depth > 0:
                    result += char
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    result += char
        return result
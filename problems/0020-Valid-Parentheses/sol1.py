# ==========================================================
# 20. Valid Parentheses
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 7 ms (Beats 14%)
# Memory     : 12.4 MB (Beats 73%)
# Link       : https://leetcode.com/problems/valid-parentheses/
# ==========================================================

class Solution(object):

    def isValid(self, s):
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            else:
                if not stack or stack.pop() != char:
                    return False
        return len(stack) == 0
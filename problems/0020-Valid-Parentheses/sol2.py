# ==========================================================
# 20. Valid Parentheses
# Difficulty : Easy
# Language   : Python
# Solution   : #2
# Runtime    : 1 ms (Beats 47%)
# Memory     : 19.1 MB (Beats 84%)
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
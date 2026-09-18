# ==========================================================
# 1678. Goal Parser Interpretation
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 15 ms (Beats 63%)
# Memory     : 12.4 MB (Beats 18%)
# Link       : https://leetcode.com/problems/goal-parser-interpretation/
# ==========================================================

class Solution(object):
    def interpret(self, command):
       command=command.replace("()","o")
       command=command.replace("(al)","al")
       return command
        
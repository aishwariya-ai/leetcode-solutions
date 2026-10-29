# ==========================================================
# 171. Excel Sheet Column Number
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 19.1 MB (Beats 78%)
# Link       : https://leetcode.com/problems/excel-sheet-column-number/
# ==========================================================

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result=0
        for ch in columnTitle:
            result=result*26+(ord(ch)- ord('A')+1)
        return result
        
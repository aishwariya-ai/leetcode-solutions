# ==========================================================
# 168. Excel Sheet Column Title
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 19.2 MB (Beats 62%)
# Link       : https://leetcode.com/problems/excel-sheet-column-title/
# ==========================================================

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result=""
        while columnNumber>0:
            columnNumber-=1
            rem=columnNumber%26
            result=chr(rem+ord('A'))+result
            columnNumber//=26
        return result

        
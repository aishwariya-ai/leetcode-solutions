# ==========================================================
# 3274. Check if Two Chessboard Squares Have the Same Color
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 27 ms (Beats 8%)
# Memory     : 12.2 MB (Beats 89%)
# Link       : https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/
# ==========================================================

class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        one=(ord(coordinate1[0])-96)+int(coordinate1[1])
        two=(ord(coordinate2[0])-96)+int(coordinate2[1])
        if (one+two)%2==0:
            return True
        else:
            return False
        
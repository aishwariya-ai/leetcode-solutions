# ==========================================================
# 1812. Determine Color of a Chessboard Square
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 12.3 MB (Beats 84%)
# Link       : https://leetcode.com/problems/determine-color-of-a-chessboard-square/
# ==========================================================

class Solution(object):
    def squareIsWhite(self, coordinates):
        newlist=[]
        num=ord(coordinates[0])-96
        newlist.append(num)
        newlist.append(int(coordinates[1]))
        if newlist[0]%2==0 and newlist[1]%2!=0:
            return True
        if newlist[0]%2!=0 and newlist[1]%2==0:
            return True
        else:
            return False

        
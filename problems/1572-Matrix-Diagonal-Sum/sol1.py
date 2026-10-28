# ==========================================================
# 1572. Matrix Diagonal Sum
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 3 ms (Beats 19%)
# Memory     : 12.3 MB (Beats 97%)
# Link       : https://leetcode.com/problems/matrix-diagonal-sum/
# ==========================================================

class Solution(object):
    def diagonalSum(self, mat):
        total=0
        rows=len(mat)
        cols=len(mat[0])
        for i in range(rows):
            for j in range(cols):
                if i==j:
                    total+=mat[i][j]
                elif i+j==rows-1:
                    total+=mat[i][j]
        return total
                    
        
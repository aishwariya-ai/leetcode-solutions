# ==========================================================
# 1351. Count Negative Numbers in a Sorted Matrix
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 3 ms (Beats 37%)
# Memory     : 13.1 MB (Beats 70%)
# Link       : https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# ==========================================================

class Solution(object):
    def countNegatives(self, grid):
        row=len(grid)
        cols=len(grid[0])
        count=0
        for i in range(row):
            for j in range(cols):
                if grid[i][j]<0:
                    count+=1
        return count
                
        
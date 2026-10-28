# ==========================================================
# 74. Search a 2D Matrix
# Difficulty : Medium
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 12.3 MB (Beats 98%)
# Link       : https://leetcode.com/problems/search-a-2d-matrix/
# ==========================================================

class Solution(object):
    def searchMatrix(self, matrix, target):
        rows=len(matrix)
        cols=len(matrix[0])
        left=0
        right=rows*cols-1
        while left<=right:
            mid=(left+right)//2
            r=mid//cols
            c=mid%cols
            value=matrix[r][c]
            if value==target:
                return True
            elif value>target:
                right=mid-1
            else:
                left=mid+1
        return False

        
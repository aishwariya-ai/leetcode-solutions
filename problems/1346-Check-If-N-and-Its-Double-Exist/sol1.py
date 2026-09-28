# ==========================================================
# 1346. Check If N and Its Double Exist
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 22 ms (Beats 7%)
# Memory     : 12.6 MB (Beats 0%)
# Link       : https://leetcode.com/problems/check-if-n-and-its-double-exist/
# ==========================================================

class Solution(object):
    def checkIfExist(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j and arr[i]==2*arr[j]:
                    return True
        return False
        
        
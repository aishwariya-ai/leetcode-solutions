# ==========================================================
# 3340. Check Balanced String
# Difficulty : Easy
# Language   : Python
# Solution   : #2
# Runtime    : 6 ms (Beats 64%)
# Memory     : 12.2 MB (Beats 81%)
# Link       : https://leetcode.com/problems/check-balanced-string/
# ==========================================================

class Solution(object):
    def isBalanced(self, num):
        odd=0
        even=0
        for i in range(len(num)):
            if i%2==0:
                even+=int(num[i])
            else:
                odd+=int(num[i])
        if even==odd:
            return True
        else:
            return False
                



        
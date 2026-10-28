# ==========================================================
# 374. Guess Number Higher or Lower
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 17 ms (Beats 42%)
# Memory     : 12.3 MB (Beats 85%)
# Link       : https://leetcode.com/problems/guess-number-higher-or-lower/
# ==========================================================

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        left=0
        right=n
        while left<=right:
            mid=left+(right-left)//2
            if(guess(mid))==0:
                return mid
            elif (guess(mid))==1:
                left=mid+1
            else:
                right=mid-1
        return -1

        
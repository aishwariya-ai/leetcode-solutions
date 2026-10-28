# ==========================================================
# 1287. Element Appearing More Than 25% In Sorted Array
# Difficulty : Easy
# Language   : Python
# Solution   : #2
# Runtime    : 7 ms (Beats 41%)
# Memory     : 14.2 MB (Beats 8%)
# Link       : https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
# ==========================================================

class Solution(object):
    def findSpecialInteger(self, arr):
        count={}
        total=0
        for num in arr:
            count[num]=count.get(num,0)+1
        for num,frequency in count.items():
            if frequency >(len(arr)//4):
                total=num
        return total

        
# ==========================================================
# 1491. Average Salary Excluding the Minimum and Maximum Salary
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 19.1 MB (Beats 98%)
# Link       : https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
# ==========================================================

class Solution:
    def average(self, salary: list[int]) -> float:
        avg=0
        minimum=min(salary)
        maximum=max(salary)
        for num in salary:
            if num!=minimum and num!=maximum:
                avg+=num
        return float(avg/(len(salary)-2))
        
        
from collections import Counter
class Solution(object):
    def sumOfUnique(self, nums):
        frequency = Counter(nums)
        total = 0
        for key, value in frequency.items():
            if value == 1:
                total += key
        return total
        
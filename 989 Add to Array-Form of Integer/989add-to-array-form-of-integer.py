class Solution(object):

    def addToArrayForm(self, num, k):
        temp_arr = []
        for n in num:
            temp_arr.append(str(n))
        temp_str = "".join(temp_arr)
        sum1 = int(temp_str) + k
        result = []
        for n in str(sum1):
            result.append(int(n))
        return result
class Solution(object):
    def countPrefixes(self, words, s):
        count=0
        for char in words:
            if s.startswith(char):
                count+=1
        return count
        
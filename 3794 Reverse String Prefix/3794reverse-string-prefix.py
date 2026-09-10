class Solution(object):
    def reversePrefix(self, s, k):
        newstring=s[:k]
        reversedstr=newstring[::-1]
        return (reversedstr+s[k:])

        
        
class Solution(object):
    def firstPalindrome(self, words):
        for char in words:
            if(char==char[::-1]):
                return char
        return ""

        
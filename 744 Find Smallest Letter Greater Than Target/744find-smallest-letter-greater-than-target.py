class Solution(object):
    def nextGreatestLetter(self, letters, target):
        for char in letters:
            if ord(target)<ord(char):
                return char
        return letters[0]
        
        
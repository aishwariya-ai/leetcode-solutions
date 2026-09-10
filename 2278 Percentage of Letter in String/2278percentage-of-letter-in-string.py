class Solution(object):
    def percentageLetter(self, s, letter):
        percentage=0
        count=0
        for char in s:
            if char==letter:
                count+=1
        percentage=(count*100)//len(s)
        return percentage
        
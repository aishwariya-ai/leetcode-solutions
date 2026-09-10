class Solution(object):
    def secondHighest(self, s):
        number=[]
        digits='1234567890'
        for char in s:
            if char in digits:
                number.append(int(char))
        number = list(set(number))
        number1=sorted(number)
        if len(number1) < 2:
            return -1
        return number1[len(number)-2]
        
        
        
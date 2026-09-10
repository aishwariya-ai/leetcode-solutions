class Solution(object):
    def isSameAfterReversals(self, num):
        temp=num
        reverse=0
        newreverse=0
        while temp:
            remainder=temp%10
            reverse=reverse*10+remainder
            temp=temp//10
        while reverse:
            newremainder=reverse%10
            newreverse=newreverse*10+newremainder
            reverse=reverse//10
        if(newreverse==num):
            return True
        return False

        
        
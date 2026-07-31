class Solution(object):
    def findComplement(self, num):
        binary=bin(num)[2:]
        flipped=""
        for i in binary:
            if(i=="0"):
                flipped+="1"
            else:
                flipped+="0"
        return int(flipped,2)
        
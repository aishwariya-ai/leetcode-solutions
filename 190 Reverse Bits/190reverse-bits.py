class Solution(object):
    def reverseBits(self, n):
        binary=bin(n)[2:]
        binary = binary.zfill(32)
        binreversed=binary[::-1]
        decimal=int(binreversed,2)
        return decimal

        
        
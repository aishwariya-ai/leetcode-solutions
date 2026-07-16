class Solution(object):
    def checkIfPangram(self, sentence):
        arr=list(set(sentence))
        if(len(arr)==26):
            return True
        return False
        
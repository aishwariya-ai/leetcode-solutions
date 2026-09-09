class Solution(object):
    def uniqueMorseRepresentations(self, words):
        final=set()
        alpha=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            decoded=""
            for char in word:
                decoded+=alpha[ord(char)-97]
            final.add(decoded)
        return len(final)



        
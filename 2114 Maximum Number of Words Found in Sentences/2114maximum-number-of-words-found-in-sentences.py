class Solution(object):
    def mostWordsFound(self, sentences):
        maxwords=0
        for words in sentences:
            wordcount=len(words.split())
            maxwords=max(maxwords,wordcount)
        return maxwords
            

        
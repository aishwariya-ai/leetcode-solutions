# ==========================================================
# 383. Ransom Note
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 105 ms (Beats 5%)
# Memory     : 12.7 MB (Beats 23%)
# Link       : https://leetcode.com/problems/ransom-note/
# ==========================================================

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for char in ransomNote:
            if ransomNote.count(char)> magazine.count(char):
                return False
        return True


        
        
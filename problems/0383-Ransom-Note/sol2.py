# ==========================================================
# 383. Ransom Note
# Difficulty : Easy
# Language   : Python
# Solution   : #2
# Runtime    : 23 ms (Beats 86%)
# Memory     : 12.4 MB (Beats 100%)
# Link       : https://leetcode.com/problems/ransom-note/
# ==========================================================

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        for r in ransomNote:
            
            if r in magazine:
                magazine.remove(r)
            else:
                return False
        return True 


        
        
# ==========================================================
# 2299. Strong Password Checker II
# Difficulty : Easy
# Language   : Python
# Solution   : #2
# Runtime    : 0 ms (Beats 100%)
# Memory     : 12.2 MB (Beats 96%)
# Link       : https://leetcode.com/problems/strong-password-checker-ii/
# ==========================================================

class Solution(object):
    def strongPasswordCheckerII(self, password):
        digit=lower=upper=special=False
        punc= "!@#$%^&*()-+"
        if len(password)<8:
            return False
        for i in range (len(password)):
            if password[i].isdigit():
                digit=True
            elif password[i].islower():
                lower=True
            elif password[i].isupper():
                upper=True
            elif password[i] in punc:
                special=True
            else:
                return False
            if i < len(password)-1:
                if password[i]==password[i+1]:
                    return False
        return digit and lower and upper and special 



        
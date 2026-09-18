# ==========================================================
# 1108. Defanging an IP Address
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 11 ms (Beats 86%)
# Memory     : 12.4 MB (Beats 18%)
# Link       : https://leetcode.com/problems/defanging-an-ip-address/
# ==========================================================

class Solution(object):
    def defangIPaddr(self, address):
        result=address.replace(".","[.]")
        return result
        
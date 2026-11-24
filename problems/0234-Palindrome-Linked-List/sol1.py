# ==========================================================
# 234. Palindrome Linked List
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 17 ms (Beats 94%)
# Memory     : 53.5 MB (Beats 24%)
# Link       : https://leetcode.com/problems/palindrome-linked-list/
# ==========================================================

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        l=0
        r=len(nums)-1
        while l < r:
            if nums[l]!=nums[r]:
                return False
            l+=1
            r-=1
        return True
        
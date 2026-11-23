# ==========================================================
# 206. Reverse Linked List
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 20.3 MB (Beats 73%)
# Link       : https://leetcode.com/problems/reverse-linked-list/
# ==========================================================

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        pre= None
        curr=head
        while curr:
            newcur=curr.next
            curr.next=pre
            pre=curr
            curr=newcur
        return pre
        
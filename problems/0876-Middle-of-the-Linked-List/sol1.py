# ==========================================================
# 876. Middle of the Linked List
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 1 ms (Beats 3%)
# Memory     : 19.4 MB (Beats 13%)
# Link       : https://leetcode.com/problems/middle-of-the-linked-list/
# ==========================================================

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        Fast= head
        slow = head
        while (Fast is not None and Fast.next is not None):
            Fast=Fast.next.next
            slow=slow.next
        return slow
        
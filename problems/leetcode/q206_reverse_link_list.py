from typing import Optional
"""
206 - Reverse Linked List. https://leetcode.com/problems/reverse-linked-list/
What I learned: Can do either recursively or iteratively
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # recursive strategy
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(head, prev):
            if not head:
                return prev
            temp = head.next
            head.next = prev
            return helper(temp, head)
        return helper(head, None)

    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev

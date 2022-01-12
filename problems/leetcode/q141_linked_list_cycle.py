# Definition for singly-linked list.

from typing import Optional

"""
141. Linked List Cycle https://leetcode.com/problems/linked-list-cycle/
What I learned: The strategy is to use two pointers, a walker and a runner (slow and fast). The walker (slow) goes 
through each node. The runner (fast) skips ahead 2. So if there is a cycle, the runner will eventually lap the walker 
and the walker and runner will be at the same node. Otherwise the runner will reach the end of the linked list first.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def append(self, node):
        self.next = node


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        walker = head
        runner = head
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True
        return False


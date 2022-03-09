from typing import List
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.val} left: {self.left} right: {self.right}"


def bfs_traversal(root: TreeNode) -> List[int]:
    if not root:
        return []
    queue = deque()
    queue.append(root)
    result = []
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    return result

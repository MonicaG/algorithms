from data_structures.trees.TreeNode import TreeNode
from typing import List
from collections import deque


def inorder(tree: TreeNode) -> List:
    def recurse(node):
        if node is None:
            return
        recurse(node.left)
        result.append(node.value)
        recurse(node.right)
    result = []
    recurse(tree)
    return result


def preorder(tree: TreeNode) -> List:
    def recurse(node):
        if node is None:
            return
        result.append(node.value)
        recurse(node.left)
        recurse(node.right)
    result = []
    recurse(tree)
    return result


def postorder(tree: TreeNode) -> List:
    def recurse(node):
        if node is None:
            return
        recurse(node.left)
        recurse(node.right)
        result.append(node.value)
    result = []
    recurse(tree)
    return result


def level_order(tree: TreeNode) -> List:
    queue = deque()
    result = []
    queue.append(tree)
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.value)
            queue.append(node.left)
            queue.append(node.right)
    return result

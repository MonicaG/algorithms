from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val}, {self.left}, {self.right})'


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node, left_val, right_val) -> bool:
            if node is None:
                return True
            print(f"node: {node}, left_value: {left_val}, right_Value: {right_val}")
            if not(left_val < node.val < right_val):
                return False

            return is_valid(node.left, left_val, node.val) and is_valid(node.right, node.val, right_val)

        return is_valid(root, float("-INF"), float("INF"))
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node({self.value}, {self.left}, {self.right})'

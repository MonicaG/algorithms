from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        # The index of the preorder array element currently being processed
        self.preorder_index = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def make_tree(start, end):
            """
            :param start: the index to start at in the inorder array
            :param end: the index to end at in the inorder array
            :return: the TreeNode structure or None if the end index is less than the start index
            """
            if end < start:
                return None
            root = TreeNode(preorder[self.preorder_index])
            self.preorder_index += 1
            root_index = location[root.val]
            root.left = make_tree(start, root_index - 1)
            root.right = make_tree(root_index + 1, end)
            return root

        location = {}
        # set self.preorder_index to 0 in case the buildTree method is called multiple times on the Solution instance.
        # If it wasn't set then the self.preorder_index would be a value used in the previous invocation.
        self.preorder_index = 0
        for index, value in enumerate(inorder):
            location[value] = index
        return make_tree(0, len(inorder) - 1)

    # def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    #     def insert(tree, new_node):
    #         if location[new_node.val] - location[tree.val] < 0:
    #             if tree.left:
    #                 insert(tree.left, new_node)
    #             else:
    #                 tree.left = new_node
    #         else:
    #             if tree.right:
    #                 insert(tree.right, new_node)
    #             else:
    #                 tree.right = new_node
    #     location = {}
    #     for index, value in enumerate(inorder):
    #         location[value] = index
    #
    #     root = TreeNode(preorder[0])
    #     for i in range(1, len(preorder)):
    #         insert(root, TreeNode(preorder[i]))
    #     return root


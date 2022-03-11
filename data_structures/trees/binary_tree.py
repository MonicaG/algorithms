from data_structures.trees.TreeNode import TreeNode


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def __repr__(self):
        return f'BinaryTree({self.root})'

    def print_tree_inorder(self):
        self.__print_tree_inorder(self.root)

    def __print_tree_inorder(self, node):
        if node is None:
            return
        self.__print_tree_inorder(node.left)
        print(node.value)
        self.__print_tree_inorder(node.right)

    def print_tree_preorder(self):
        self.__print_tree_preorder(self.root)

    def __print_tree_preorder(self, node):
        if node is None:
            return
        else:
            print(node.value)
            self.__print_tree_preorder(node.left)
            self.__print_tree_preorder(node.right)

    def empty(self):
        return self.root is None

    def find_greatest_value(self):
        return self.__find_greatest_value(self.root)

    def __find_greatest_value(self, node):
        if node is None:
            return None
        elif node.right is None:
            return node.value
        else:
            return self.__find_greatest_value(node.right)

    def insert(self, value):
        self.__insert(value, self.root)

    def __insert(self, value, node=None):
        if self.empty():
            self.root = TreeNode(value)
            return
        elif value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self.__insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self.__insert(value, node.right)

    def delete(self, value):
        self.__delete(value, self.root)

    def __delete(self, value, node):
        if node is None:
            return None
        elif value < node.value:
            self.__delete(value, node.left)
            return node
        elif value > node.value:
            self.__delete(value, node.right)
            return node
        else:
            # value == node.value
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.right = self.__lift(node.right, node)
                return node

    def __lift(self, node, nodeToDelete):
        if node.left:
            node.left = self.__lift(node.left, nodeToDelete)
            return node
        else:
            nodeToDelete.value = node.value
            return node.right




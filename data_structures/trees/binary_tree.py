class Node:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left_child = left
        self.right_child = right

    def __repr__(self):
        return f'Node({self.value}, {self.left_child}, {self.right_child})'


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
        self.__print_tree_inorder(node.left_child)
        print(node.value)
        self.__print_tree_inorder(node.right_child)

    def print_tree_preorder(self):
        self.__print_tree_preorder(self.root)

    def __print_tree_preorder(self, node):
        if node is None:
            return
        else:
            print(node.value)
            self.__print_tree_preorder(node.left_child)
            self.__print_tree_preorder(node.right_child)

    def empty(self):
        return self.root is None

    def find_greatest_value(self):
        return self.__find_greatest_value(self.root)

    def __find_greatest_value(self, node):
        if node is None:
            return None
        elif node.right_child is None:
            return node.value
        else:
            return self.__find_greatest_value(node.right_child)

    def insert(self, value):
        self.__insert(value, self.root)

    def __insert(self, value, node=None):
        if self.empty():
            self.root = Node(value)
            return
        elif value < node.value:
            if node.left_child is None:
                node.left_child = Node(value)
            else:
                self.__insert(value, node.left_child)
        elif value > node.value:
            if node.right_child is None:
                node.right_child = Node(value)
            else:
                self.__insert(value, node.right_child)

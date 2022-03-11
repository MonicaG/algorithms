import pytest
from data_structures.trees.TreeNode import TreeNode
from data_structures.trees.tree_traversal import inorder, preorder, postorder, level_order

@pytest.fixture
def tree():
    """
            10
           /  \
          5   15
        / \   / \
      3   7  12  20

    """
    node10 = TreeNode(10)
    node5 = TreeNode(5)
    node3 = TreeNode(3)
    node7 = TreeNode(7)
    node15 = TreeNode(15)
    node12 = TreeNode(12)
    node20 = TreeNode(20)

    node5.left = node3
    node5.right = node7

    node15.left = node12
    node15.right = node20

    node10.left = node5
    node10.right = node15
    return node10


@pytest.fixture
def unbalanced_tree():
    """
               10
              /  \
             7   15
           /     / \
         4     12  20
          \
          6
         /
        5
       """

    node10 = TreeNode(10)
    node7 = TreeNode(7)
    node4 = TreeNode(4)
    node6 = TreeNode(6)
    node5 = TreeNode(5)
    node15 = TreeNode(15)
    node12 = TreeNode(12)
    node20 = TreeNode(20)

    node7.left = node4
    node4.right = node6
    node6.left = node5

    node15.left = node12
    node15.right = node20

    node10.left = node7
    node10.right = node15
    return node10


def test_inorder(tree):
    result = inorder(tree)
    assert result == [3, 5, 7, 10, 12, 15, 20]


def test_inorder_unbalanced(unbalanced_tree):
    result = inorder(unbalanced_tree)
    assert result == [4, 5, 6, 7, 10, 12, 15, 20]


def test_inorder_empty():
    assert inorder(None) == []


def test_inorder_one_element():
    root = TreeNode(5)
    assert inorder(root) == [5]


def test_preorder(tree):
    result = preorder(tree)
    assert result == [10, 5, 3, 7, 15, 12, 20]


def test_preorder_unbalanced(unbalanced_tree):
    result = preorder(unbalanced_tree)
    assert result == [10, 7, 4, 6, 5, 15, 12, 20]


def test_preorder_empty():
    assert preorder(None) == []


def test_preorder_one_element():
    root = TreeNode(5)
    assert preorder(root) == [5]


def test_postorder(tree):
    result = postorder(tree)
    assert result == [3, 7, 5, 12, 20, 15, 10]


def test_postorder_unbalanced(unbalanced_tree):
    result = postorder(unbalanced_tree)
    assert result == [5, 6, 4, 7, 12, 20, 15, 10]


def test_postorder_empty():
    assert postorder(None) == []


def test_postorder_one_element():
    root = TreeNode(5)
    assert postorder(root) == [5]


def test_leve_order(tree):
    result = level_order(tree)
    assert result == [10, 5, 15, 3, 7, 12, 20]


def test_level_order_unbalanced(unbalanced_tree):
    result = level_order(unbalanced_tree)
    assert result == [10, 7, 15, 4, 12, 20, 6, 5]


def test_level_order_empty():
    assert level_order(None) == []


def test_level_order_one_element():
    root = TreeNode(5)
    assert level_order(root) == [5]
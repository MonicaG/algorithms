import pytest
from algorithms.search.breadth_first_search_tree import bfs_traversal, TreeNode


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


def test(tree):
    result = bfs_traversal(tree)
    assert [10, 5, 15, 3, 7, 12, 20] == result


def test_empty():
    root = None
    result = bfs_traversal(root)
    assert [] == result


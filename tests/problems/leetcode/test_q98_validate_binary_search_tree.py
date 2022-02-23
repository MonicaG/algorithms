from problems.leetcode.q98_validate_binary_search_tree import TreeNode, Solution


def test_invalid_tree():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3, n1, n2)
    n6 = TreeNode(6)
    n12 = TreeNode(12)
    n19 = TreeNode(19)
    n15 = TreeNode(15, n12, n19)
    n9 = TreeNode(9, n6, n15)
    n5 = TreeNode(5, n3, n9)

    sol = Solution()
    assert sol.isValidBST(n5) is False


def test_valid_tree():
    n1 = TreeNode(1)
    n4 = TreeNode(4)
    n3 = TreeNode(3, n1, n4)
    n6 = TreeNode(6)
    n12 = TreeNode(12)
    n19 = TreeNode(19)
    n15 = TreeNode(15, n12, n19)
    n9 = TreeNode(9, n6, n15)
    n5 = TreeNode(5, n3, n9)

    sol = Solution()
    assert sol.isValidBST(n5)

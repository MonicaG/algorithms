from problems.leetcode.q297_serialize_and_deserialize_binary_tree import Codec
from problems.leetcode.q105_construct_binary_tree_from_preorder_and_inorder_traversal import Solution


def test_leet_code_ex1():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    sol = Solution()
    codec = Codec()
    result = sol.buildTree(preorder, inorder)
    serial_result = codec.serialize(result)
    assert serial_result == "3,9,20,n,n,15,7,n,n,n,n"


def test_leet_code_ex2():
    preorder = [-1]
    inorder = [-1]
    sol = Solution()
    codec = Codec()
    result = sol.buildTree(preorder, inorder)
    serial_result = codec.serialize(result)
    assert serial_result == "-1,n,n"


def test_left_only_nodes():
    preorder = [7, 10, 9, 4]
    inorder = [4, 9, 10, 7]
    sol = Solution()
    codec = Codec()
    result = sol.buildTree(preorder, inorder)
    serial_result = codec.serialize(result)
    assert serial_result == "7,10,n,9,n,4,n,n,n"


def test_right_only_nodes():
    preorder = [15, 10, 25, 17]
    inorder = [15, 10, 25, 17]
    sol = Solution()
    codec = Codec()
    result = sol.buildTree(preorder, inorder)
    serial_result = codec.serialize(result)
    assert serial_result == "15,n,10,n,25,n,17,n,n"


def test_balanced_tree():
    preorder = [20, 15, 10, 5, 12, 17, 16, 19, 30, 25, 23, 27, 40, 35, 45]
    inorder = [5, 10, 12, 15, 16, 17, 19, 20, 23, 25, 27, 30, 35, 40, 45]
    sol = Solution()
    codec = Codec()
    result = sol.buildTree(preorder, inorder)
    serial_result = codec.serialize(result)
    assert serial_result == "20,15,30,10,17,25,40,5,12,16,19,23,27,35,45,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n"

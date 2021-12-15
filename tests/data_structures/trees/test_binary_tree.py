from data_structures.trees.binary_tree import BinaryTree


def test_binary_tree_insert():
    bt = BinaryTree()
    bt.insert(10)
    bt.insert(5)
    bt.insert(15)
    bt.insert(12)
    bt.insert(7)

    assert bt.root.value == 10
    assert bt.root.left_child.value == 5
    assert bt.root.right_child.value == 15
    assert bt.root.right_child.left_child.value == 12
    assert bt.root.left_child.right_child.value == 7


def test_find_greatest_value():
    bt = BinaryTree()
    bt.insert(10)
    bt.insert(5)
    bt.insert(7)
    bt.insert(15)
    bt.insert(20)
    bt.insert(17)
    bt.insert(23)
    bt.insert(4)
    bt.insert(9)
    assert bt.find_greatest_value() == 23

    bt2 = BinaryTree()
    assert bt2.find_greatest_value() is None


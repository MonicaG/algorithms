from problems.leetcode.q297_serialize_and_deserialize_binary_tree import Codec


def test_leet_code_example():
    input_str = "1,2,3,n,n,4,5,n,n,n,n"
    codec = Codec()
    node = codec.deserialize(input_str)
    result = codec.serialize(node)
    assert result == input_str


def test_one_node():
    input_str = "4,n,n"
    codec = Codec()
    node = codec.deserialize(input_str)
    result = codec.serialize(node)
    assert result == input_str


def test_empty_tree():
    input_str = ""
    codec = Codec()
    node = codec.deserialize(input_str)
    result = codec.serialize(node)
    assert result == input_str


def test_tree():
    input_str = "10,5,20,3,7,15,30,2,4,6,8,n,17,25,35,n,n,n,n,n,n,n,n,n,n,n,n,n,n"
    codec = Codec()
    node = codec.deserialize(input_str)
    result = codec.serialize(node)
    assert result == input_str


def test_full_tree():
    input_str="10,5,15,3,7,12,20,n,n,n,n,n,n,n,n"
    codec = Codec()
    node = codec.deserialize(input_str)
    result = codec.serialize(node)
    assert result == input_str


def test_left_children_only_tree():
    input_str = "50,40,n,30,n,20,n,n,n"
    codec = Codec()
    node = codec.deserialize(input_str)
    result = codec.serialize(node)
    assert result == input_str


def test_right_children_only_tree():
    input_str = "50,n,60,n,70,n,80,n,n"
    codec = Codec()
    node = codec.deserialize(input_str)
    result = codec.serialize(node)
    assert result == input_str
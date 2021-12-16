from data_structures.heap.max_binary_heap import MaxHeap


def test_max_heap_insert():
    heap = MaxHeap()
    heap.insert(55)
    heap.insert(22)
    heap.insert(34)
    heap.insert(10)
    heap.insert(2)
    heap.insert(99)
    heap.insert(68)
    assert heap.get_list() == [99, 22, 68, 10, 2, 34, 55]


def test_pop():
    heap = MaxHeap()
    heap.insert(55)
    heap.insert(22)
    heap.insert(34)
    heap.insert(10)
    heap.insert(2)
    heap.insert(99)
    heap.insert(68)

    assert heap.pop() == 99
    assert heap.get_list() == [68, 22, 55, 10, 2, 34]
    assert heap.pop() == 68
    assert heap.get_list() == [55, 22, 34, 10, 2]
    assert heap.pop() == 55
    assert heap.get_list() == [34, 22, 2, 10]
    assert heap.pop() == 34
    assert heap.get_list() == [22, 10, 2]
    assert heap.pop() == 22
    assert heap.get_list() == [10, 2]
    assert heap.pop() == 10
    assert heap.get_list() == [2]
    assert heap.pop() == 2
    assert heap.get_list() == []

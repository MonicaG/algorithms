from problems.leetcode.q206_reverse_link_list import Solution, ListNode


def test_iterative():
    sol = Solution()
    node4 = ListNode(4)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    node = sol.reverseListIterative(node1)
    assert node.val == 4
    assert node.next.val == 3
    assert node.next.next.val == 2
    assert node.next.next.next.val == 1
    assert node.next.next.next.next is None


def test_iterative_empty():
    sol = Solution()

    node = sol.reverseListIterative(None)
    assert node is None


def test_iterative_one_element():
    sol = Solution()

    node1 = ListNode(1)
    node = sol.reverseListIterative(node1)
    assert node is node1


def test_iterative_two_elements():
    sol = Solution()

    node2 = ListNode(2)
    node1 = ListNode(1, node2)
    node = sol.reverseListIterative(node1)
    assert node.val == 2
    assert node.next.val == 1
    assert node.next.next is None


def test_recursive():
    sol = Solution()
    node4 = ListNode(4)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    node = sol.reverseListRecursive(node1)
    assert node.val == 4
    assert node.next.val == 3
    assert node.next.next.val == 2
    assert node.next.next.next.val == 1
    assert node.next.next.next.next is None


def test_recursive_empty():
    sol = Solution()

    node = sol.reverseListRecursive(None)
    assert node is None


def test_recursive_one_element():
    sol = Solution()

    node1 = ListNode(1)
    node = sol.reverseListRecursive(node1)
    assert node is node1


def test_recursive_two_elements():
    sol = Solution()

    node2 = ListNode(2)
    node1 = ListNode(1, node2)
    node = sol.reverseListRecursive(node1)
    assert node.val == 2
    assert node.next.val == 1
    assert node.next.next is None

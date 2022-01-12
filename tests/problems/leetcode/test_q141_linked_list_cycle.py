from problems.leetcode.q141_linked_list_cycle import Solution, ListNode


def test_solution_no_cycle():
    sol = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node3.append(node4)
    node2.append(node3)
    node1.append(node2)

    assert sol.hasCycle(node1) is False


def test_solution_has_cycle():
    sol = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node4.append(node2)
    node3.append(node4)
    node2.append(node3)
    node1.append(node2)

    assert sol.hasCycle(node1)


def test_solution_has_cycle_to_itself():
    sol = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node4.append(node4)
    node3.append(node4)
    node2.append(node3)
    node1.append(node2)

    assert sol.hasCycle(node1)


def test_solution_empty():
    sol = Solution()
    assert sol.hasCycle(None) is False


def test_solution_one_node_no_cycle():
    sol = Solution()
    node1 = ListNode(1)
    assert sol.hasCycle(node1) is False


def test_solution_one_node_with_cycle():
    sol = Solution()
    node1 = ListNode(1)
    node1.append(node1)
    assert sol.hasCycle(node1)

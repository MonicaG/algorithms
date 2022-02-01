import pytest
from algorithms.search.depth_first_search_graph import dfs, dfs_traverse, dfs_traversal_iterative


@pytest.fixture
def graph():
    return {
        "A": ["B", "C", "D"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B", "D"],
        "E": ["B", "F"],
        "F": ["C", "E", "G"],
        "G": ["F"],
    }


def test_dfs(graph):
    assert dfs(graph, "C", "B") is True
    assert dfs(graph, "C", "X") is False
    assert dfs(graph, "X", "B") is False
    assert dfs(graph, "G", "A") is True
    assert dfs(graph, "F", "B") is True


def test_dfs_traverse(graph):
    assert dfs_traverse(graph, "A") == ["B", "D", "E", "F", "C", "G"]
    assert dfs_traverse(graph, "B") == ["A", "C", "F", "E", "G", "D"]
    assert dfs_traverse(graph, "C") == ["A", "B", "D", "E", "F", "G"]
    assert dfs_traverse(graph, "D") == ["B", "A", "C", "F", "E", "G"]
    assert dfs_traverse(graph, "E") == ["B", "A", "C", "F", "G", "D"]
    assert dfs_traverse(graph, "F") == ["C", "A", "B", "D", "E", "G"]
    assert dfs_traverse(graph, "G") == ["F", "C", "A", "B", "D", "E"]
    assert dfs_traverse(graph, "X") == []


def test_dfs_traverse_iterative(graph):
    assert dfs_traversal_iterative(graph, "A") == ["B", "D", "E", "F", "C", "G"]
    assert dfs_traversal_iterative(graph, "B") == ["A", "C", "F", "E", "G", "D"]
    assert dfs_traversal_iterative(graph, "C") == ["A", "B", "D", "E", "F", "G"]
    assert dfs_traversal_iterative(graph, "D") == ["B", "A", "C", "F", "E", "G"]
    assert dfs_traversal_iterative(graph, "E") == ["B", "A", "C", "F", "G", "D"]
    assert dfs_traversal_iterative(graph, "F") == ["C", "A", "B", "D", "E", "G"]
    assert dfs_traversal_iterative(graph, "G") == ["F", "C", "A", "B", "D", "E"]
    assert dfs_traversal_iterative(graph, "X") == []

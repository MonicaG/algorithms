import pytest
from algorithms.search.breadth_first_search_graph import bfs, bfs_traversal


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


def test_bfs_traversal(graph):

    assert bfs_traversal(graph, "A") == ["B", "C", "D", "E", "F", "G"]
    assert bfs_traversal(graph, "B") == ["A", "D", "E", "C", "F", "G"]
    assert bfs_traversal(graph, "C") == ["A", "F", "B", "D", "E", "G"]
    assert bfs_traversal(graph, "D") == ["B", "A", "E", "C", "F", "G"]
    assert bfs_traversal(graph, "E") == ["B", "F", "A", "D", "C", "G"]
    assert bfs_traversal(graph, "F") == ["C", "E", "G", "A", "B", "D"]
    assert bfs_traversal(graph, "G") == ["F", "C", "E", "A", "B", "D"]
    assert bfs_traversal(graph, "X") == []


def test_bfs(graph):
    assert bfs(graph, "A", "G") is True
    assert bfs(graph, "A", "X") is False
    assert bfs(graph, "X", "A") is False
    assert bfs(graph, "G", "A") is True
    assert bfs(graph, "F", "B") is True
    assert bfs(graph, "G", "G") is True



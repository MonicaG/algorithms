from typing import Dict, List


def dfs_traversal_iterative(graph: Dict, start: str) -> List[str]:
    if graph is None or start is None or start not in graph:
        return []

    result = []
    stack = []
    visited = {}
    stack.append(start)
    visited[start] = True
    while stack:
        item = stack.pop()

        if item not in visited:
            result.append(item)
            visited[item] = True

        # reversed is used here to give the same result as the recursive traversal. If reversed is not used, then the
        # algorithm would walk from last item in the adjacent vertices list to the first. This is because of the order
        # in which vertices are pushed onto the stack
        for vertex in reversed(graph[item]):
            if vertex not in visited:
                stack.append(vertex)

    return result


def dfs(graph: Dict, start: str, target: str, visited=None) -> bool:
    """
    Keep track of the vertices visited. If we come across a vertex that has not been processed, then iterate over its
    list of adjacent vertices. Recursively call the dfs function for each of the adjacent vertices.
    :param graph: A simple graph definition using a dict. The key is the vertex, the value is an array of adjacent
    vertices.
    :param start: The vertex to start searching at
    :param target: The vertex to find
    :param visited: Used by the recursion to mark which vertices we have already processed
    :return: True if the target is in the graph, false otherwise
    """
    if graph is None or start is None or target is None or start not in graph:
        return False
    # Why visited=None and this? See https://docs.python-guide.org/writing/gotchas/
    if visited is None:
        visited = {}
    if target == start:
        return True
    visited[start] = True
    for vertex in graph[start]:
        if vertex not in visited:
            return dfs(graph, vertex, target, visited)
    return False


def dfs_traverse(graph: Dict, start: str, visited=None, result=None) -> List[str]:
    if graph is None or start is None or start not in graph:
        return []
    if result is None:
        result = []

    if visited is None:
        visited = {}
    visited[start] = True
    for vertex in graph[start]:
        if vertex not in visited:
            result.append(vertex)
            dfs_traverse(graph, vertex, visited, result)
    return result

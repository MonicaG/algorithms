from typing import List, Dict
from collections import deque


def bfs(graph: Dict, start: str, target: str) -> bool:
    if graph is None or start is None or target is None or start not in graph:
        return False
    if start == target:
        return True
    queue = deque()
    visited = {}
    queue.append(start)
    visited[start] = True
    while queue:
        item = queue.popleft()
        for vertex in graph[item]:
            if vertex == target:
                return True
            if vertex not in visited:
                visited[vertex] = True
                queue.append(vertex)
    return False


def bfs_traversal(graph: Dict, start: str) -> List[str]:
    if graph is None or start is None or start not in graph:
        return []
    result = []
    queue = deque()
    visited = {}
    queue.append(start)
    visited[start] = True
    while queue:
        item = queue.popleft()
        for vertex in graph[item]:
            if vertex not in visited:
                visited[vertex] = True
                queue.append(vertex)
                result.append(vertex)
    return result

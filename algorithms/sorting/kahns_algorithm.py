'''
Kahn's algorithm - used for finding a topological sort (ordering) of a directed acyclic graph.
See: https://app.gitbook.com/s/6JbWoYwqVgAwosJzOAwN/algorithms/kahns-algorithm
'''
from typing import List
from collections import defaultdict, deque


class Graph:

    __MIN_VALUE__ = 0
    
    def __init__(self, num_vertices):
        self.graph = defaultdict(list)
        self.num_vertices = num_vertices

    def __is_valid__(self, num: int) -> bool:
        return num >= Graph.__MIN_VALUE__ and num < self.num_vertices

    def add_edge(self, u: int, v: int):
        '''
        Add an edge from vertex u to vertex v
        '''
        if not self.__is_valid__(u) or not self.__is_valid__(v):
            raise Exception(f"Invalid vertex value. Must be between {Graph.__MIN_VALUE__}  and {self.num_vertices}")
        self.graph[u].append(v)

    def add_non_connected_vertex(self, u):
        self.graph[u].append(None)



class Kahns:
   def kahn(self, graph: Graph) -> List[int]:
        # this array keeps track of how many edges are incoming to a vertex (how many dependecies a course has)
        # because the vertices ints an array can be used. The array index is the vertex int
        incoming_edges = [0] * graph.num_vertices

        # populate the incoming_edges with the number of incoming edges for each vertex
        for u in graph.graph:
            for v in graph.graph[u]:
                if v:
                    incoming_edges[v] += 1


        # initialize the queue with any vertices that do NOT have any incoming edges (0 dependencies)
        processing_queue = deque()
        for vertex, edges in enumerate(incoming_edges):
            if edges == 0:
                processing_queue.append(vertex)

       
        topo_sort = []
        num_vertices_processed = 0
        while processing_queue:
            vertex = processing_queue.pop()
            num_vertices_processed += 1
            topo_sort.append(vertex)
            for v in graph.graph[vertex]:
                if v:
                    incoming_edges[v] -= 1
                    if incoming_edges[v] == 0:
                        processing_queue.append(v)

        # The graph contains a cycle if these two values do not match
        if num_vertices_processed != graph.num_vertices:
            raise Exception("Invalid graph")
        return topo_sort

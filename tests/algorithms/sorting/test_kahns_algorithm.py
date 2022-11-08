import pytest
from algorithms.sorting.kahns_algorithm import Graph, Kahns
class TestKahnsAlogorithm:

    def test_test_two_vertices_no_cycle(self):
        graph = Graph(2)
        graph.add_edge(0, 1)
        algo = Kahns()
        assert algo.kahn(graph) == [0, 1]

    def test_non_connected_graph_no_cycle(self):
         graph = Graph(6)
         graph.add_edge(0, 1)
         graph.add_edge(0, 4)
         graph.add_edge(1, 2)
         graph.add_edge(2, 4)
         graph.add_edge(1, 3)
         graph.add_non_connected_vertex(5)

         algo = Kahns()
         assert algo.kahn(graph) == [5, 0, 1, 3, 2, 4]
        

    def test_graph_with_cycles(self):
         graph = Graph(5)
         graph.add_edge(0, 1)
         graph.add_edge(0, 4)
         graph.add_edge(1, 2)
         graph.add_edge(2, 4)
         graph.add_edge(1, 3)
         graph.add_edge(4, 1)

         algo = Kahns()
         with pytest.raises(Exception):
            algo.kahn(graph)
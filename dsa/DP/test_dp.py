from dsa.DP.binomial_coefficient import binomial_coefficient
from dsa.DP.fibonacci import fib
from dsa.DP.sssp import shortest_path
from dsa.graphs.graph import Graph


def test_binomial_coeffient():
    assert binomial_coefficient(1, 1) == 1
    assert binomial_coefficient(5, 5) == 1
    assert binomial_coefficient(5, 2) == 10
    assert binomial_coefficient(37, 4) == 66045


def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2

    assert fib(23) == 28657


def test_sp():
    edges = [[1, 2, 1], [1, 3, 3], [2, 4, 3], [3, 4, 1], [2, 3, 1]]
    graph = Graph(edges, True)
    adj = graph.get_node(1)
    assert adj == [2, 3]
    assert graph.get_inverse_edges(1) == []
    cost, path = shortest_path(graph, 1, 4)
    assert cost == 3
    assert path == [(1, 2), (2, 3), (3, 4)]

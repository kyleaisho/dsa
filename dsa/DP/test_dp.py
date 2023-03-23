from dsa.DP.binomial_coefficient import binomial_coefficient
from dsa.DP.fibonacci import fib
from dsa.DP.sssp import shortest_path
from dsa.graphs.graph import Graph
from dsa.DP.text_justification import (
    justify,
    justify_recursive,
    generate_matrix,
    calculate_splits,
    get_unpadded_lines,
)
from dsa.DP.edit_distance import edit_distance


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


def test_justification():
    inf = float("inf")
    COL_WIDTH = 10
    words = ["Xander", "boy", "likes", "to", "code"]
    ans_matrix = [
        [16, 0, inf, inf, inf],
        [inf, 49, 1, inf, inf],
        [inf, inf, 25, 4, inf],
        [inf, inf, inf, 64, 9],
        [inf, inf, inf, inf, 36],
    ]
    ans_splits = [1, 3, 3, 5, 5]
    ans_lines = [["Xander"], ["boy", "likes"], ["to", "code"]]
    ans = ["Xander    ", "boy  likes", "to    code"]

    matrix = generate_matrix(words, COL_WIDTH)
    splits, costs = calculate_splits(matrix)
    lines = get_unpadded_lines(words, splits)
    assert matrix == ans_matrix
    assert splits == ans_splits
    assert lines == ans_lines
    assert justify(words, COL_WIDTH) == ans


def test_justification_recursive():
    COL_WIDTH = 10
    words = ["Xander", "boy", "likes", "to", "code"]

    assert justify(words, COL_WIDTH) == justify_recursive(words, COL_WIDTH)


def test_edit_distance():
    word1 = "intention"
    word2 = "execution"
    edit_cost = 5

    assert edit_distance(word1, word2) == edit_cost
    assert edit_distance("zoologicoarchaeologist", "zoogeologist") == 10

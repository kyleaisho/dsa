from dsa.graphs.build_adj_list import build_weighted
from typing import List, Tuple, Any
from dsa.graphs.node import Node


class Graph:
    def __init__(self, edges: List[Tuple[Any, Any, int]], directed: bool) -> None:
        self._edges = edges
        self._directed = directed
        self._adj = {}
        self._weights = {}
        self._inverse_edges = {}
        self.build_weighted()

    def __getitem__(self, name):
        return self._adj[name]

    def __iter__(self):
        return iter(self._adj)

    def keys(self):
        return self._adj.keys()

    def items(self):
        return self._adj.items()

    def values(self):
        return self._adj.values()

    def build_weighted(self):
        weights = self._weights
        adj = self._adj
        inv_edges = self._inverse_edges

        for u, v, w in self._edges:
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            if u not in weights:
                weights[u] = {}
            if v not in weights:
                weights[v] = {}
            if u not in inv_edges:
                inv_edges[u] = []
            if v not in inv_edges:
                inv_edges[v] = []

            adj[u].append(v)
            inv_edges[v].append(u)
            weights[u][v] = w

    def get_node(self, key) -> Node:
        if key in self._adj:
            return self._adj[key]
        return None

    def weight(self, u: Node, v: Node):
        return self._weights[u][v]

    # def build_inverse_edges(self):
    #     G = self._graph
    #     edges = self._inverse_edges
    #     for u in G.values():
    #         if u not in edges:
    #             edges[u] = []
    #         for v in u.adj:
    #             if u not in edges:
    #                 edges[u] = []
    #             edges[u] = v

    def get_inverse_edges(self, v: Node):
        if v in self._inverse_edges:
            return self._inverse_edges[v]
        return []

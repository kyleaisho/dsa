from dsa.graphs.graph import Graph


class Results:
    def __init__(self, source, destination) -> None:
        self.src = source
        self.dest = destination
        self.parent = {}
        self.d = {}


def shortest_path(G: Graph, src, dest):
    res = Results(src, dest)

    res.parent[src] = None
    res.d[src] = 0
    for u in G:
        dp_sp(G, u, res)

    path_edges = []
    curr = dest
    parent = res.parent[curr]
    while parent is not None:
        path_edges.insert(0, (parent, curr))
        curr = parent
        parent = res.parent[parent]

    return res.d[dest], path_edges


def dp_sp(G: Graph, v, res):
    if v in res.d:
        return res.d[v]
    res.d[v] = float("inf")
    res.parent[v] = None
    adj = G.get_inverse_edges(v)
    for u in adj:
        new_cost = dp_sp(G, u, res) + G.weight(u, v)
        if new_cost < res.d[v]:
            res.d[v] = new_cost
            res.parent[v] = u
    return res.d[v]

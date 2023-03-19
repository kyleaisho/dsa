from dsa.graphs.node import Node
from dsa.graphs.visualize import GraphVisualization


def build_from_tuple(*args, **kwargs):
    return build_weighted(*args, **kwargs)


def build_weighted(nodes, directed=True):
    graph = {}
    weights = {}
    graph["__weights"] = weights
    import pudb

    pudb.set_trace()
    for edge in nodes:
        node = edge[0]
        neighbor = edge[1]
        weight = 1
        if len(edge) > 2:
            weight = edge[2]
        if node not in graph:
            graph[node] = Node(node)
        if neighbor not in graph:
            graph[neighbor] = Node(neighbor)
        if node not in weights:
            weights[node] = {}

        weights[node][neighbor] = weight

        graph[node].adj.append(neighbor)

        if not directed:
            graph[neighbor].adj.append(node)

    return graph


def print_graph(V, directed=False, weighted=False):
    gv = GraphVisualization(directed, weighted)
    seen = set()

    for v in V:
        if v in seen:
            continue
        seen.add(v)
        for u in V[v].adj:
            gv.add_edge(v, u)

    gv.visualize()

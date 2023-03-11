from node import Node
from visualize import GraphVisualization


def build_from_tuple(nodes, directed=True):
    graph = {}

    for node, neighbor in nodes:
        if node not in graph:
            graph[node] = Node(node, node)
        if neighbor not in graph:
            graph[neighbor] = Node(neighbor, neighbor)

        graph[node].adj.append(neighbor)

        if not directed:
            graph[neighbor].adj.append(node)

    return graph


def print_graph(V, directed=False):
    gv = GraphVisualization(directed)
    seen = set()

    for v in V:
        if v in seen:
            continue
        seen.add(v)
        for u in V[v].adj:
            gv.add_edge(v, u)

    gv.visualize()

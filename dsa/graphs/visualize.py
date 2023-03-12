# First networkx library is imported
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt


# Defining a Class
class GraphVisualization:
    def __init__(self, directed=False, weighted=False):
        # visual is a list which stores all
        # the set of edges that constitutes a
        # graph
        self.directed = directed
        self.weighted = weighted
        self.G = nx.DiGraph() if self.directed else nx.Graph()
        self.edges = []

    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def add_edge(self, u, v, **kwargs):
        self.G.add_edge(u, v, **kwargs)
        self.edges.append((u, v))

    def draw_graph(self):
        G = self.G
        pos = nx.spring_layout(self.G, seed=7)
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, self.edges)

        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels)
        return pos

    def visualize(self):
        self.draw_graph()
        plt.show()

    def draw_path(self, edges):
        G = self.G
        pos = self.draw_graph()
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color="red")
        plt.show()

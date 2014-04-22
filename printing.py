import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph, labels=None,
               node_size=200, node_color='blue', node_alpha=1,
               edge_color='black', edge_alpha=0.7, edge_tickness=1,
               edge_text_pos=0.3):

    G = nx.Graph()

    for node in graph:
        for edge in node.edges:
            G.add_edge(node.index, edge.index)

    graph_pos = {}
    node_color = []
    for node in graph:
        graph_pos[node.index] = (node.x, node.y)
        node_color.append(node.color)

    nx.draw_networkx_nodes(G, graph_pos, node_size=node_size, alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G, graph_pos, width=edge_tickness, alpha=edge_alpha, edge_color=edge_color)

    plt.show()

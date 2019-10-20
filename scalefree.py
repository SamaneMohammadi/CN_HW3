from random import seed
import networkx as nx
import matplotlib.pyplot as plt

#create a graph with degrees following a power law distribution
s = nx.utils.powerlaw_sequence(100, 2.2) #100 nodes, power-law exponent 2.5
G = nx.expected_degree_graph(s, selfloops=True)

print(G.nodes())
print(G.edges())
graph = nx.configuration_model(G, seed=seed)
loops = graph.selfloop_edges()
# remove parallel edges and self-loops
print("number of selfloop edge:",loops)
graph = nx.Graph(graph)
graph.remove_edges_from(loops)



#draw and show graph
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
plt.show()

import networkx as nx
import random

# Erdos-Reyni Model
n = 5242
m = 14484
er = nx.gnm_random_graph(n, m, directed=False)

ac_er = nx.average_clustering(er)

# Small-World Model
k = 4
p = 0
sw = nx.newman_watts_strogatz_graph(n, k, p, seed=None)

for i in range(4000):
    while True:
        random_new_edge = (random.sample(range(1, n), 2))
        if not (sw.has_edge(random_new_edge[0], random_new_edge[1])):
            # print(random_new_edge)
            sw.add_edge(random_new_edge[0], random_new_edge[1])
            break

ac_sw = nx.average_clustering(sw)

# Real-World Collaboration Network
ca = nx.read_edgelist("ca-GrQc.txt", comments='#', delimiter='\t')
ac_ca = nx.average_clustering(ca)

print'The average clustering coefficient for Erdos-Reyni= %f\n' \
     'The average clustering coefficient for Small-World= %f\n' \
     'The average clustering coefficient for the collaboration network= %f' % (ac_er, ac_sw, ac_ca)

import networkx as nx
import snap
import matplotlib.pyplot as plt
import random

# Erdos-Reyni Model
n = 5242
m = 14484
er = nx.gnm_random_graph(n, m, directed=False)

er_deg_dist = {}
er_keys = []
er_values = []

for v in nx.nodes(er):
    if nx.degree(er, v) in er_deg_dist:
        er_deg_dist[nx.degree(er, v)] += 1
    else:
        er_deg_dist[nx.degree(er, v)] = 1

for key in sorted(er_deg_dist.iterkeys()):
    er_keys.append(key)
    er_values.append(er_deg_dist[key])


er_values_p = [float(i) / 5242 for i in er_values]

print(er_keys)
print(er_values_p)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(er_keys, er_values, marker='s', linestyle='--', label='ER')

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

sw_deg_dist = {}
sw_keys = []
sw_values = []

for v in nx.nodes(sw):
    if nx.degree(sw, v) in sw_deg_dist:
        sw_deg_dist[nx.degree(sw, v)] += 1
    else:
        sw_deg_dist[nx.degree(sw, v)] = 1

for key in sorted(sw_deg_dist.iterkeys()):
    sw_keys.append(key)
    sw_values.append(sw_deg_dist[key])

sw_values_p = [float(i) / 5242 for i in sw_values]


print(sw_keys)
print(sw_values_p)
ax.plot(sw_keys, sw_values, marker='*', linestyle='-.', label='SW')

# print(nx.number_of_edges(sw))

# Real-World Collaboration Network
colab_net = snap.LoadEdgeList(snap.PUNGraph, "ca-GrQc.txt", 0, 1, '\t')

snap.DelSelfEdges(colab_net)

ca_deg_dist = {}
ca_keys = []
ca_values = []

for n in colab_net.Nodes():
    if n.GetOutDeg() in ca_deg_dist:
        ca_deg_dist[n.GetDeg()] += 1
    else:
        ca_deg_dist[n.GetDeg()] = 1

for key in sorted(ca_deg_dist.iterkeys()):
    ca_keys.append(key)
    ca_values.append(ca_deg_dist[key])

ca_values_p = [float(i) / 5242 for i in ca_values]

print(ca_keys)
print(ca_values_p)
ax.plot(ca_keys, ca_values, marker='o', linestyle=':', label='CA')
plt.title('Degree Distribution')
ax.set_xscale('symlog')
ax.set_yscale('symlog')
plt.grid(True)
ax.legend()
plt.savefig('hw1-q11.pdf')
plt.show()

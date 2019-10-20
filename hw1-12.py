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

print'Erdos Reyni Random Graph'
print'Degrees: ', er_keys
print'Occurrence:', er_values
print'Prob.:', er_values_p

er_sumq = 0
for i in range(len(er_values)):
    if i != 0:
        er_sumq += er_values[i]
# print(er_sumq)

temp = er_values[1:]
er_qk = [float(i) for i in temp]
temp_keys = er_keys[1:]

er_pqk = [i / er_sumq for i in er_qk]

er_eed = 0

print'ER_qk:', er_pqk

for i in range(len(er_qk)):
    er_eed += (temp_keys[i] - 1) * er_qk[i] / er_sumq
    # print(temp_keys[i] - 1, er_qk[i] / er_sumq)
print 'ER Expected Excess Degree:', er_eed

er_ed = 0
for i in range(len(er_values_p)):
    er_ed += er_keys[i] * er_values_p[i]
print 'ER Expected Degree:', er_ed

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(er_keys[1:], er_qk, marker='s', linestyle='--', label='ER')

# Small-World Model
k = 4
p = 0
sw = nx.newman_watts_strogatz_graph(n, k, p, seed=None)

for i in range(4000):
    while True:
        random_new_edge = (random.sample(range(1, n), 2))
        if not (sw.has_edge(random_new_edge[0], random_new_edge[1])):
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

print'\nSmall-World Random Network'
print'Degrees:', sw_keys
print'Occurrence:', sw_values
print'Prob.:', sw_values_p

sw_qk = []
sw_sumq = 0
for i in sw_values:
    sw_sumq += i
# print(sw_sumq)

for i in range(len(sw_values)):
    sw_qk.append(float(sw_values[i]))

sw_pqk = [i / sw_sumq for i in sw_qk]

print'SW_qk:', sw_pqk

sw_eed = 0
for i in range(len(sw_qk)):
    sw_eed += (sw_keys[i] - 1) * sw_qk[i] / sw_sumq
print 'SW Expected Excess Degree:', sw_eed

sw_ed = 0
for i in range(len(sw_values_p)):
    sw_ed += sw_keys[i] * sw_values_p[i]
print 'SW Expected Degree:', sw_ed

ax.plot(sw_keys, sw_qk, marker='*', linestyle='-.', label='SW')

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

print'\nReal-World Collaboration Network'
print'Degrees:', ca_keys
print'Occurrence:', ca_values
print'Prob.:', ca_values_p

ca_qk = []
ca_sumq = 0
for i in range(len(ca_values)):
    if i != 0:
        ca_sumq += ca_values[i]
# print(ca_sumq)

for i in range(len(ca_values)):
    if i != 0:
        ca_qk.append(float(ca_values[i]))

ca_temp = ca_values[1:]
ca_qk = [float(i) for i in ca_temp]
ca_temp_keys = ca_keys[1:]
ca_pqk = [i / ca_sumq for i in ca_qk]
print'CA_qk:', ca_pqk
ca_eed = 0
for i in range(len(ca_qk)):
    ca_eed += (ca_temp_keys[i] - 1) * ca_qk[i] / ca_sumq
    # print(ca_temp_keys[i] - 1, ca_qk[i] / ca_sumq)
print 'CA Expected Excess Degree:', ca_eed

ca_ed = 0
for i in range(len(ca_values_p)):
    ca_ed += ca_keys[i] * ca_values_p[i]
print 'CA Expected Degree:', ca_ed

ax.plot(ca_keys[1:], ca_qk, marker='o', linestyle=':', label='CA')
plt.title('Excess Degree Distribution')
ax.set_xscale('symlog')
ax.set_yscale('symlog')
plt.grid(True)
ax.legend()
plt.savefig('hw1-q12.pdf')
plt.show()

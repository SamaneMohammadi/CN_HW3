import random
import numpy as np
import snap
import matplotlib.pyplot as plt

epi_net = snap.LoadEdgeList(snap.PNGraph, "soc-Epinions1.txt", 0, 1, '\t')
eu_net = snap.LoadEdgeList(snap.PNGraph, "email-EuAll.txt", 0, 1, '\t')

epi_nodes = []
eu_nodes = []

epi_forward = []
epi_backward = []
eu_forward = []
eu_backward = []

for v in epi_net.Nodes():
    epi_nodes.append(v.GetId())
for v in eu_net.Nodes():
    eu_nodes.append(v.GetId())

random_epi = random.sample(range(1, epi_net.GetNodes()), 100)
random_eu = random.sample(range(1, eu_net.GetNodes()), 100)

for i in range(len(random_epi)):
    results = snap.GetSubTreeSz(epi_net, random_epi[i], True, False)
    epi_forward.append(results[0])
    results = snap.GetSubTreeSz(epi_net, random_epi[i], False, True)
    epi_backward.append(results[0])

print'Epinions Forward Reachable Nodes:', epi_forward
print'Epinions Backward Reachable Nodes:', epi_backward
for i in range(len(random_eu)):
    results = snap.GetSubTreeSz(eu_net, random_eu[i], True, False)
    eu_forward.append(results[0])
    results = snap.GetSubTreeSz(eu_net, random_eu[i], False, True)
    eu_backward.append(results[0])
print'Email Forward Reachable Nodes:', eu_forward
print'Email Backward Reachable Nodes:', eu_backward

plt.subplots_adjust(hspace=0.4)
plt.subplot(221)
epi_forward_sorted = np.sort(epi_forward)
plt.step(np.arange(epi_forward_sorted.size), epi_forward_sorted)
plt.title('Epinions: Reachability using outlinks')
plt.ylabel('reached nodes')
plt.grid(True)

plt.subplot(222)
epi_backward_sorted = np.sort(epi_backward)
plt.step(np.arange(epi_backward_sorted.size), epi_backward_sorted)
plt.title('Epinions: Reachability using inlinks')
plt.ylabel('reached nodes')
plt.grid(True)

plt.subplot(223)
epi_forward_sorted = np.sort(eu_forward)
plt.step(np.arange(epi_forward_sorted.size), epi_forward_sorted)
plt.title('Email: Reachability using outlinks')
plt.ylabel('reached nodes')
plt.grid(True)

plt.subplot(224)
eu_backward_sorted = np.sort(eu_backward)
plt.step(np.arange(eu_backward_sorted.size), eu_backward_sorted)
plt.title('Email: Reachability using inlinks')
plt.ylabel('reached nodes')
plt.grid(True)

plt.savefig('hw1-q22.png')
plt.show()

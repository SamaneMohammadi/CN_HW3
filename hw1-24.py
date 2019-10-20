import random
import snap

epi_net = snap.LoadEdgeList(snap.PNGraph, "soc-Epinions1.txt", 0, 1, '\t')
eu_net = snap.LoadEdgeList(snap.PNGraph, "email-EuAll.txt", 0, 1, '\t')

EpiWcc = snap.GetMxWcc(epi_net)
EuWcc = snap.GetMxWcc(eu_net)

epi_nodes = []
eu_nodes = []

EpiWcc_nodes = []
EuWcc_nodes = []

for v in epi_net.Nodes():
    epi_nodes.append(v.GetId())
for v in eu_net.Nodes():
    eu_nodes.append(v.GetId())

for v in EpiWcc.Nodes():
    EpiWcc_nodes.append(v.GetId())
for v in EuWcc.Nodes():
    EuWcc_nodes.append(v.GetId())

repeats = [100, 500, 1000, 2000]
for r in repeats:
    epi_all = []
    epi_wcc = []
    eu_all = []
    eu_wcc = []
    for i in range(r):
        random_epi = random.sample(range(1, epi_net.GetNodes()), 2)
        while (not epi_net.IsNode(random_epi[0])) or (not epi_net.IsNode(random_epi[1])):
            random_epi = random.sample(range(1, epi_net.GetNodes()), 2)
        epi_all.append(snap.GetShortPath(epi_net, random_epi[0], random_epi[1], True))

        random_eu = random.sample(range(1, eu_net.GetNodes()), 2)
        while (not eu_net.IsNode(random_eu[0])) or (not eu_net.IsNode(random_eu[1])):
            random_eu = random.sample(range(1, eu_net.GetNodes()), 2)
        eu_all.append(snap.GetShortPath(eu_net, random_eu[0], random_eu[1], True))

    for i in range(r):
        random_epiwcc = random.sample(range(1, EpiWcc.GetNodes()), 2)
        while (not EpiWcc.IsNode(random_epiwcc[0])) or (not EpiWcc.IsNode(random_epiwcc[1])):
            random_epiwcc = random.sample(range(1, EpiWcc.GetNodes()), 2)
        epi_wcc.append(snap.GetShortPath(EpiWcc, random_epiwcc[0], random_epiwcc[1], True))

        random_euwcc = random.sample(range(1, EuWcc.GetNodes()), 2)
        while (not EuWcc.IsNode(random_euwcc[0])) or (not EuWcc.IsNode(random_euwcc[1])):
            random_euwcc = random.sample(range(1, EuWcc.GetNodes()), 2)
        eu_wcc.append(snap.GetShortPath(EuWcc, random_euwcc[0], random_euwcc[1], True))

    print'Number of Experiments: ', r
    print'Email graph All:'
    print'\tno of disconnected pairs:', eu_all.count(-1)
    print'\tFraction of connected pairs:', 1 - (float(eu_all.count(-1)) / r)

    print'Email graph WCC Only:'
    print'\tno of disconnected pairs:', eu_wcc.count(-1)
    print'\tFraction of connected pairs:', 1 - (float(eu_wcc.count(-1)) / r)

    print'Epinions graph All:1'
    print'\tno of disconnected pairs:', epi_all.count(-1)
    print'\tFraction of connected pairs:', 1 - (float(epi_all.count(-1)) / r)

    print'Epinions graph WCC Only:'
    print'\tno of disconnected pairs:', epi_wcc.count(-1)
    print'\tFraction of connected pairs:', 1 - (float(epi_wcc.count(-1)) / r)


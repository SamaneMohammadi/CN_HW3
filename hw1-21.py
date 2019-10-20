import snap

epi_net = snap.LoadEdgeList(snap.PNGraph, "soc-Epinions1.txt", 0, 1, '\t')
eu_net = snap.LoadEdgeList(snap.PNGraph, "email-EuAll.txt", 0, 1, '\t')

epi_start_nodes = [9809, 1952]
eu_start_nodes = [189587, 675]

for node in epi_start_nodes:
    results = snap.GetSubTreeSz(epi_net, node, True, False)
    print "Node: %d, Forward BFS, Size %d, Depth %d" % (node, results[0], results[2])

    results = snap.GetSubTreeSz(epi_net, node, False, True)
    print "Node: %d, Backward BFS, Size %d, Depth %d" % (node, results[0], results[2])

for v in eu_start_nodes:
    results = snap.GetSubTreeSz(eu_net, v, True, False)
    print "Node: %d, Forward BFS, Size %d, Depth %d" % (v, results[0], results[2])

    results = snap.GetSubTreeSz(eu_net, v, False, True)
    print "Node: %d, Backward BFS, Size %d, Depth %d" % (v, results[0], results[2])

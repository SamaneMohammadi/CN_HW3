import networkx as nx
import matplotlib.pyplot as plt

#create a graph with degrees following a power law distribution

#I believe we can eliminate this loop to find s by using the call
#nx.utils.create_degree_sequence(100,powerlaw_sequence) with
#appropriate modification
while True:
    s=[]
    while len(s)<100:
        nextval = int(nx.utils.powerlaw_sequence(1, 2.5)[0]) #100 nodes, power-law exponent 2.5
        if nextval!=0:
            s.append(nextval)
    if sum(s)%2 == 0:
        break
G = nx.configuration_model(s)
G=nx.Graph(G) # remove parallel edges
self_loop = G.selfloop_edges()
print("number of self loop edge:",self_loop)
G.remove_edges_from(G.selfloop_edges())

#draw and show graph0
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
plt.show()
from networkx.generators.random_graphs import erdos_renyi_graph
import sys


node_count = int(sys.argv[1])
edge_prob = float(sys.argv[2])
g = erdos_renyi_graph(node_count, edge_prob)

with open('file.txt', 'w') as file:
    print(node_count, file=file)
    print(len(g.edges), file=file)
    for i in g.edges:
        print(*i, file=file)

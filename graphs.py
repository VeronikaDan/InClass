import networkx as nx
g = nx.Graph()
g.add_node(1)
g.add_nodes_from([1,2,3,4,5,6,7,34])
g.add_edge(1,5)
g.add_edges_from([(1,2), (3,4),(2,4), (6,4),(4,34), (1,7), (2,34)])
g.remove_node(5)
g.nodes()
g.edges()
g.neighbors(2) #какие соседи
g.degree(2) #число соседей
for node in g.nodes():
    print(node, g.degree(node))

nx.write_gexf(g, 'graph.gexf')
g1 = nx.read_gexf('graph.gexf')

import matplotlib.pyplot as plt
pos = nx.spring_layout(g)
nx.draw_networkx_nodes(g, pos, node_color = 'yellow', node_size=50)
nx.draw_networkx_edges(g, pos, edge_color = 'blue')
nx.draw_networkx_labels(g, pos, font_size = 20)
plt.axis('off')
plt.show() #plt.savefig('graph.png')
nx.diameter(g) #самый длинный путь
g.number_of_nodes()
g.number_of_edges()
nx.density(g) #примерно отношение узлов к ребрам
nx.average_clustering(g)
deg = nx.degree_centrality(g)

# goo.gl/AQllCa - датасеты разных сетей
import re

g_dolph = nx.Graph()
f = open('out.dolphins', 'r', encoding = 'utf-8')
dolphins = f.readlines()
for line in dolphins:
    nums = re.findall(r'[0-9]+', line)
    g_dolph.add_edge(int(nums[0]), int(nums[1]))

pos_dolph = nx.spring_layout(g_dolph)
nx.draw_networkx_nodes(g_dolph, pos_dolph, node_color = 'blue', node_size=100)
nx.draw_networkx_edges(g_dolph, pos_dolph, edge_color = 'yellow')
nx.draw_networkx_labels(g_dolph, pos_dolph, font_size = 20)
plt.axis('off')
plt.show()
deg_d = nx.degree_centrality(g_dolph)
print(deg_d)
max_deg = 0
center = 0
for d in deg_d.keys():
    if deg_d[d] > max_deg:
        max_deg = deg_d[d]
        center = d
print(max_deg,center)



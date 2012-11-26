import matplotlib.pyplot as plt
import networkx as nx
import grid
from edge import Edge
import const

time = 2
isTraffic = True
g = nx.Graph()
gr = grid.Grid()
nodes = []

# Add the nodes to the graph, along with labels
i = 0
while i < const.GRID_SIZE:

	j=0

	while j < const.GRID_SIZE:
		g.add_node('('+str(i)+', '+str(j)+')', pos=(i,j))
		nodes.append((i,j))
		j += 1

	i += 1

pos=nx.get_node_attributes(g,'pos')
#g.add_nodes_from(nodes)

# Assign weights to each edge and add the edges to the graph
for n in nodes:
	if (((n[0] + 1) <= const.GRID_SIZE-1)):
		g.add_edge('('+str(n[0])+', '+str(n[1])+')', '('+str(n[0]+1)+', '+str(n[1])+')', weight = gr.findAppropriateVerticalEdge(n[0], n[1], n[0]+1, n[1],time, isTraffic))
	if (((n[1] + 1) <= const.GRID_SIZE-1)):
		g.add_edge('('+str(n[0])+', '+str(n[1])+')', '('+str(n[0])+', '+str(n[1]+1)+')', weight = gr.findAppropriateVerticalEdge(n[0], n[1], n[0], n[1]+1,time, isTraffic))

# Create a dictionary for the edge weights
edge_labels=dict([((u,v,),d['weight'])
             for u,v,d in g.edges(data=True)])

nx.draw(g, pos)
#nx.draw_networkx_nodes(g, pos, nodelist =nodes, node_size=200, node_color='r', node_shape='o', alpha=1.0, cmap=None, vmin=None, vmax=None, ax=None, linewidths=None, label="Nodes")
nx.draw_networkx_edge_labels(g,pos,edge_labels=edge_labels)


#g.draw_networkx_edges(edges)
#nx.draw_networkx_nodes(g, pos=nx.spring_layout(g), nodelist =nodes, node_size=200, node_color='r', node_shape='o', alpha=1.0, cmap=None, vmin=None, vmax=None, ax=None, linewidths=None, label="Nodes")
plt.show()
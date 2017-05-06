import networkx as nx
import matplotlib.pyplot as plt
import queue
import math
import random

graph = nx.Graph()
def make_new_graph(filename):
    file = open(filename, 'w')
    for i in range(7):
        for j in range(7):
            if i is not j:
                if random.randint(1, 3) == 1:
                    file.write(str(chr(97 + i)) + ',' + str(chr(97+j)) + ',' + str(random.randint(1, 15)) + '\n')

def read_old_graph(filename):
    file = open(filename)
    for line in file:
        line = line.split(',')
        graph.add_edge(line[0], line[1], weight=int(line[2]))
#make_new_graph("test_graph")
read_old_graph("test_graph")

# Draw the graph
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True)
labels = nx.get_edge_attributes(graph,'weight')
nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels)
plt.show()
import networkx as nx
import matplotlib.pyplot as plt
import queue
import math
import random

graph = nx.Graph()

def dijkstras_traversal(g, start_node, destination_node):
    unvisited = queue.Queue()
    visited = list()
    dist_vals = {}
    fastest = {}
    unvisited.put(start_node)
    dist_vals[start_node] = 0
    while destination_node not in visited:
        current_node = unvisited.get()
        for neighbor, weight in g[current_node].items():
            if neighbor not in visited:
                weight = weight['weight']
                unvisited.put(neighbor)
                if dist_vals.get(current_node) + weight < dist_vals.get(neighbor, math.inf):
                    dist_vals[neighbor] = dist_vals.get(current_node) + weight
                    fastest[neighbor] = current_node
        visited.append(current_node)
    path = [destination_node]
    while path[0] != start_node:
        path.insert(0, fastest[path[0]])
    return path, dist_vals[destination_node]

print(dijkstras_traversal(graph, 'f', 'e'))
# Draw the graph
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True)
labels = nx.get_edge_attributes(graph,'weight')
nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels)
plt.show()
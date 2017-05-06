import networkx as nx
import matplotlib.pyplot as plt
import queue
import math
import random
import time

graph = nx.Graph()
def read_old_graph(filename):
    file = open(filename)
    for line in file:
        line = line.split(',')
        graph.add_edge(line[0], line[1], weight=int(line[2]))
read_old_graph("test_graph")

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


def find_permutations(perm_list):
    all_perms = list()
    if len(perm_list) > 2:
        for i in perm_list:
            for j in find_permutations(list_without(perm_list, i)):
                all_perms.append(list(i) + j)
    else:
        return [[perm_list[0], perm_list[1]], [perm_list[1], perm_list[0]]]
    return all_perms

def list_without(aList, value):
    ret_list = list()
    for i in aList:
        if i != value:
            ret_list.append(i)
    return ret_list


def find_best_circuit(g, start_finish_node):
    l = g.nodes()
    l.remove(start_finish_node)
    perms = find_permutations(l)
    best_path = list()
    quickest_dist = math.inf
    for path in perms:
        path = [start_finish_node] + path + [start_finish_node]
        accum_path = [start_finish_node]
        accum_dist = 0
        for i in range(len(path) - 1):
            if accum_dist < quickest_dist:
                dijsktras = dijkstras_traversal(g, path[i], path[i + 1])
                for node in dijsktras[0][1:]:
                    accum_path.append(node)
                accum_dist += dijsktras[1]
            else:
                break
        if accum_dist < quickest_dist:
            best_path = accum_path
            quickest_dist = accum_dist
    return best_path, quickest_dist

def find_best_circuits(g, start_finish_node):
    l = g.nodes()
    l.remove(start_finish_node)
    perms = find_permutations(l)
    best_paths = list()
    for path in perms:
        path = [start_finish_node] + path + [start_finish_node]
        accum_path = [start_finish_node]
        accum_dist = 0
        for i in range(len(path) - 1):
            dijsktras = dijkstras_traversal(g, path[i], path[i + 1])
            for node in dijsktras[0][1:]:
                accum_path.append(node)
            accum_dist += dijsktras[1]
        insert_index = len(best_paths)
        for i, val in enumerate(best_paths):
            if accum_dist < val[1]:
                insert_index = i
                break
        best_paths.insert(insert_index, (accum_path, accum_dist))
    return best_paths

c = time.time()
#find_best_circuits(graph, 'b')
print(time.time() - c)
for i in find_best_circuits(graph, 'b'):
    print(i)

# Draw the graph
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True)
labels = nx.get_edge_attributes(graph,'weight')
nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels)
plt.show()
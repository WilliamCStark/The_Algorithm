import networkx as nx
import matplotlib.pyplot as plt
import queue
import math
import time
graph = nx.Graph()
# Key value pairs of form; location: {activity: (category, cost, time)}
lookup_locations = {"Zakynthos" :
                        {
                            "Navagio Beach (Shipwreck Beach)": ("Beaches", 1, 40),
                            "Blue Caves": ("Caves", 1, 50),
                            "Turtle Spotting Cruise": ("Animals", 1.5, 35),
                            "Eurodivers": ("Diving", 1.5, 40),
                            "Happy Horse": ("Animals", 3, 80)
                        },
                    "Corfu":
                        {
                            "Corfu Trail": ("Hiking", 240, 10),
                            "Mount Pantokrator": ("Mountains", 2, 50),
                            "Old Fortress Corfu": ("Ancient Ruins", 1, 30),
                            "La Grotta Beach": ("Beaches", 1, 0),
                            "Spinada Square": ("Points of Interest", 1, 30)
                        },
                    "Delos":
                        {
                            "Ancient Delos Tour": ("Ancient Ruins", 5, 72),
                            "Mount Kynthos": ("Mountains", 3, 50),
                            "Small-Group Sailing Yacht": ("Sailing", 2, 100),
                            "Avenue of the Lions": ("Points of Interest", 2, 90),
                            "Temple of Isis": ("Ancient Ruins", 1.5, 90)
                        },
                    "Mykonos":
                        {
                            "Elia Beach": ("Beaches", 2, 20),
                            "Matayianni Street": ("Points of Interest", 1, 0),
                            "Mykonos Seabus": ("Sailing", 3, 60),
                            "The Windmills": ("Points of Interest", 1.5, 10),
                            "Super Paradise Beach": ("Beaches", 4, 60)
                        },
                    "Crete":
                        {
                            "Aquaworld Aquarium and Reptile Rescue Centre": ("Museums and Aquariums", 3, 55),
                            "Old Venetian Harbour": ("Beaches", 2, 20),
                            "Samaria Gorge National Park": ("Parks", 4, 60),
                            "Souda Bay War Cemetery": ("Points of Interest", 1.5, 35),
                            "Lake Cournas": ("Lakes", 2, 25)
                        },
                    "Cephalonia":
                        {
                            "Assos": ("Beaches", 3, 40),
                            "Melissani Cave": ("Caves", 2, 30),
                            "Skala Beach": ("Beaches", 2, 20),
                            "Lighthoues of Saint Theodori": ("Points of Interest", 1, 30),
                            "Boat Tour": ("Sailing", 4, 60)
                        },
                    "Koufonissi":
                        {
                            "Pori Beach": ("Beaches", 2, 20),
                            "Italida Beach": ("Beaches", 2, 20),
                            "Finikas Beach":("Beaches", 2, 20),
                            "Fanos Beach": ("Beaches", 2, 20),
                            "Sorokos Bar": ("Bars", 3, 60)
                        },
                    "Hydra":
                        {
                            "Historical Archive - Museum of Hydra": ("Museums and Aquariums", 2, 50),
                            "Saint Nicholas Beach": ("Beaches", 2, 25),
                            "Mount Eros Hydra": ("Mountains", 3, 65),
                            "Vlichos Beach": ("Beaches", 2, 30),
                            "Lazaros Koundouriotis Mansion (National Historical Museum)": ("Museums and Aquariums", 3, 90)
                        },
                    "Andros":
                        {
                            "Cyclades Olive Museum": ("Museums and Aquariums", 2, 50),
                            "Monastery of Panachratos": ("Points of Interest", 1, 40),
                            "Achla Beach": ("Beaches", 3, 30),
                            "Vitali Beach": ("Beaches", 3, 40),
                            "Museum of Contempary Art": ("Museums and Aquariums", 2, 60)
                        },
                    "Symi":
                        {
                            "Panormitis Monastery": ("Points of Interest", 2, 20),
                            "Nanou Beach": ("Beaches", 3, 20),
                            "Kali Strata": ("Ancient Ruins", 3, 50),
                            "Pedi Beach": ("Beaches", 2, 10),
                            "Nos Beach": ("Beaches", 2, 10)
                        },
                    "Skyros":
                        {
                            "Gorgonia Diving": ("Diving", 4, 110),
                            "Molos Beach": ("Beaches", 3, 20),
                            "The Faltaits Historical and Folklore Museum": ("Museums and Aquariums", 2, 80),
                            "Mouries Farm": ("Animals", 2, 40),
                            "Kores": ("Shops", 0.5, 50)
                        },
                    "Karpathos":
                        {
                            "Apella Beach": ("Beaches", 2, 20),
                            "Diakoftis Beach": ("Beaches", 2, 25),
                            "Lefkos Beach": ("Beaches", 2, 30),
                            "Amoopi Beach": ("Beaches", 2, 15),
                            "Kira Pangia Beach": ("Beaches", 2, 10)
                        }}
# Collect user input
def get_categories():
    categories = list()
    for key, val in lookup_locations.items():
        for key1, val1 in val.items():
            if val1[0] not in categories:
                categories.append(val1[0])
    return categories

def find_activities(category):
    acts = list()
    for key, dict in lookup_locations.items():
        for act, val in dict.items():
            if val[0] == category:
                acts.append(act)
    return acts

def gather_activity_input():
    chosen_activities = list()
    categories = sorted(get_categories())
    while True:
        try_again = True
        while try_again:
            try_again = False
            for i, val in enumerate(categories):
                print(str(i + 1) + ". " + val)
            print("0. Done")
            user_input = input("Select Category: ")
            user_category = ""
            if lower(user_input) in [lower(i) for i in categories]:
                for i in categories:
                    if lower(user_input) == lower(i):
                        user_category = i
            else:
                try:
                    if int(user_input) > 0:
                        user_category = categories[int(user_input) - 1]
                    elif int(user_input) == 0:
                        break
                    else:
                        print("Select a category from the list.")
                        try_again = True
                except ValueError:
                    print("Select a category from the list.")
                    try_again = True
                except IndexError:
                    print("Select a category from the list.")
                    try_again = True
        print(user_category)
        activities = sorted(find_activities(user_category))
        to_remove = list()
        removed = 0
        try_again = True
        while try_again:
            try_again = False
            for i, val in enumerate(activities):
                if val not in chosen_activities:
                    print(str(i + 1 - removed) + ". " + val)
                else:
                    to_remove.append(val)
                    removed += 1
            for i in to_remove:
                activities.remove(i)
            print("0. Done")
            print("ENTER. Return")
            user_input = input("Select Activity: ")
            user_activity = ""
            if lower(user_input) in [lower(i) for i in activities]:
                for i in activities:
                    if lower(user_input) == lower(i):
                        if i not in chosen_activities:
                            chosen_activities.append(i)
                            if len(activities) == 1:
                                categories.remove(user_category)
            else:
                try:
                    if int(user_input) > 0:
                        if activities[int(user_input) - 1] not in chosen_activities:
                            chosen_activities.append(activities[int(user_input) - 1])
                            if len(activities) == 1:
                                categories.remove(user_category)
                    elif int(user_input) == 0:
                        break
                except ValueError:
                    if user_input == "":
                        pass
                    else:
                        print("Select an activity from the list.")
                        try_again = True
                except IndexError:
                    print("Select an activity from the list.")
                    try_again = True
    return chosen_activities

def lower(string):
    return string.lower()

# Get user input
ideal_cost = 0
while True:
    try:
        ideal_cost = int(input("Enter your ideal cost: "))
        break
    except ValueError:
        print("Enter a number.")
ideal_time = 0
while True:
    try:
        user_input = input("Enter your ideal time: ").split()
        user_input[0] = int(user_input[0])
        if lower(user_input[1]) == "years" or lower(user_input[1]) == "year":
            ideal_time = user_input[0] * 365 * 24
        elif lower(user_input[1]) == "months" or lower(user_input[1]) == "month":
            ideal_time = user_input[0] * 30 * 24
        elif lower(user_input[1]) == "weeks" or lower(user_input[1]) == "week":
            ideal_time = user_input[0] * 7 * 24
        elif lower(user_input[1]) == "days" or lower(user_input[1]) == "day":
            ideal_time = user_input[0] * 24
        elif lower(user_input[1]) == "hours" or lower(user_input[1]) == "hour":
            ideal_time = user_input[0]
        elif lower(user_input[1]) == "minutes" or lower(user_input[1]) == "minute":
            ideal_time = user_input[0] / 60
        elif lower(user_input[1]) == "seconds" or lower(user_input[1]) == "second":
            ideal_time = user_input[0] / 3600
        else:
            ideal_time = user_input[0]
        break
    except ValueError:
        print("Enter a number.")
    except IndexError:
        ideal_time = user_input[0]
        break
# Test function to test user selecting activities that imply all islands
def get_all_islands():
    acts = list()
    for i in lookup_locations:
        for j in lookup_locations[i]:
            acts.append(j)
    return acts
#activities = gather_activity_input()
activities = get_all_islands()

# Generate Graph
def make_graph(g):
    for i in lookup_locations.keys():
        g.add_node(i)
    g.add_node("Home")
    edges = []
    # Weight = (Time, Money)
    # Connections between locaion nodes
    g.add_edge("Zakynthos", "Delos", time=0.5, cost=20)
    g.add_edge("Zakynthos", "Hydra", time=0.75, cost=20)
    g.add_edge("Zakynthos", "Cephalonia", time=0.5, cost=20)
    g.add_edge("Zakynthos", "Corfu", time=0.5, cost=15)
    g.add_edge("Delos", "Mykonos", time=0.25, cost=20)
    g.add_edge("Mykonos", "Koufonissi", time=0.25, cost=10)
    g.add_edge("Cephalonia", "Koufonissi", time=0.25, cost=10)
    g.add_edge("Koufonissi", "Skyros", time=0.5, cost=30)
    g.add_edge("Skyros", "Karpathos", time=1, cost=35)
    g.add_edge("Hydra", "Crete", time=0.16, cost=25)
    g.add_edge("Corfu", "Crete", time=0.16, cost=10)
    g.add_edge("Crete", "Symi", time=0.33, cost=20)
    g.add_edge("Crete", "Andros", time=0.083, cost=0)
    g.add_edge("Karpathos", "Symi", time=2, cost=120)
    g.add_edge("Home", "Zakynthos", time=20, cost=750)
# Add island edges
make_graph(graph)

# Generate Solutions
time_for_activities_per_day = 10
cost_of_accom_per_day = 100
cost_of_food_per_day = 75

def find_permutations(perm_list):
    all_perms = list()
    if len(perm_list) > 2:
        for i in perm_list:
            for j in find_permutations(list_without(perm_list, i)):
                all_perms.append([i] + j)
    elif len(perm_list) == 2:
        return [[perm_list[0], perm_list[1]], [perm_list[1], perm_list[0]]]
    else:
        return [perm_list]
    return all_perms

def list_without(aList, value):
    ret_list = list()
    for i in aList:
        if i != value:
            ret_list.append(i)
    return ret_list

def find_relevant_islands(activities):
    islands = list()
    for island, dict in lookup_locations.items():
        for activity, data in dict.items():
            if activity in activities:
                if island not in islands:
                    islands.append(island)
    return islands

# Gather a list of the first 9 or less islands
islands = sorted(find_relevant_islands(activities))
if len(islands) > 8:
    islands = islands[:8]

def dijkstras_traversal(g, start_node, destination_node, activity_cost=0, edge_value='weight'):
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
                weight = weight[edge_value]
                unvisited.put(neighbor)
                if dist_vals.get(current_node) + weight < dist_vals.get(neighbor, math.inf):
                    dist_vals[neighbor] = dist_vals.get(current_node) + weight
                    fastest[neighbor] = current_node
        visited.append(current_node)
    path = [destination_node]
    while path[0] != start_node:
        path.insert(0, fastest[path[0]])
    return path, dist_vals[destination_node] + activity_cost,

def get_island_activity_costs(island, activities, activity_info, type):
    if island == 'Home':
        return 0, list()
    type_dict = {"time:": 1, "cost": 2}
    cost = 0
    used_activities = list()
    for key, val in activity_info[island].items():
        if key in activities:
            used_activities.append(key)
            cost += val[type_dict[type]]
    for i in used_activities:
        activities.remove(i)
    return cost, activities

# Find the shortest path to traverse each permutation
def find_best_circuits(g, nodes, start_finish_node, activities, activity_info, edge_value='weight'):
    l = nodes
    if start_finish_node in nodes:
        l.remove(start_finish_node)
    perms = find_permutations(l)
    best_paths = list()
    prev_travs = {}
    t = time.time()
    for path in perms:
        path = [start_finish_node] + path + [start_finish_node]
        accum_path = [start_finish_node]
        accum_dist = 0
        for i in range(len(path) - 1):
            access_string = "-".join([path[i], path[i+1]])
            if access_string in prev_travs:
                dijsktras = prev_travs[access_string]
            else:
                dijsktras = dijkstras_traversal(g, path[i], path[i + 1], edge_value=edge_value)
                prev_travs[access_string] = dijsktras
            for node in dijsktras[0][1:]:
                accum_path.append(node)
            activity_cost, activities = get_island_activity_costs(path[i], activities, activity_info,edge_value)
            accum_dist += dijsktras[1] + activity_cost
        insert_index = len(best_paths)
        for i, val in enumerate(best_paths):
            if accum_dist < val[1]:
                insert_index = i
                break
        best_paths.insert(insert_index, (accum_path, accum_dist))
    print(time.time() - t)
    return best_paths

circuits = find_best_circuits(graph, islands, "Home", activities, lookup_locations, edge_value='cost')
print(circuits[0])


# Draw the graph
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True)
labels = nx.get_edge_attributes(graph,'weight')
nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels)
plt.show()

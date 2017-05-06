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

islands = list()
for i in lookup_locations:
    islands.append(i)

# def key_in_perms(to_perm):
#     for perm in permed[str(len(perm_list))]:
#         this_perm = list()
#         for i in perm:
#             this_perm.append(perm_list[i])
#         all_perms.append(this_perm)

def list_without(aList, value):
    ret_list = list()
    for i in aList:
        if i != value:
            ret_list.append(i)
    return ret_list

def dynamic_perms(perm_list, permed={}):
    if str(len(perm_list)) not in permed:
        permed[len(perm_list)] = []
        if len(perm_list) > 1:
            for val in reversed(perm_list):
                for j in dynamic_perms(list_without(perm_list, val), permed=permed):
                    permed[len(perm_list)].append([val] + j)
        else:
            permed[str(len(perm_list))] = [[perm_list]]
    return permed[str(len(perm_list))]

for i in dynamic_perms([0,1,2]):
    print(i)

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

def find_perms(perm_list):
    replace = {}
    for i in range(len(perm_list)):
        replace[str(i)] = perm_list[i]
    file = open(str(len(perm_list)))
    perms = list()
    for perm in file:
        perm = perm.strip()
        for key in replace:
            perm = perm.replace(key, replace[key])
        perms.append(perm.split(','))
    return perms


def gen_perms():
    to_perm = [str(i) for i in range(9)]
    for i in range(9):
        file = open(str(i+1), 'w')
        perms = find_permutations(to_perm[:i+1])
        for perm in perms:
            file.write(",".join(perm) + '\n')

# t = time.time()
# find_perms(list('abcdefgij'))
# print(time.time() - t)
# t = time.time()
# find_permutations(list('abcdefgij'))
# print(time.time() - t)
import time

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

a = list()
for i in range(5):
    a.append(str(i))
c = time.clock()
l = find_permutations(a)
print(time.clock() - c)
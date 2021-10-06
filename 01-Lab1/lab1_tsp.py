"""Traveling Salesman Problem

"""
import os
import sys
import random
import numpy as np
# set the seed
np.random.seed(42)

#uncomment when done
#file = sys.argv[1]

def read_file(filename):
    city_dict = {}
    with open(filename, 'r') as f:
        n = f.readline() # the first value of the file gives n the number of cities
        print(n)
        for line in f:
            # loop to read lins and add key:city id, value: x,y coords into dictionary. 
            values = line.split()
            city_dict[int(values[0])] = [float(i) for i in values[1:]]
    return city_dict

file = 'Term 1/Metaheuristics/01-Lab1/TSP dataset/dummy_data.tsp'
city_dict = read_file(file)

def euc_distance(x1, y1, x2, y2):
    return round(((x1-x2)**2 + (y1-y2)**2)**(1/2))

visited = [np.random.choice(list(city_dict.keys()))] # selecting a random city id
not_visited = [c_id for c_id in city_dict.keys() if c_id not in visited]
total_distance = []
print(f'initial visited list: {visited}')
print(f'initial not visited list {not_visited}')
for _ in range(len(city_dict)-1):
    distances = {}
    for city in not_visited:
        x1, y1 = city_dict[visited[-1]]
        x2, y2 = city_dict[city]
        dist = euc_distance(x1, y1, x2, y2)
        distances[city] = dist

    min_dist_id = min(distances, key=distances.get)
    print(min_dist_id)
    visited.append(min_dist_id)
    print(distances)
    
    if min_dist_id in not_visited:
        not_visited.remove(min_dist_id)
    total_distance.append(distances[min_dist_id])
    # print(f"Visited: {visited}")
    # print('\n')
    # print(f'not_visited {not_visited}')



output_file = 'output.tsp'
with open('Term 1/Metaheuristics/01-Lab1/TSP dataset/output.tsp','w+') as f:
    f.writelines(f"{np.sum(total_distance)}\n")
    f.writelines(f'{i}\n' for i in visited)




# part 2: alternative method
new_visited = [np.random.choice(list(city_dict.keys()))] # selecting a random city id
new_not_visited = [c_id for c_id in city_dict.keys() if c_id not in new_visited]
new_total_distance = []
print('\n'*3)
print(f'initial new_visited list: {new_visited}')
print(f'initial not visited list {new_not_visited}')

for _ in range(len(city_dict)-1):
    new_distances = {}
    for i in range(len(city_dict)-1):
        x1, y1 = city_dict[new_visited[-1]]
        city_id = np.random.choice(new_not_visited)
        x2, y2 = city_dict[city_id]
        dist = euc_distance(x1, y1, x2, y2)
        new_distances[city_id] = dist
        new_visited.append(city_id)
    print(new_distances)
    
    if city_id in new_not_visited:
        new_not_visited.remove(city_id)
    new_total_distance.append(new_distances[city_id])
    
    print(new_visited)
    print(new_not_visited)

print(new_distances)




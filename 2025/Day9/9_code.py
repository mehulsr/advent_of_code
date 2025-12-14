# data = open("9_example.txt", "r").read().strip().split("\n")
data = open("9_input.txt", "r").read().strip().split("\n")

import numpy as np
from shapely.geometry import Point, Polygon, box

coords = []
for line in data:
    coord = line.split(',')
    coords.append([int(coord[0]), int(coord[1])])
polygon = Polygon(coords)
coords = np.array(coords)

# Soln 1
pairwise_distances = np.abs(coords[:, np.newaxis, :] - coords[np.newaxis, :, :])
max_flat_index = np.argmax(pairwise_distances)
row_index, col_index = np.unravel_index(max_flat_index, pairwise_distances.shape)
a, b = coords[row_index], coords[col_index]
dims = 1+np.abs(a-b)
print(dims[0]*dims[1])


# Soln 2
def calculate_pairwise_metric_broadcast(vectors):
    # Reshape vectors to enable broadcasting for pairwise differences
    a_expanded = vectors[:, np.newaxis, :]  # Shape (n, 1, 2)
    b_expanded = vectors[np.newaxis, :, :]  # Shape (1, n, 2)

    # Calculate x for all pairs simultaneously
    x = 1 + np.abs(a_expanded - b_expanded)  # Shape (n, n, 2)

    # Calculate the metric for all pairs simultaneously
    metric_matrix = x[:, :, 0] * x[:, :, 1]  # Shape (n, n)
    return metric_matrix

pairwise_distances = calculate_pairwise_metric_broadcast(coords)
def valid_rectangle(point1, point2):
    x1,y1 = point1
    x2,y2 = point2

    if x1 == x2 or y1 == y2:
        return False
    minx, maxx = min(x1, x2), max(x1, x2)
    miny, maxy = min(y1, y2), max(y1, y2)    

    rect = box(minx, miny, maxx, maxy)
    if polygon.contains(rect): return True
    return False

while True:
    max_dist = np.max(pairwise_distances)
    max_flat_index = np.argmax(pairwise_distances)
    row_index, col_index = np.unravel_index(max_flat_index, pairwise_distances.shape)
    a, b = coords[row_index], coords[col_index]
    if valid_rectangle(a,b):
        print(max_dist)
        break
    else:
        pairwise_distances[row_index][col_index] = -1
        pairwise_distances[col_index][row_index] = -1
        valid_a, valid_b = False, False
print("Done")
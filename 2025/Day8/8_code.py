import math

data = open("8_input.txt", "r").read().strip().split("\n")
coords = []
for line in data:
    cleaned = line.strip().rstrip(",")
    x, y, z = cleaned.split(",")
    coords.append((int(x), int(y), int(z)))

def three_largest_after_k_custom_merges(coords):
    pairs_by_dist = []
    n = len(coords)
    for i in range(n):
        for j in range(i+1, n):
            p1, p2 = coords[i], coords[j]
            dist = math.dist(p1, p2)
            pairs_by_dist.append((dist, p1, p2))

    pairs_by_dist.sort()  # sort ascending by distance

    node_to_island_map = {}   # node -> island_id
    island_sizes = {}         # island_id -> size
    island_idx = 1            # unique island ID
    connections = 1           # counts merges / additions 

    while pairs_by_dist:
        _, pair1, pair2 = pairs_by_dist.pop(0)
        island1 = node_to_island_map.get(pair1, 0)
        island2 = node_to_island_map.get(pair2, 0)        

        if island1 == island2 == 0:
            node_to_island_map[pair1] = island_idx
            node_to_island_map[pair2] = island_idx
            island_sizes[island_idx] = 2
            island_idx += 1
            connections += 1
        elif island1 == island2:
            connections += 1
            continue
        elif island1 != 0 and island2 == 0:
            node_to_island_map[pair2] = island1
            island_sizes[island1] += 1
            connections += 1
        elif island1 == 0 and island2 != 0:
            node_to_island_map[pair1] = island2
            island_sizes[island2] += 1
            connections += 1
        elif island1 != island2:
            island_sizes[island1] += island_sizes[island2]
            for node, iid in node_to_island_map.items():
                if iid == island2:
                    node_to_island_map[node] = island1
            del island_sizes[island2]
            connections += 1

        if max(island_sizes.values()) == n:
            # print(island_sizes, pair1, pair2)
            break

    return island_sizes, pair1, pair2


island_sizes, pair1, pair2 = three_largest_after_k_custom_merges(coords)
print(island_sizes, pair1, pair2)
print(pair1[0]*pair2[0])
# print("Product:", top3[0] * top3[1] * top3[2])

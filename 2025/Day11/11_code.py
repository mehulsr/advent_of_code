# data = open("11_example.txt", "r").read().strip().split("\n")
data = open("11_input.txt", "r").read().strip().split("\n")


# Soln 1
# create adjacency matrix
adjacency_matrix = {}
for line in data:
    parts = line.split(' ')
    source, nodes = parts[0][:-1], parts[1:]
    adjacency_matrix[source] = nodes

paths = []
def backtrack(path):
    start = path[-1]

    if start == 'out':
        if path not in paths:
            paths.append(path.copy())
        return

    for node in adjacency_matrix[start]:
        path.append(node)
        backtrack(path)
        path.pop()    
    return

path = ['you']
backtrack(path)
print(paths)
print(len(paths))


# Soln 2
required = {"dac", "fft"}

memo = {}   # (node, frozenset(required_seen)) -> count

def backtrack(path, required_seen):
    start = path[-1]

    # If reached goal, check required nodes
    if start == "out":
        return 1 if required.issubset(required_seen) else 0

    # DP key for memo
    key = (start, frozenset(required_seen))
    if key in memo:
        return memo[key]

    total = 0

    for node in adjacency_matrix[start]:

        # prevent cycles: don't revisit nodes in current path
        if node in path:
            continue

        # update which required nodes we have seen
        new_required_seen = required_seen | ({node} & required)

        # extend path
        path.append(node)
        total += backtrack(path, new_required_seen)
        path.pop()

    memo[key] = total
    return total

count = backtrack(["svr"], set())
print("Number of valid paths =", count)


    

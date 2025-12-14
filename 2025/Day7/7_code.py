# data = open("7_input.txt", "r").read().strip().split("\n")
data = open("7_example.txt", "r").read().strip().split("\n")


first_line = data[0]
S = (0,0)
beam_cols = set()
width = len(first_line)
for i, c in enumerate(first_line):
    if c == 'S': 
        S = (0,i)
        beam_cols.add(i)
        break

# print(beam_cols)

# Soln 1
split_count = 0
for line in data[1:]:
    to_add = []
    to_remove = []
    for col in beam_cols:
        if line[col] == '^': 
            split_count += 1
            to_remove.append(col)
            if col > 0: to_add.append(col-1)
            if col < width-1: to_add.append(col+1)
    beam_cols -= set(to_remove)
    beam_cols.update(to_add)
    print(beam_cols)
print(split_count)


# Soln 2
rows = len(data)
cols = len(data[0])

# Find start column
for j, c in enumerate(data[0]):
    if c == 'S':
        S_col = j
        break

# DP arrays — only need previous + current row
prev = [0] * cols
curr = [0] * cols

prev[S_col] = 1   # Start position

for i in range(1, rows):
    line = data[i]
    # Reset current row
    for j in range(cols):
        curr[j] = 0

    for j in range(cols):
        if prev[j] == 0:
            continue

        # If not a '^', the beam stays in the same column
        if line[j] != '^':
            curr[j] += prev[j]
        else:
            # '^' splits left and/or right
            if j > 0:
                curr[j-1] += prev[j]
            if j < cols - 1:
                curr[j+1] += prev[j]

    # Swap rows
    prev, curr = curr, prev

# Total paths reaching the last row
print(sum(prev))

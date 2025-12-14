data = open("4_input.txt", "r").read().strip().split("\n")
# data = open("4_example.txt", "r").read().strip().split("\n")

matrix = []

for line in data:
    matrix.append(list(line))

rows = len(matrix)
cols = len(matrix[0])

def count_adjacent(row, col, matrix):
    count = 0

    if col > 0:
        count += (matrix[row][col-1] == '@')
    if col < cols-1: 
        count += (matrix[row][col+1] == '@')         

    if row > 0:
        count += (matrix[row-1][col] == '@') 
        if col > 0: 
            count += (matrix[row-1][col-1] == '@')
        if col < cols-1: 
            count += (matrix[row-1][col+1] == '@')
    if row < cols-1:
        count += (matrix[row+1][col] == '@')
        if col > 0:
            count += (matrix[row+1][col-1] == '@')
        if col < cols-1:
            count += (matrix[row+1][col+1] == '@')
    
    return count


# Soln 1
total_count = 0

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == '@' and count_adjacent(row, col, matrix) < 4:
            # print(row, col)
            total_count += 1

print(total_count)


# Soln 2
total_count = 0

while True:
    iter_count = 0
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == '@' and count_adjacent(row, col, matrix) < 4:
                # print(row, col)
                matrix[row][col] = '.'
                iter_count += 1

    if iter_count == 0:
        break

    total_count += iter_count

print(total_count)

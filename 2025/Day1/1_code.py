data = open("1_input.txt", "r").read().strip().split("\n")
# data = open("1_example.txt", "r").read().strip().split("\n")

# Puzzle 1
cur = 50
zero_counts = 0

for turn in data:
    direction, count = turn[0], int(turn[1:])

    if direction == 'R':
        cur  = (cur+count)%100
    elif direction == 'L':
        cur = (cur-count)%100
    
    if cur == 0:
        zero_counts += 1

print(zero_counts)

# Puzzle 2
r = 0
pos = 50
for turn in data: 
    f = (turn[0], int(turn[1:]))   
    r += f[1] // 100
    offset = f[1] % 100
    if offset != 0:
        if f[0] == "L":
            offset = -offset
        posn = pos + offset
        if pos != 0 and (posn <= 0 or posn >= 100):
            r += 1
        pos = posn % 100
print(r)

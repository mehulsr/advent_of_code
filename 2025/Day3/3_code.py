data = open("3_input.txt", "r").read().strip().split("\n")
# data = open("3_example.txt", "r").read().strip().split("\n")


def find_max(num: str, end_pos: int, start_pos: int = 0):
    largest = -1
    largest_idx = -1
    for i, n in enumerate(num[start_pos : end_pos+1]):
        if int(n) > largest: 
            largest = int(n)
            largest_idx = i
    return largest, largest_idx+start_pos

total = 0

# Soln 1
for line in data:
    first_digit, first_pos = find_max(line, len(line)-1, 0)
    # print(first_digit, first_pos)
    second_digit, second_pos = find_max(line, len(line), first_pos+1)
    # print(second_digit, second_pos)    
    cur = first_digit*10 + second_digit
    total += cur
    print(cur)

# Soln 2
for line in data:
    pos = -1
    cur = 0
    for i in range(11, -1, -1):
        # print(i, pos+1, len(line)-i)        
        digit, pos = find_max(line, len(line)-i-1, pos+1)
        # print(digit)
        cur += digit*(10**i)
    total += cur
    print(cur)

print(total)


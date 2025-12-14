data = open("5_input.txt", "r").read().strip().split("\n")
# data = open("5_example.txt", "r").read().strip().split("\n")

question_id = 0
fresh_ids = []

for i, line in enumerate(data):
    # print(len(line))
    if line == "":
        question_id = i
        break

    parts = line.split('-')
    start, end = int(parts[0]), int(parts[1])
    fresh_ids.append((start, end))

# Soln 1
fresh_count = 0
for line in data[question_id+1:]:
    ing = int(line)
    for id_set in fresh_ids:
        start, end = id_set[0], id_set[1]
        if ing>=start and ing<=end:
            fresh_count += 1
            break

print(fresh_count)


# Soln 2
# Sort intervals by (start, end)
fresh_ids = sorted(fresh_ids, key=lambda pair: (pair[0], pair[1]))

consolidated_list = [fresh_ids[0]]
for start, end in fresh_ids[1:]:
    prev_start, prev_end = consolidated_list[-1]
    if start > prev_end:
        consolidated_list.append((start, end))
        print((prev_start, prev_end), (start, end), "no merge")
    else:
        # Replace last interval with merged one
        merged = (prev_start, max(prev_end, end))
        consolidated_list[-1] = merged
        print((prev_start, prev_end), (start, end), "merged →", merged)

fresh_id_count = 0
for id_set in consolidated_list:
    start, end = id_set
    fresh_id_count += (end-start)+1
print(fresh_id_count)







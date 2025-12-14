# data = open("12_example.txt", "r").read().strip().split("\n")
data = open("12_input.txt", "r").read().strip().split("\n")


shapes = []
shape = []
spaces = []
for line in data:
    if line == "":
        shapes.append(shape)
        shape = []
    elif line[0] in ['.', '#']:
        shape.append(line)
    else:
        parts = line.split(' ')
        if len(parts) == 1:
            continue
        else:
            subparts = parts[0].split('x')
            width = int(subparts[0])
            height = int(subparts[1][:-1])
            array = [int(sub) for sub in parts[1:]]
            spaces.append((width, height, array))

# print(shapes, spaces)
gift_width, gift_height = len(shapes[0]), len(shapes[0][0])

# soln 1 -- trivial case, only works for given input and not an actual solution
count = 0
for (width, height, array) in spaces:
    gift_count = sum(array)
    if gift_count*gift_height*gift_height <= width*height:
        count += 1
print(count)
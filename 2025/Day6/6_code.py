data = open("6_input.txt", "r").read().strip().split("\n")
# data = open("6_example.txt", "r").read().strip().split("\n")

import numpy as np

# Soln 1
# signs
line = data[-1].split(" ")
signs = []
for sign in line:
    if sign == " " or sign == "": continue
    signs.append(sign)
print(signs)

nums = []
for line in data[:-1]:
    parts = line.split(" ")
    line_nums = []
    for num in parts:
        if num == " " or num == "": continue
        line_nums.append(int(num))
    nums.append(line_nums)

nums = np.array(nums)
# print(nums)

total = 0
sign_applied = []
col_maths = []
for col in range(len(signs)):
    sign = signs[col]
    if sign == '+':
        col_maths.append(np.sum(nums[:,col]))
    elif sign == '*':
        col_maths.append(np.prod(nums[:,col]))

print(np.sum(col_maths))


# Soln 2
width = len(data[0])
height = len(data)-1
matrix = []
nums = []
for col in range(width):
    num = ''
    for i in range(height):
        if data[i][col] == ' ': continue
        else: num += data[i][col]
    if num == "": 
        # print(nums)
        matrix.append(nums)
        nums = []
        continue
    nums.append(int(num))
matrix.append(nums)
print(matrix)


line = data[-1].split(" ")
signs = []
for sign in line:
    if sign == " " or sign == "": continue
    signs.append(sign)
print(signs)


sum_nums = []
for i in range(len(signs)):
    sign = signs[i]
    nums = matrix[i]
    if sign == '+':
        sum_nums.append(np.sum(nums))
    elif sign == '*':
        sum_nums.append(np.prod(nums)) 
print(np.sum(sum_nums))       

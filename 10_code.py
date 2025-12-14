import re
import pulp

def parse_line(line):
    # Extract joltage requirements
    target = list(map(int, re.search(r'\{([^}]+)\}', line).group(1).split(',')))
    n = len(target)

    # Extract all button groups
    raw_buttons = re.findall(r'\(([^)]*)\)', line)
    buttons = []
    for rb in raw_buttons:
        rb = rb.strip()
        if rb == "":
            inds = []
        else:
            inds = list(map(int, rb.split(',')))
        vec = [0]*n
        for i in inds:
            vec[i] += 1  # each press adds +1
        buttons.append(vec)

    return target, buttons


def solve_machine(target, buttons):
    """
    Solve A*x = target with x >= 0 integer, minimizing sum(x).
    """
    n = len(target)
    m = len(buttons)

    # Transpose: rows = counters, cols = buttons
    A = [list(col) for col in zip(*buttons)]

    problem = pulp.LpProblem("Joltage", pulp.LpMinimize)

    # Variables: x_j = presses of button j
    x = [pulp.LpVariable(f"x{j}", lowBound=0, cat="Integer") for j in range(m)]

    # Objective: minimize total presses
    problem += pulp.lpSum(x)

    # Constraints: A * x = target
    for i in range(n):
        problem += pulp.lpSum(A[i][j] * x[j] for j in range(m)) == target[i]

    # Solve
    status = problem.solve(pulp.PULP_CBC_CMD(msg=0))

    if status != 1:
        return None  # no solution

    presses = sum(int(v.value()) for v in x)
    return presses


def solve_file(filename):
    total = 0
    with open(filename) as f:
        for idx, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue

            target, buttons = parse_line(line)
            presses = solve_machine(target, buttons)

            print(f"Machine {idx}: {presses} presses")
            total += presses

    print("\nTOTAL:", total)
    return total


# Example:
solve_file("10_input.txt")

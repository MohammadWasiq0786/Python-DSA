def solve_linear(a, b):
    if a == 0:
        raise ValueError("No solution (a cannot be 0).")
    return -b / a

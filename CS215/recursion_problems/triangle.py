def print_triangle(side):
    if side == 0:
        return # Base case: do nothing.
    # Solve a simpler version of the problem.
    print_triangle(side - 1)
    # Draw the last line.
    for i in range(side):
        print("*", end="")
    print()
def print_rectangle(wid):
    leng = 10
    if wid == 0:
        return # Base case: do nothing.
    # Solve a simpler version of the problem.
    print_rectangle(wid - 1)
    # Draw the last line.
    for i in range(leng):
        print("*", end="")
    print()
def main():
    print_triangle(3)
    print()
    print_rectangle(5)
main()

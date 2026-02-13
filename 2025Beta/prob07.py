grid:list[str] = []

# read the grid
while True:
    # try catch because their is nothing to detect the bounds of the area
    try:
        line = input()
        print(line)
        if line == "":
            break
        grid.append(line)
    except EOFError:
        break

# sees if "A" exists in the grid
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == 'A':
            print(f"Get out of there! Danger at ({x}, {y})")
            break
else:
    print("You are lucky Get back to the office NOW!")
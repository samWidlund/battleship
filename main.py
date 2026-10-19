# Initial values
ROW, COL = 10, 10
grid = [[0 for _ in range(ROW)] for _ in range(COL)]
letters_pos = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H": 7, "I":8, "J":9}

def shoot(grid, x, y):
    if grid[y][x] == 1:
        grid[y][x] = 2
    elif grid[y][x] == 0:
        grid[y][x] = 3

def placeShip(grid, ship_length, x, y, orientation):
    if orientation == "horizontal":
        if x + ship_length > 10:
            return False
        for i in range(ship_length):
            grid[y][x + i] = 1

    if orientation == "vertical":
            if y + ship_length > 10:
                return False
            for i in range(ship_length):
                grid[y + i][x] = 1

    return True
    


def getIndex(x,y):
    if y in letters_pos:
        return (x, letters_pos[y])
    else:
        return("Index out of range")

def updateGrid(grid, tuple, value):
    x_value = tuple[0]
    y_value = tuple[1]
    grid[y_value][x_value] = value

    return None

updateGrid(grid,getIndex(1,"B"), 1)

# Display grid
for row in grid:
    print(row)

print(f"Placed: {placeShip(grid, 3, 7, 4, 'vertical')}")


shoot(grid, 7, 5)



print()

for row in grid:
    print(row)
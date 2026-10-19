import random as r

# Initial values
ROW, COL = 10, 10
grid = [[0 for _ in range(ROW)] for _ in range(COL)]
letters_pos = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H": 7, "I":8, "J":9}

def shoot(grid, x, y):
    pos = grid[y][x] 
    if pos == 1:
        pos = 2
    elif pos == 0:
        pos = 3

def placeShip(grid, ship_length, x, y, orientation):
    if orientation == "horizontal":
        if x + ship_length > 10:
            return False
        for i in range(ship_length):
            if grid[y][x + i] != 0:
                return False
        for i in range(ship_length):
            grid[y][x + i] = 1

    if orientation == "vertical":
        if y + ship_length > 10:
            return False
        for i in range(ship_length):
            if grid[y + i][x] != 0:
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

def displayGrid(grid):
    for row in grid:
        print(row)

def machine(grid):
    orientation = ["horizontal", "vertical"]

    x_pos = r.randint(0,9)
    y_pos = r.randint(0,9)
    ship_len = r.randint(1,4)
    ship_orientation = orientation[r.randint(0,1)]

    print(f"Placed ship: \n Pos:{x_pos},{y_pos} Size:{ship_len} Orientation:{ship_orientation}")

    return placeShip(grid, ship_len, x_pos, y_pos, ship_orientation)

counter = 1
while counter < 6:
    if machine(grid) == True:
        counter += 1

displayGrid(grid)
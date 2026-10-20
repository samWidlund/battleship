import random as r

# Initial values
ROW, COL = 10, 10
grid = [[0 for _ in range(ROW)] for _ in range(COL)]


def shoot(grid, x, y):
    pos = grid[y][x] 
    if pos == 1:
        grid[y][x] = 2
    elif pos == 0:
        grid[y][x] = 3

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

def aiRandomPlace(count):
    counter = 0
    while counter < count:
        if machine(grid) == True:
            counter += 1

def checkWin(grid):
    for row in grid:
        for x in row:
            if x == 1:
                return False
    return True

#aiRandomPlace(1)

print()

placeShip(grid, 1, 0, 0, "horizontal")

shoot(grid, 0, 0)
displayGrid(grid)

#Input format D2 = 4,1 etc
def parsePlayerInput(input_string):
    letters_pos = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H": 7, "I":8, "J":9}
    x = 0
    y = 0
    valid = True

    if input_string[0] in letters_pos:
        y = letters_pos[input_string[0]]
    else:
        valid = False


    if int(input_string[1:]) <= 10:
        x = int(input_string[1:]) - 1
    else:
        valid = False

    return (valid, x, y)


def playSingle():
    win = False
    #while win == False:


print(parsePlayerInput("A1"))
print(parsePlayerInput("B7"))
print(parsePlayerInput("J10"))
print(parsePlayerInput("X18"))

import random as r
import os

def shoot(grid, x, y): # returns true or false and updates index to show if ship is hit or not
    pos = grid[y][x] 
    if pos == 1:
        grid[y][x] = 2
        return True

    elif pos == 0:
        grid[y][x] = 3
        return False

def placeShip(grid, ship_length, x, y, orientation): # places ship in grid and returns true if position is in range    
    if orientation == 0: # horizontal
        if x + ship_length > 10:
            return False
        for i in range(ship_length):
            if grid[y][x + i] != 0:
                return False
        for i in range(ship_length):
            grid[y][x + i] = 1

    if orientation == 1: # vertical
        if y + ship_length > 10:
            return False
        for i in range(ship_length):
            if grid[y + i][x] != 0:
                return False
        for i in range(ship_length):
            grid[y + i][x] = 1
    return True

def displayGrid(grid):
    letters = "".join(chr(i) for i in range(ord("A"), ord("J") + 1))
    numbers = "  ".join(str(i) for i in range(1,11))
    index = 0

    print(f"     {numbers}")
    print("  ┏-------------------------------")

    for row in grid:
        print(f"{letters[index]} | {row}")
        index += 1
    print()

def machine(grid):
    orientation = r.randint(0, 1)

    x_pos = r.randint(0,9)
    y_pos = r.randint(0,9)
    ship_len = r.randint(2,4)

    print(f"Placed ship: \n Pos:{x_pos},{y_pos} Size:{ship_len} Orientation:{orientation}\n") # debug

    return placeShip(grid, ship_len, x_pos, y_pos, orientation)

def aiRandomPlace(grid, count): # machine places {count} amount of ships
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

def parsePlayerInput(input_string): # returns user input as bool and index tuple , input format is eg. D2 = 4,1
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

def askUser (string):
    return input(f"{string}:\n")

def playSingle(): # loops until player has won / hit every ship
    ROW, COL = 10, 10
    grid = [[0 for _ in range(ROW)] for _ in range(COL)]
    win = False

    aiRandomPlace(grid, 3)

    print("0 = no ship, 1 = ship, 2 = hit ship\n")

    while win == False:
        displayGrid(grid)

        input = askUser("Select position to shoot, eg. A2").upper()
        valid, x, y = parsePlayerInput(input)

        while valid != True:
            valid, x, y = parsePlayerInput(askUser("Index out of range, shoot again").upper())

        if shoot(grid, x, y):
            print("Hit on ship\n")
        else:
            print("Miss!\n")

        if checkWin(grid) == True:
            displayGrid(grid)
            print("Win! Every ship has been hit")
            win = True

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear') # system deprecated?

def playPair():
    ROW, COL = 10, 10
    grid1 = [[0 for _ in range(ROW)] for _ in range(COL)]
    grid2 = [[0 for _ in range(ROW)] for _ in range(COL)]

    run_game = True
    placed_ship = 0

    while placed_ship < 3:
        user1_input = askUser("Place ship").upper()
        valid, x, y = parsePlayerInput(user1_input)
        if valid:
            placeShip(grid1, 1, x, y, 1)
            placed_ship += 1
        else:
            valid, x, y = parsePlayerInput(askUser("Index out of range, shoot again").upper())
    displayGrid(grid1)

    while run_game:
        user1_shoot = askUser("Shoot")
        valid, x, y = parsePlayerInput(user1_shoot)
        shoot(grid1, x, y)

        if checkWin(grid1):
            displayGrid(grid1)
            print("Win!!!!")
            run_game = False
playPair()
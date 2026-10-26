import random as r
import os
import subprocess
import time

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

def parsePlayerPosInput(input_string): # returns user input as bool and index tuple , input format is eg. D2 = 4,1
    letters_pos = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H": 7, "I":8, "J":9}
    x = 0
    y = 0
    valid = True

    if input_string[0] in letters_pos:
        y = letters_pos[input_string[0]]
    else:
        valid = False

    try:
        if int(input_string[1:]) <= 10 and int(input_string[1:]) > 0:
            x = int(input_string[1:]) - 1
        else:
            valid = False
    except ValueError: # if {input_string} is something completely wrong like "awadsadWAaWASd"
        valid = False

    return (valid, x, y)

def askUser (string):
    return input(f"{string}:\n").upper()

def playSingle(): # loops until player has won / hit every ship
    ROW, COL = 10, 10
    grid = [[0 for _ in range(ROW)] for _ in range(COL)]
    win = False

    aiRandomPlace(grid, 3)

    print("0 = no ship, 1 = ship, 2 = hit ship\n")

    while win == False:
        displayGrid(grid)

        input = askUser("Select position to shoot, eg. A2")
        valid, x, y = parsePlayerPosInput(input)

        while valid != True:
            valid, x, y = parsePlayerPosInput(askUser("Index out of range, shoot again"))

        if shoot(grid, x, y):
            print("Hit on ship\n")
        else:
            print("Miss!\n")

        if checkWin(grid) == True:
            displayGrid(grid)
            print("Win! Every ship has been hit")
            win = True

def clearScreen():
    command = "cls" if os.name == "nt" else "clear" # runs cls if window os, otherwise clear for unix based systems
    subprocess.run(command, shell=True)

def askUserPlaceShip(grid):
    valid_length = ("1","2","3","4","5","6","7","8","9","10")
    valid_orientation = ("0","1")

    length = askUser("Enter ship length (1-10)")
    while length not in valid_length:
        length = askUser("Invalid input, enter length (1-10)")

    orientation = askUser("Enter orientation of ship, 0 = horizontal, 1 = vertical")
    while orientation not in valid_orientation:
        orientation = askUser("Invalid input, 0 = horizontal, 1 = vertical")

    valid, x, y = parsePlayerPosInput(askUser("Enter position to place ship, like A1"))
    if (valid):
        placed = placeShip(grid, int(length), x, y, int(orientation))
    while (valid != True) or (placed == False):
        valid, x, y = parsePlayerPosInput(askUser("Invalid input, enter position like A1"))
        placed =  placeShip(grid, int(length), x, y, int(orientation))

    return (int(length), int(orientation), int(x), int(y))

def usersPlaceShips(grid1, grid2, amount_ships): # does not handle wrong inputs
    count1, count2 = 0, 0

    # player 1
    while count1 < amount_ships:
        print("User1")
        displayGrid(grid1)
        askUserPlaceShip(grid1)
        displayGrid(grid1)
        count1 += 1
    time.sleep(2)
    clearScreen()

    # player 2
    while count2 < amount_ships:
        print("User2")
        displayGrid(grid2)
        askUserPlaceShip(grid2)
        displayGrid(grid2)
        count2 += 1
    time.sleep(2)
    clearScreen()

def playPair():
    ROW, COL = 10, 10
    grid1 = [[0 for _ in range(ROW)] for _ in range(COL)]
    grid2 = [[0 for _ in range(ROW)] for _ in range(COL)]

    usersPlaceShips(grid1, grid2, 1)

    while True: # improve logic / make function
        user1_shoot = askUser("User1 shoot")
        valid, x, y = parsePlayerPosInput(user1_shoot)
        if valid:
            if shoot(grid2, x, y):
                print("Hit!")
            else:
                print("Miss!")

            displayGrid(grid2)
        if checkWin(grid2):
            print("User1 wins")
            break

        user2_shoot = askUser("User2 shoot")
        valid, x, y = parsePlayerPosInput(user2_shoot)
        if valid:
            if shoot(grid1, x, y):
                print("Hit!")
            else:
                print("Miss!")
            displayGrid(grid1)

        if checkWin(grid1):
            displayGrid(grid2)
            print("User2 wins")
            break

try:
    playPair()

except KeyboardInterrupt:
    clearScreen()
    print("Process killed by keyboard")
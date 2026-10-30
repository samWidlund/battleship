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

def displayGrid(grid, user):
    letters = "".join(chr(i) for i in range(ord("A"), ord("J") + 1))
    numbers = " ".join(str(i) for i in range(1,11))
    index = 0

    print(f"\n{user} grid:")
    print()
    print(f"    {numbers}")
    print("  ┏---------------------")

    for row in grid:
        display_row = ""
        for pos in row:
            if pos == 1:
                display_row += "■ "
            elif pos == 2:
                display_row += "x "
            elif pos == 3:
                display_row += "○ "
            elif pos == 0:
                display_row += "~ "
        print(f"{letters[index]} | {display_row}")
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

    if len(input_string) < 1:
        return (False, 0, 0)
    
    if input_string[0] in letters_pos:
        y = letters_pos[input_string[0]]
    else:
        valid = False

    try:
        if int(input_string[1:]) <= 10 and int(input_string[1:]) > 0:
            x = int(input_string[1:]) - 1
        else:
            valid = False
    except ValueError: # if {input_string[1:]} is letter instead of number
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
        displayGrid(grid, "Current")

        input = askUser("Select position to shoot, eg. A2")
        valid, x, y = parsePlayerPosInput(input)

        while valid != True:
            valid, x, y = parsePlayerPosInput(askUser("Index out of range, shoot again"))

        if shoot(grid, x, y):
            print("Hit on ship\n")
        else:
            print("Miss!\n")

        if checkWin(grid) == True:
            displayGrid(grid, "Current")
            print("Win! Every ship has been hit")
            win = True

def clearScreen():
    command = "cls" if os.name == "nt" else "clear" # runs cls if window os, otherwise clear for unix based systems
    subprocess.run(command, shell=True)

def askUserPlaceShip(grid, length):
    valid_orientation = ("0","1")

    print(f"Place ship of length {length}\n")

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

def usersPlaceShips(grid1, grid2, amount_ships):
    count1, count2 = 0, 0

    ship_lengths = [4, 3, 2]

    # player 1
    while count1 < amount_ships:
        displayGrid(grid1, "Player 1")
        askUserPlaceShip(grid1, ship_lengths[count1])
        clearScreen()
        count1 += 1
    displayGrid(grid1, "Player 1")
    time.sleep(2)
    clearScreen()

    # player 2
    while count2 < amount_ships:
        displayGrid(grid2, "Player 2")
        askUserPlaceShip(grid2, ship_lengths[count2])
        clearScreen()
        count2 += 1
    displayGrid(grid2, "Player 2")
    time.sleep(2)
    clearScreen()

def userShoot(shoot_grid):
    user_input = input("Shoot: ").upper()
    valid, x, y = parsePlayerPosInput(user_input)

    while valid == False:
        user_input = input("Invalid input try again: ").upper()
        valid, x, y = parsePlayerPosInput(user_input)
    if valid:
        if shoot(shoot_grid, x, y):
            clearScreen()
            print("\nHit!")
            displayDuringGame(shoot_grid)
            return True
        else:
            clearScreen()
            print("\nMiss!")
            displayDuringGame(shoot_grid)
            return False

def displayDuringGame(grid):
    letters = "".join(chr(i) for i in range(ord("A"), ord("J") + 1))
    numbers = " ".join(str(i) for i in range(1,11))
    index = 0

    print(f"    {numbers}")
    print("  ┏---------------------")
    for row in grid:
        temp = ""
        for n in row:
            if n == 1:
                temp += "~ "
            elif n == 2:
                temp += "x "
            elif n == 3:
                temp += "○ "
            elif n == 0:
                temp += "~ "
        print(f"{letters[index]} | {temp}")
        index += 1
    print()

def displayIntro():
    print()
    print("========================================")
    print("\nBattleship game in terminal! 💣💣💣💣💣\n")
    print("========================================")
    print()
    print("Each player places 3 ships of lengths 4, 3, 2")
    print()
    print("Following icons represents:")
    print("   ■ = Ship")
    print("   ~ = Water / empty position")
    print("   x = Shot on ship")
    print("   ○ = Miss")
    print()
    print("----------------------------------------")

def playPair():
    ROW, COL = 10, 10
    grid1 = [[0 for _ in range(ROW)] for _ in range(COL)]
    grid2 = [[0 for _ in range(ROW)] for _ in range(COL)]
    win = False



    displayIntro()
    usersPlaceShips(grid1, grid2, 3)

    while not win:
        print("Player 1: ")
        print()
        displayDuringGame(grid2)

        print("Player 1 shoot")
        user1_shoot = userShoot(grid2)
        while user1_shoot:
            if checkWin(grid2):
                print("Player 1 wins!")
                win = True
                break
            else:
                print("Player 1 shoot")
                user1_shoot = userShoot(grid2)
            time.sleep(1)
            clearScreen()

            print("Player 1 shoot history: ")
            print()
            displayDuringGame(grid2)
        if win:
            break

        time.sleep(2)
        clearScreen()

        print("Player 2:")
        print()
        displayDuringGame(grid1)

        print("Player 2")
        user2_shoot = userShoot(grid1)
        while user2_shoot:
            if checkWin(grid1):
                print("Player 2 wins!")
                win = True
                break
            else:
                print("Player 2 shoot")
                user2_shoot = userShoot(grid1)
            time.sleep(1)
            clearScreen()

            print("Player 2:")
            print()
            displayDuringGame(grid1)

        if win:
            break

        time.sleep(2)
        clearScreen()

    print("\nGame is over")

try:
    playPair()

except KeyboardInterrupt:
    clearScreen()
    print("Process killed by keyboard")
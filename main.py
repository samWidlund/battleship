# Initial values
ROW, COL = 10, 10
grid = [["O" for _ in range(ROW)] for _ in range(COL)]
letters_pos = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H": 7, "I":8, "J":9}

def getIndex(x,y):
    if y in letters_pos:
        return (x, letters_pos[y])
    else:
        return("Index out of range")

def updateGrid(grid, tuple, value):
    x_value = tuple[0]
    y_value = tuple[1]
    grid[x_value][y_value] = value

    return None

updateGrid(grid,getIndex(1,"B"), "SHIP")

# Display grid
for row in grid:
    print(row)

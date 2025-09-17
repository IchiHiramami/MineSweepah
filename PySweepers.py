#MineSweepah Modules
import os, random
from copy import deepcopy

cellWidth = 3

def clearConsole():
    """
    Literally 'clear' in the terminal except its automated
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def setInitialBoard(setting: tuple):
    """
    Given a tuple with columns and rows x,y => generates gameBoard (system only) and Player Board (UI) as a list (rows) of lists (columns)
    First 2 rows are table headers meaning they will be unplayable areas. Same for the first column.
    Use alignment '.center()' for padding. 
     """
    gB, pB = [],[]
    # header for player readability
    head = ["0 |"] + [str(i+1).center(cellWidth) for i in range(setting[0])]
    div = ["-" * len(h) for h in head]
    gB.append(head)
    gB.append(div)

    # actual playable area
    for i in range(setting[1]):
        sideLabel = str(i+1).center(2) + "|"
        blanks = [" - " for _ in range(setting[0])]
        gB.append([sideLabel] + blanks)

    # player copy and system copy
    pB = deepcopy(gB)
    for row in pB:
        print(*row)
    return gB, pB, setting

def generateGameBoard(gB: list, setting: tuple):
    """
    Assign placement of bomb in Game Board (System). 
    In assignemnt, bombs are randomly assigned a tile given the difficulty setting. First two rows and first column are not included in the assignment map. 
    For every tile that is not a bomb, check all 8 adjacent tiles for bomb. Maximum is 8. This method uses a relative direction
    For table cleanup, all integers (except the frozen row and column) are converted to string and padded using .center()
    """
    # bomb assignment
    for row in gB[2:]:
        for _ in range(setting[2]):
            row[(random.randint(1, len(row)-1))] = " * "
    # 8 way bomb check
    for row in range(2, len(gB)):
        for column in range(1, len(gB[row])):
            if gB[row][column] != " * ":
                count = 0
                for dRow, dColumn in [(-1,0),(1,0),(0,-1),(0,1),(-1,1),(1,1),(-1,-1),(1,-1)]: # relative direction, where (x,y)
                    newRow, newColumn = row + dRow, column + dColumn
                    if 2 <= newRow < len(gB) and 1 <= newColumn < len(gB[newRow]):
                        if gB[newRow][newColumn] == " * ":
                            count += 1
                gB[row][column] = str(count).center(cellWidth)
    # pad integer values to 3 characters => failsafe/ all catch
    for row in range(2, len(gB)):
        for column in range(1, len(gB)-1):
            if isinstance(gB[row][column], int):
                gB[row][column] = str(gB[row][column]).center(cellWidth)

def customBoardSize():
    """
    Allows the user to input custom values for number of rows, columns, and bombs per row.
    For bomb input, assigns a random integer from 0 to user input
    Returns a tuple of (Column, Row, and Bomb) 
    """
    clearConsole()
    while True:
        try:
            y = int(input("Enter Number of Rows (MAX: 99): "))
            x = int(input("Enter Number of Columns (MAX: 99): "))
            z = int(input("Enter Number of Bombs per Row (MUST NOT BE GREATER THAN COLUMN): "))
        except (ValueError):
            print("PLEASE ENTER A DIGIT ONLY")
            continue
        if z > x:
            input("ERROR! Bombs per row cannot exceed number of columns.")
        elif x > 99 or y > 99 or x < 1 or y < 1:
            input("ERROR! Rows and columns must be between 1 and 99.")
        else:
            break
        z = random.randint(1,z)
    return x, y, z

def showBoard(pB: list):
    """
    Glorified Board Print Statement. Need I say more?
    """
    for row in pB:
        print(*row)

def moveInterpreter(gB: list, pB: list, m: tuple):
    """
    Translates user actions unto the playerboard by crossreferencing with the gameboard (system).
    ALLOWED ARGUMENTS:
    [F/U/R] [COLUMN (X)] [ROW (Y)] only
    """
    clearConsole()
    try:
        gBCoordinate = gB[m[2] + 1][m[1]]
        targetColumn = m[1]
        targetRow = m[2] + 1
    except (IndexError):
        print("ERROR! Your coordinate is not within the Game Board!")
        showBoard(pB)
        return False

    if m[0] == 'R':
        if gBCoordinate == " * ":
            pB[targetRow][targetColumn] = gBCoordinate
            showBoard(pB)
            print("GAMEOVER!")
            print("[ PREVIOUS MOVE:", m[0], m[1], m[2], "]\n")
            return True
            
        elif gBCoordinate == " 0 ":
            checked = set()
            q = []
            q.append((targetRow, targetColumn))

            while q:
                row, column = q.pop(0)
                if (row, column) in checked:
                    continue
                checked.add((row, column))

                pB[row][column] = gB[row][column]

                if gB[row][column] != " 0 ":
                    continue

                direction = [(-1,0),(1,0),(0,-1),(0,1),(-1,1),(1,1),(1,-1),(-1,-1)]
                beside = []
                for dRow, dColumn in direction:
                    r, c = row + dRow, column + dColumn
                    if 0 <= r < len(gB) and 0 <= c < len(gB[targetRow]):
                        beside.append((r,c))

                for r, c in beside:
                    if (r,c) not in checked and gB[r][c] != " * ":
                        q.append((r,c))       

        else:
            pB[targetRow][targetColumn] = gBCoordinate

        print("[ PREVIOUS MOVE:", m[0], m[1], m[2], "]\n")        
        showBoard(pB)
        return False

    elif m[0] == 'F':
        if pB[targetRow][targetColumn] == " - ":
            pB[targetRow][targetColumn] = " > "
        else:
            print("This tile is already flagged or revealed! Try another tile")
        print("[ PREVIOUS MOVE:", m[0], m[1], m[2], "]\n")
        showBoard(pB)
        return False

    elif m[0] == 'U':
        if pB[targetRow][targetColumn] == " > ":
            pB[targetRow][targetColumn] = " - "
        else:
            print("This tile has not been flagged or already revealed! Try another tile")
        print("[ PREVIOUS MOVE:", m[0], m[1], m[2], "]\n")
        showBoard(pB)
        return False
    
    elif m[0] not in ('U', 'F' ,'R'):
        print("Invalid Action Type, Only Pick Between F/U/R")
        showBoard(pB)
        print("[ PREVIOUS MOVE:", m[0], m[1], m[2], "]\n") 
        return False

def checkWin(gB , pB):
    """
    After every move, check every cell in the playerboard and compare it to the gameboard (system)
    Player wins IF AND ONLY IF the remaining blanks in the playerboard are blanks which are actually bombs in the gameboard (system)
    """
    for row in range(2, len(gB)):
        for column in range(1, len(gB[row])):
            if gB[row][column] != " * " and pB[row][column] == " - ":
                return False
    return True        
# --------------------END OF CODE---------------------
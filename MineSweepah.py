# MineSweeper in Python, for Lab5 under EEE 111
from PySweepers import setInitialBoard,customBoardSize,generateGameBoard,moveInterpreter,checkWin,clearConsole
from random import randint

clearConsole()
dS = [(5,5,randint(0,2)),(9,9,randint(0,4)),(14,14,randint(0,5))] # rows, columns, and bombs per row

while True:
    input("""\n          \n░▒▓██████████████▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░░▒▓███████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ \n░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ \n░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ \n░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░  ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░ ░▒▓███████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░ \n░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ \n░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░       \n░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓█████████████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ \nHOW TO PLAY MINESWEEPAH!:\n      1. Pick a Difficulty\n      2. Answering Methods:\n        a. F x y => Flag cell (x,y)\n        b. R x y => Reveal cell (x,y)\n        c. U x y => UnFlag cell (x,y)\n      3. If you manage to complete the board without getting the bomb, you win!\n      4. If you picked the bomb, you lose! """)

    clearConsole()
    print("""\n[1] - Easy\n[2] - Medium\n[3] - Hard\n[4] - Custom\n""")

    difficulty = input("ENTER DIFFICULTY SETTING: ").strip()

    if difficulty.isnumeric():
        if difficulty == "1":
            gameBoard, playerBoard, bombs = setInitialBoard(dS[0])
            generateGameBoard(gameBoard, dS[0])
        elif difficulty == "2":
            gameBoard, playerBoard, bombs= setInitialBoard(dS[1])
            generateGameBoard(gameBoard, dS[1])

        elif difficulty == "3":
            gameBoard, playerBoard, bombs = setInitialBoard(dS[2])
            generateGameBoard(gameBoard, dS[2])

        elif difficulty == "4":
            gameBoard, playerBoard, bombs = setInitialBoard(customBoardSize())
            generateGameBoard(gameBoard, bombs)
        else:
            print("Pick a number from 1 to 4 only")

    else:
        input("PLEASE PICK A NUMBER! [ENTER] to continue")
        continue
    
    while True:
        move = input("'F' - Flag tile 'U' - Unflag tile 'R' - Reveal tile\nENTER YOUR MOVE: ")
        if len(move.split()) == 3:
            parts = move.split()
            actionType = parts[0].upper()
            coordinate = list(map(int, parts[1:]))

            move = (actionType, coordinate[0], coordinate[1])
            l = moveInterpreter(gameBoard, playerBoard, move)
            s = checkWin(gameBoard, playerBoard)
            if l == True:
                status = "LOST"
                break
            elif s == False and l == False:
                continue    
            else:
                status = "WIN"
                break

        else:
            print("INVALID ACTION, [F/U/R] [COLUMN (X)] [ROW (Y)] only")

    if status == "LOST":
        print("YOU LOST!")
        again = input("Play again? (Y/N): ").upper().strip()
        if again != "Y":
            break
    else:
        print("YOU WIN!")
        again = input("Play again? (Y/N): ").upper().strip()
        if again != "Y":
            break
# --------------------END OF CODE---------------------
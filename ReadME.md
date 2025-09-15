
#  Minesweepah

A terminal-based Minesweeper game written in Python for EEE 111. This project features a modular design with a main game loop (`Minesweepah.py`) and a helper module (`PySweepers.py`) that encapsulates board logic, user interaction, and game mechanics.

---

##  Project Structure

| File            | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| `Minesweepah.py`| Main game loop and user interface. Handles difficulty selection and gameplay.|
| `PySweepers.py` | Helper functions for board generation, move handling, and win checking.     |

---

## 🎮 Gameplay Instructions

### 1. Launch the Game
Run `Minesweepah.py` in a Python 3 environment.

### 2. Choose Difficulty
Select from:
- `[1] Easy` → 5×5 board, 1–2 bombs per row
- `[2] Medium` → 9×9 board, 1–4 bombs per row
- `[3] Hard` → 14×14 board, 1–5 bombs per row
- `[4] Custom` → User-defined board size and bomb density

### 3. Enter Moves
Use the following commands:
- `F x y` → Flag cell at (x, y)
- `R x y` → Reveal cell at (x, y)
- `U x y` → Unflag cell at (x, y)

### 4. Win/Lose Conditions
- Reveal all safe cells to win.
- Reveal a bomb to lose.

---

## 🧠 Module Breakdown: PySweepers.py

### Board Setup

- `clearConsole()`  
  Clears the terminal screen for better readability.

- `setInitialBoard(setting: tuple)`  
  Initializes the game board and player board with headers and blank cells. Returns both boards and the setting tuple.

- `generateGameBoard(gB: list, setting: tuple)`  
  Randomly places bombs and calculates adjacent bomb counts (max 8). Pads all values for display.

- `customBoardSize()`  
  Prompts user for custom board dimensions and bomb density. Returns a tuple `(rows, columns, bombs_per_row)`.

### Gameplay Logic

- `showBoard(pB: list)`  
  Prints the current state of the player board.

- `moveInterpreter(gB: list, pB: list, m: tuple)`  
  Processes player moves:
  - Reveals cells and triggers flood-fill for zero-adjacent cells.
  - Flags and unflags cells.
  - Validates input and coordinates.

- `checkWin(gB, pB)`  
  Compares player board to game board. Returns `True` if all non-bomb cells are revealed.

---

## 🛠 Requirements

- Python 3.x
- No external libraries required beyond Python's standard library (`os`, `random`, `copy`, `queue`)

---

##  Notes

- Coordinates are entered as `x y`, where `x` is the column and `y` is the row.
- The game uses ASCII art and console prompts for interaction.
- Bomb placement is randomized per row based on difficulty.

---

##  Author

Developed by: Ichi Hiramami for EEE 111 

---
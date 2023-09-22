## Battleships

Battleships in Python is a version of the classic naval warfare game, designed to be played in the terminal.

## How to Play

To play the game, follow these steps:

1. Run the Python script in your terminal.
2. You'll see an empty board displayed with rows labeled from 'A' to 'E' and columns from '1' to '5'.
3. To make a move, enter the coordinates of the cell you want to target (e.g., 'A1', 'B2').
4. The board will be updated to reflect the outcome of your move and the computer's subsequent move.
5. The game continues until all the ships on one of the boards are destroyed.

## Features

### Existing Features:

1. **Emoji-Based Interface**:
   - The board and ships are displayed using emojis for an engaging experience.
2. **Play Against the Computer**:
   - The computer's moves are randomly generated.
3. **Accepts User Input**:
   - Players input coordinates to take their turn.

### Future Features:

- Allow the player to select the board size and the number of ships.
- Implement different ship sizes and types.
- Add multiplayer functionality.

## Data Model

The Battleship game is modeled using two-dimensional lists to represent the game boards for both the player and the computer. Each board is a matrix where each cell represents a specific state in the game:

- **Boards**: The player's board and the computer's board are both represented as 2D lists. Each board's size is defined by a constant, but for the current version, we use a 5x5 grid.

- **Symbols**:

  - **WATER (`WATER`)**: Represents an untouched segment of the ocean, i.e., where no move has been made.
  - **MISS (`MISS`)**: Indicates a segment of the ocean where a move was made, but no ship was present.
  - **HIT (`HIT`)**: Denotes a successful move where a ship segment was targeted and hit.
  - **SHIP (`SHIP`)**: Represents a segment of a ship. In the computer's board displayed to the player, these are hidden and appear as `WATER` to maintain the game's mystery.

- **Moves**: Player and computer moves are tracked by modifying the respective 2D lists. A move is represented by changing the state of a cell on the board. For example, if the player targets a cell and hits a ship, that cell's value changes from `SHIP` to `HIT`.

- **Game State**: The entirety of the game's state is stored in these 2D lists. By examining them, one can determine the positions of the ships, the moves made by both the player and the computer, and deduce which ships have been sunk or remain.

## Technical Breakdown

### `input_to_coordinates` function:

This function converts a user's textual input, like 'A1', into row and column indices for the game board.

- It uses the `ord()` function to convert the letter ('A' to 'E') into an ASCII value. By subtracting the ASCII value of 'A', we derive the row index. For instance, 'A' becomes 0, 'B' becomes 1, etc.
- The numeric part of the input indicates the column, but as our board starts at index 0, we subtract 1.

More about the `ord()` function can be found [A quick tutorial on Python’s ord() function with examples](https://betterprogramming.pub/understanding-pythons-ord-function-7fd9518ed457)

### Main Game Loop - `main()`

This function serves as the game's main entry point, where the foundational setup occurs before the actual gameplay starts.

### Script Execution Condition - `if __name__ == "__main__":`

This common Python idiom ensures that the main game loop (`main()`) only runs if the script is executed directly.

**Explanation:**

When a Python script is executed, a built-in variable named `__name__` is automatically defined. If the script is the main program being run (not imported as a module into another script), `__name__` takes the value `"__main__"`. This condition ensures the game starts only if executed directly, and not if imported elsewhere.

By structuring it this way, the game is set up to initialize and be ready for additional gameplay functionalities.

## Testing

### Bugs

1. **Solved Bugs**:

   - ...

2. **Remaining Bugs**:
   - ...

### Validator Testing

...

## Deployment

...

**Steps for deployment:**

- Clone this repository to your local machine.
- ...

---

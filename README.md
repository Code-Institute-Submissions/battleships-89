# Battleships in Python

Battleships in Python is a rendition of the classic naval combat game, optimized for terminal play.

## How to Play

1. Execute the Python script within your terminal.
2. An initial game board is presented, with rows labeled 'A' to 'E' and columns from '1' to '5'.
3. Input the coordinates of your targeted cell (e.g., 'A1', 'B2').
4. The boards will update, displaying the results of both your move and the computer's counter-move.
5. Victory is achieved when all ships on a board are sunk.

## Features

### Existing Features:

1. **Emoji-Based Interface**: Utilize emojis for an immersive visual representation.
2. **Play Against the Computer**: Computer moves are randomized.
3. **Accepts User Input**: Players provide coordinates to dictate their turn.
4. **Dynamic Feedback**: Real-time board updates after each turn.

### Future Features:

- Board and ship count customization.
- Introduction of varied ship dimensions and classifications.
- Integration of multiplayer capabilities.

## Data Model

Battleship's game state is built upon two-dimensional arrays, simulating game boards for both participants:

- **Boards**: Both boards (player's and computer's) are 2D arrays, currently sized at 5x5.
- **Symbols**:

  - **WATER (`WATER`)**: 🟦 - Denotes an untargeted ocean segment.
  - **MISS (`MISS`)**: ❌ - Marks an ocean segment with an unsuccessful hit attempt.
  - **HIT (`HIT`)**: 💥 - Signals a successful hit on a ship segment.
  - **SHIP (`SHIP`)**: 🚢 - Indicates a ship segment. On the computer's board, these are shown as `WATER` when not targeted.

- **Moves**: Every move modifies the respective board. A cell's state change (e.g., from `SHIP` to `HIT`) represents the move's outcome.

- **Game State**: All game data, including ship positions, moves, and progression, is housed within these arrays.

## Technical Breakdown

### Utility Functions

- `initialize_board(size)`: Set up a new game board of a specified size.
- `place_ships(board, num_ships)`: Deploys ships on the board at random positions, ensuring no overlapping ships.
- `input_to_coordinates`: Translates user input, such as 'A1', into actionable game board indices.
- `make_move(board, row, col)`: Logs player and computer moves on the board, updating cell states, and returns the outcome of the move.
- `display_boards(player_board, computer_board)`: Displays the current state of both player's and computer's boards.
- `count_hits(board)`: Counts the number of HIT emojis on the given board.

### Game Control

- **Main Game Loop (`main()`)**: Orchestrates game setup and looped play until a victor emerges.

- **Script Trigger (`if __name__ == "__main__":`)**: Ensures the game starts only when this script is the primary execution point.

Reference on `ord()` function: [Understanding Python’s ord() function with examples](https://betterprogramming.pub/understanding-pythons-ord-function-7fd9518ed457).

## Testing

### Bugs

1. **Solved Bugs**:

   - **Double Ship Placement**: Fixed an issue where ships could be placed on top of each other on the game board, causing an inaccurate count of ships.

2. **Remaining Bugs**:
   - ...

### Validator Testing

## Deployment

**Steps for deployment:**

- Clone this repository to your local machine.
- ...

---

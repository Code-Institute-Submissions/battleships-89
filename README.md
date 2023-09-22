# Battleships in Python

Battleships in Python is a rendition of the classic naval combat game, now optimized for terminal play.

## How to Play

1. Execute the Python script within your terminal.
2. An initial game board is presented, with rows labeled 'A' to 'E' and columns from '1' to '5'.
3. Input the coordinates of your targeted cell (e.g., 'A1', 'B2').
4. The boards will update, showing the results of both your move and the computer's counter-move.
5. Victory is achieved when all the ships on a board are sunk.

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

  - **WATER (`WATER`)**: Denotes an untargeted ocean segment.
  - **MISS (`MISS`)**: Marks an ocean segment with an unsuccessful hit attempt.
  - **HIT (`HIT`)**: Signals a successful hit on a ship segment.
  - **SHIP (`SHIP`)**: Indicates a ship segment. On the computer's board, these are clandestinely shown as `WATER`.

- **Moves**: Every move modifies the respective board. A cell's state alteration (e.g., from `SHIP` to `HIT`) represents the move's outcome.

- **Game State**: All game data, including ship positions, moves, and overall progression, is housed within these arrays.

## Technical Breakdown

### Utility Functions

- `input_to_coordinates`: Translates user input, such as 'A1', into actionable game board indices.
- `place_ships`: Deploys ships on the board at random positions without overlap.
- `make_move`: Logs player and computer moves, updating the board accordingly.

### Game Control

- **Main Game Loop (`main()`)**: Orchestrates game setup and looped play until conclusion.

- **Script Trigger (`if __name__ == "__main__":`)**: Ensures the game is initiated only when this script is the primary execution point.

Reference on `ord()` function: [Understanding Python’s ord() function with examples](https://betterprogramming.pub/understanding-pythons-ord-function-7fd9518ed457).

## Testing

### Bugs

1. **Solved Bugs**:

   - ...

2. **Remaining Bugs**:
   - ...

### Validator Testing

## Deployment

**Steps for deployment:**

- Clone this repository to your local machine.
- ...

---

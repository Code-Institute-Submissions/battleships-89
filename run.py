import random

# Emoji constants
WATER = "\U0001F7E6"  # Blue Square for water
MISS = "\U0000274C"  # Red X for miss
HIT = "\U0001F4A5"  # Explosion for hit
SHIP = "\U0001F6A2"  # Ship for ship (this will not be shown on the computer board)

# Initialize board
def initialize_board(size):
    return [[WATER for col in range(size)] for row in range(size)]

# Place random ships
def place_ships(board, num_ships):
    """
    Randomly place a specified number of ships on the provided game board.
    Args:
    - board (list of list): 2D list representing the game board.
    - num_ships (int): Number of ships to be placed on the board.
    Note: fix potential overlap!
    """
    for i in range(num_ships):
        row, col = random.randint(0, len(board) - 1), random.randint(0, len(board) - 1)
        board[row][col] = SHIP

# Convert user input to coordinates
def input_to_coordinates(move):
    """
    Convert the user's textual input into corresponding row and column indices on the game board.
    Args: move (str): The user's input in the format of a letter followed by a number (e.g., 'A1', 'B3').
    Returns tuple: A tuple containing the row and column indices corresponding to the user's input.
    Note: input validation!
    """
    row = ord(move[0].upper()) - ord('A')
    col = int(move[1]) - 1
    return row, col

# Make a move
def make_move(board, row, col):
    """
    Records a move on the provided board at the given row and column.
    Args:
    - board (list of lists): The 2D game board where the move will be recorded.
    - row (int): The zero-based row index where the move will be made.
    - col (int): The zero-based column index where the move will be made.
    Returns bool: True if the move results in a hit, False if it's a miss.
    """
    if board[row][col] == SHIP:
        board[row][col] = HIT
        return True  # Hit
    else:
        board[row][col] = MISS
        return False  # Miss

# Main game loop
def main():
    size = 5
    player_board = initialize_board(size)
    computer_board = initialize_board(size)

if __name__ == "__main__":
    main()

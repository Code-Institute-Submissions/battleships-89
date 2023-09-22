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
    placed = 0
    while placed < num_ships:
        row, col = random.randint(0, len(board) - 1), random.randint(0, len(board) - 1)
        if board[row][col] != SHIP:  # Ensure the cell isn't already occupied by a ship
            board[row][col] = SHIP
            placed += 1

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
    Returns str: "hit" if the move results in a hit, "miss" if it's a miss, "already targeted" if cell was already hit/miss.
    """
    if board[row][col] == MISS or board[row][col] == HIT:
        return "already targeted"
    elif board[row][col] == SHIP:
        board[row][col] = HIT
        return "hit"
    else:
        board[row][col] = MISS
        return "miss"

def display_boards(player_board, computer_board):
    # Display computer's board without showing ships
    print("\nComputer's Board:")
        # Display rows with row labels (A, B, C, etc.)
    for idx, row in enumerate(computer_board):
        label = chr(idx + ord('A'))
        print(f"{label} |", " ".join([cell if cell != SHIP else WATER for cell in row]))

    # Display column headings between the two boards
    print("  ".join(['   '] + ['1', '2', '3', '4', '5']))  # Adjust if you change the board size
    # Display player's board with all information visible and with row labels
    for idx, row in enumerate(player_board):
        label = chr(idx + ord('A'))
        print(f"{label} |", " ".join(row))

def count_hits(board):
    """
    Counts the number of HIT emojis on the given board.
    Args:
    - board (list of lists): The 2D game board.
    Returns int: The number of hits on the board.
    """
    return sum(row.count(HIT) for row in board)

# Main game loop
def main():
    size = 5
    num_ships = 5

    player_board = initialize_board(size)
    computer_board = initialize_board(size)

    place_ships(player_board, num_ships)
    place_ships(computer_board, num_ships)

    while True:
        display_boards(player_board, computer_board)

        valid_input = False
        while not valid_input:
            move = input("Enter your move (e.g., 'A1'), 'x' to exit: ")
            
            if move.lower() == 'x':
                print("Thanks for playing! Exiting the game.")
                return  # Exit the game
            if len(move) == 2 and move[0].upper() in 'ABCDE' and move[1] in '12345':
                row, col = input_to_coordinates(move)
                result = make_move(computer_board, row, col)
                if result == "already targeted":
                    print("You've already targeted this cell. Choose another.")
                elif result == "hit":
                    print("You hit the ship! 💥")
                    valid_input = True
                elif result == "miss":
                    print("Miss! ❌")
                    valid_input = True

        # Computer's turn
        comp_row, comp_col = random.randint(0, size - 1), random.randint(0, size - 1)
        comp_result = make_move(player_board, comp_row, comp_col)
        while comp_result == "already targeted":
            comp_row, comp_col = random.randint(0, size - 1), random.randint(0, size - 1)
            comp_result = make_move(player_board, comp_row, comp_col)
        
        if comp_result == "hit":
            print("Computer hit your ship!")
        elif comp_result == "miss":
            print("Computer missed!")
        
        # Check for end game conditions
        if count_hits(computer_board) == num_ships:
            print("Congratulations! You sunk all the computer's ships!")
            break
        elif count_hits(player_board) == num_ships:
            print("All your ships have been sunk! Game Over!")
            break



if __name__ == "__main__":
    main()

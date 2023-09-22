import random


# Emoji constants
WATER = "\U0001F7E6"  # Blue Square for water
MISS = "\U0000274C"  # Red X for miss.
HIT = "\U0001F4A5"  # Explosion for hit
SHIP = "\U0001F6A2"  # Ship for ship


def initialize_board(size):
    return [[WATER for col in range(size)] for row in range(size)]


def place_ships(board, num_ships):
    placed = 0
    attempts = 0
    while placed < num_ships:
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board) - 1)
        if board[row][col] != SHIP:
            board[row][col] = SHIP
            placed += 1
        attempts += 1
        if attempts > 1000:
            raise ValueError("Too many attempts to place ships."
                             " Possibly too many ships for the board size.")


def input_to_coordinates(move):
    row = ord(move[0].upper()) - ord('A')
    col = int(move[1]) - 1
    return row, col


def make_move(board, row, col):
    if board[row][col] == MISS or board[row][col] == HIT:
        return "already targeted"
    elif board[row][col] == SHIP:
        board[row][col] = HIT
        return "hit"
    else:
        board[row][col] = MISS
        return "miss"


def convert_cell(cell):
    return cell if cell != SHIP else WATER


def display_boards(player_board, computer_board):
    print("\nComputer's Board:")
    for idx, row in enumerate(computer_board):
        label = chr(idx + ord('A'))
        row_content = " ".join([convert_cell(cell) for cell in row])
        print(f"{label} |", row_content)

    column_headers = ['   ', '1', '2', '3', ' 4', '5']
    print("  ".join(column_headers))

    for idx, row in enumerate(player_board):
        label = chr(idx + ord('A'))
        print(f"{label} |", " ".join(row))


def count_hits(board):
    return sum(row.count(HIT) for row in board)


def get_valid_move():
    while True:
        move = input("Enter your move (e.g., 'A1'), 'x' to exit:\n")
        if move.lower() == 'x':
            print("Thanks for playing! Exiting the game.")
            exit()
        valid_row = len(move) == 2 and move[0].upper() in 'ABCDE'
        valid_col = move[1] in '12345'
        if valid_row and valid_col:
            return move.upper()
        else:
            print("Invalid input. Use the format 'A1'")


def computer_turn(player_board, size):
    comp_row = random.randint(0, size - 1)
    comp_col = random.randint(0, size - 1)
    comp_result = make_move(player_board, comp_row, comp_col)

    while comp_result == "already targeted":
        comp_row = random.randint(0, size - 1)
        comp_col = random.randint(0, size - 1)
        comp_result = make_move(player_board, comp_row, comp_col)

    return comp_result


def main():
    size = 5
    num_ships = 5

    player_board = initialize_board(size)
    computer_board = initialize_board(size)

    place_ships(player_board, num_ships)
    place_ships(computer_board, num_ships)

    while True:
        display_boards(player_board, computer_board)
        move = get_valid_move()
        row, col = input_to_coordinates(move)
        result = make_move(computer_board, row, col)

        while result == "already targeted":
            print("You've already targeted this cell. Choose another.")
            move = get_valid_move()
            row, col = input_to_coordinates(move)
            result = make_move(computer_board, row, col)

        if result == "hit":
            print("You hit the ship! 💥")
        elif result == "miss":
            print("Miss! ❌")

        comp_result = computer_turn(player_board, size)
        if comp_result == "hit":
            print("Computer hit your ship!")
        elif comp_result == "miss":
            print("Computer missed!")

        if count_hits(computer_board) == num_ships:
            print("Congratulations! You sunk all the computer's ships!")
            break
        elif count_hits(player_board) == num_ships:
            print("All your ships have been sunk! Game Over!")
            break


if __name__ == "__main__":
    main()
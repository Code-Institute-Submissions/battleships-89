# Emoji constants
WATER = "\U0001F7E6"  # Blue Square for water
MISS = "\U0000274C"  # Red X for miss
HIT = "\U0001F4A5"  # Explosion for hit
SHIP = "\U0001F6A2"  # Ship for ship (this will not be shown on the computer board)

# Initialize board
def initialize_board(size):
    return [[WATER for col in range(size)] for row in range(size)]

# Main game loop
def main():
    size = 5
    player_board = initialize_board(size)
    computer_board = initialize_board(size)

if __name__ == "__main__":
    main()

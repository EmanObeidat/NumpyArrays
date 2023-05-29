class ChessBoard:
    def __init__(self):
        self.grid = [[(0, 0, 0) for _ in range(8)] for _ in range(8)]

    def add_red(self, row, col):
        self.grid[row][col] = (1, 0.2, 0)

    def add_blue(self, row, col):
        self.grid[row][col] = (0, 1, 1)

    def render(self):
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    cell_color = (1, 1, 1)  # white
                else:
                    cell_color = (0, 0, 0)  # black

                if self.grid[row][col] != (0, 0, 0) and self.grid[row][col] != (1, 1, 1):
                    cell_color = self.grid[row][col]

                print('\033[48;2;{};{};{}m'.format(
                    int(cell_color[0] * 255),
                    int(cell_color[1] * 255),
                    int(cell_color[2] * 255)),
                      end='  \033[0m')  # Reset color after cell

            print()

    def is_under_attack(self):
        red_position = None
        blue_positions = []

        for row in range(8):
            for col in range(8):
                if self.grid[row][col] == (1, 0.2, 0):
                    red_position = (row, col)
                elif self.grid[row][col] == (0, 1, 1):
                    blue_positions.append((row, col))

        if red_position is None:
            return False

        for blue_position in blue_positions:
            if red_position[0] == blue_position[0] or red_position[1] == blue_position[1]:
                return True

            if abs(red_position[0] - blue_position[0]) == abs(red_position[1] - blue_position[1]):
                return True

        return False


# Testing the ChessBoard class
chess_board = ChessBoard()

# Adding red and blue pieces
chess_board.add_red(2, 3)
chess_board.add_blue(4, 5)

# Rendering the chess board
print("Chess Board:")
chess_board.render()

# Checking if red is under attack
if chess_board.is_under_attack():
    print("Red is under attack!")
else:
    print("Red is not under attack!")

import numpy as np
import time

# Puzzle Requirements:
#   Given N
#   Create an N*N ndarray
#   Place N queens on the board in such a way that they don't attack each other (rows, columns, diagonals)

def initialize_matrix(n):
    chess_board = np.zeros(shape=(n, n), dtype=np.str)
    return chess_board

def populate_matrix_null_values(chess_board, n):
    for y in range(n):
        for x in range(n):
            chess_board[y][x] = '_'

    # Changes to starting configuration can be made here for testing
    # chess_board[0][1] = 'Q'
    # print(chess_board)
    return chess_board


def logic_loop(chess_board, n):
    # Base case to see if we have solved the puzzle and placed N Queens on the board
    # This will help us escape recursion later...
    if np.count_nonzero(chess_board == 'Q') != n:
        # Begin scanning the array
        for y in range(n):
            for x in range(n):
                # For each position, check if a queen here would be under attack
                if no_attacking_queens(chess_board, y, x, n):
                    # If a queen can be safely placed, do so, then recur
                    place_queen(chess_board, y, x)
                    logic_loop(chess_board, n)
                    # After every break in recursion, check to see if we have solved the puzzle
                    if np.count_nonzero(chess_board == 'Q') != n:
                        # If the puzzle is not solved, erase the latest queen to continue iterating
                        chess_board[y][x] = '_'
    # Once the base case is satisfied, return the completed puzzle
    return chess_board


def is_queen(chess_board, y, x):
    if chess_board[y][x] == 'Q':
        return True
    else:
        return False


def place_queen(chess_board, y, x):
    chess_board[y][x] = 'Q'
    return chess_board


def no_attacking_queens(chess_board, y, x, n):

    # Set a default bool, if it returns True, there are no attacking queens against the given position
    return_value = True

    # ROW CHECK
    #   This is the easiest to solve as we can just parse the list at array index entry y
    if 'Q' in chess_board[y]:
        return_value = False

    # COLUMN CHECK
    #   Given X, check "down the column" using range n to insert y index values
    for dy in range(n):
        if chess_board[dy][x] == 'Q':
            return_value = False

    # DIAG CHECK - up, right
    #   For Diag Checks, IndexErrors indicate an out of bounds array position, which we pass over
    #   Current implementation checks the full possible range
    for dxy in range(1, n + 1):
        check_y = y - dxy
        check_x = x + dxy
        if check_y >= 0 and check_x >= 0:
            try:
                if chess_board[check_y][check_x] == 'Q':
                    return_value = False
            except IndexError:
                pass

    # DIAG CHECK - down, left
    for dxy in range(1, n + 1):
        check_y = y + dxy
        check_x = x - dxy
        if check_y >= 0 and check_x >= 0:
            try:
                if chess_board[check_y][check_x] == 'Q':
                    return_value = False
            except IndexError:
                pass

    # DIAG CHECK - up, left
    for dxy in range(1, n + 1):
        check_y = y - dxy
        check_x = x - dxy
        if check_y >= 0 and check_x >= 0:
            try:
                if chess_board[check_y][check_x] == 'Q':
                    return_value = False
            except IndexError:
                pass

    # DIAG CHECK - down, right
    for dxy in range(1, n + 1):
        check_y = y + dxy
        check_x = x + dxy
        if check_y >= 0 and check_x >= 0:
            try:
                if chess_board[check_y][check_x] == 'Q':
                    return_value = False
            except IndexError:
                pass

    # Returns true having found no attacking queens for the given position
    return return_value


def print_chessboard(chess_board):
    print(chess_board)
    print('Puzzle Solved')


if __name__ == '__main__':
    # Set N value to solve puzzles of different sizes
    n = 8

    t0 = time.time()

    chess_board = initialize_matrix(n)
    chess_board = populate_matrix_null_values(chess_board, n)
    chess_board = logic_loop(chess_board, n)
    print_chessboard(chess_board)
    t1 = time.time()
    print(f'completed in {t1 - t0}s')



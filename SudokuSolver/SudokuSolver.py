import numpy
import time


def getpuzzle():

    sudoku = numpy.array([
        [0, 3, 0, 0, 7, 0, 4, 0, 0],
        [4, 0, 0, 9, 8, 0, 0, 3, 0],
        [8, 0, 9, 0, 0, 0, 2, 0, 7],
        [9, 0, 3, 0, 4, 0, 0, 5, 6],
        [1, 0, 7, 0, 0, 0, 3, 0, 2],
        [2, 4, 0, 0, 1, 0, 9, 0, 8],
        [3, 0, 1, 0, 0, 0, 7, 0, 5],
        [0, 9, 0, 0, 6, 1, 0, 0, 3],
        [0, 0, 8, 0, 5, 0, 0, 1, 0],
    ])

    sudoku_hard = numpy.array([
        [0, 0, 0, 0, 0, 0, 6, 0, 4],
        [8, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 5, 4, 9, 0, 0],
        [9, 2, 0, 1, 0, 0, 5, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 6, 0, 0, 2, 0, 1, 9],
        [0, 0, 3, 4, 8, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 2, 6],
        [7, 0, 9, 0, 0, 0, 0, 0, 0],
    ])

    sudoku_swedish = numpy.array([
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0],
    ])



    # Insert desired test case puzzle as the argument
    # Example: matrix = numpy.asmatrix(TEST_CASE)
    matrix = numpy.asmatrix(sudoku_swedish)

    return matrix

def ispossible_long(matrix, new_value, y, x):

    #check row for duplicate
    #check column for duplicate
    #check 3x3 for duplicate

    is_possible_bool = False

    #check across rows for duplicates
    for foo in range(9):
        if matrix[y, foo] == new_value:
            #print('duplicate in x - row')
            return is_possible_bool #breaks out if it finds a duplicate in the row, declares is_possible as false


    #check down columns for duplicates
    for foo in range(9):
        if matrix[foo, x] == new_value:
            # print('duplicate in y - column')
            return is_possible_bool #breaks out if it finds a duplicate in the column, declares is_possible as false


    #check 3x3 grids - here's where things get a bit messy

    # Begin by taking the y, x coordinates of the cell we are solving for
    # Step through three ranges of 3 at a time to find which third of the puzzle y is found in
    # This step will not repeat once it has found its answer thanks to y_found == False
    # Then do the same for x of the cell we are solving for
    # once we have the known "ninth" then we scan that 3x3 grid for duplicates

    start_y = 0
    start_x = 0
    y_found = False
    x_found = False

    for end_y in [3, 6, 9]:
        if y in range(start_y, end_y) and y_found == False:
            y_found = True
            # if we progress here, y is in range
            for end_x in [3, 6, 9]:
                if x in range(start_x, end_x) and x_found == False:
                   # if we progress, x is in range
                    x_found = True
                    for scan_ninth_y in range(start_y, end_y):
                        for scan_ninth_x in range(start_x, end_x):
                            if matrix[scan_ninth_y, scan_ninth_x] == new_value:
                                # If we arrive here, we have found a duplicate, and we return FALSE for is_possible_bool
                                return is_possible_bool
                else:
                    # else increment x by 3 to check the next ninth
                    start_x += 3
        else:
            # else increment y by 3 to check the next ninth
            start_y += 3

    # if no duplicates are found, we return TRUE and then in the parent loop set the 0 to new_value
    is_possible_bool = True
    return is_possible_bool


def base_case(matrix):
    finish_flag = True
    for y in range(9):
        for x in range(9):
            if matrix[y, x] == 0:
                finish_flag = False
    return finish_flag


def solve(matrix, start_time):
    global attempts
    attempts += 1
    global flag

    # This loop searches for and finds the next 0 in sequence in the array
    # Then it finds a new 1-9 value that meets the 'ispossible' rule conditions
    # Script continues to loop with the recursive function until it finds NO ZERO in the range
    # Script escapes with base-case global "flag"

    if flag == False:
        for y in range(9):
            for x in range(9):
                if matrix[y, x] == 0:

                    for new_value in range(1, 10):

                        is_possible_bool = ispossible_long(matrix, new_value, y, x)
                        if is_possible_bool == True:

                            matrix[y, x] = new_value
                            solve(matrix, start_time)
                            if flag == False:
                                matrix[y, x] = 0
                    return
    print(matrix)
    print(f'finished in {attempts} attempts')
    print(f'time: {round((time.time() - start_time), 2)}s')

    flag = True


def main():

    start_time = time.time()
    matrix = getpuzzle()
    solve(matrix, start_time)


if __name__ == '__main__':
    flag = False
    attempts = 0
    main()


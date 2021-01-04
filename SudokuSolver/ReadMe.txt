This Sudoku Solver uses backtracking to brute force a solution to any solvable sudoku puzzle.
Three test cases are included, a simple, medium, and hard (rated: Swedish for the Swedish Mathematician who came up with it)
To track the base case and the number of iterations, I use a global variable - I am not happy with this solution, but it worked for my purpose.

Time complexity based on brute force backtracking (depth first search) is O(9^m) where m is the number of blanks in a given puzzle.
No attempts to optimize for time complexity.

Example solution:

[[8 1 2 7 5 3 6 4 9]
 [9 4 3 6 8 2 1 7 5]
 [6 7 5 4 9 1 2 8 3]
 [1 5 4 2 3 7 8 9 6]
 [3 6 9 8 4 5 7 2 1]
 [2 8 7 1 6 9 5 3 4]
 [5 2 1 9 7 4 3 6 8]
 [4 3 8 5 2 6 9 1 7]
 [7 9 6 3 1 8 4 5 2]]
finished in 49559 attempts
7.47s



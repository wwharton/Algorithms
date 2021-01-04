Solves the NQueens puzzle with backtracking.
Given a chess board of size N*N, place N queens on the board such that none are attacking each other.
The biggest challenge was searching for pieces attacking diagonally.
Solution involves a try/except condition to avoid out of bound index errors,
    as I perform full depth searches for attacking pieces at every location.
My brute force, backtracking solution is awfully time inefficient, achieving worst case scenario O(N**)


Example Solution for n of 4:

[['_' 'Q' '_' '_']
 ['_' '_' '_' 'Q']
 ['Q' '_' '_' '_']
 ['_' '_' 'Q' '_']]
Puzzle Solved
completed in 0.007006645202636719s

n of 8:

[['Q' '_' '_' '_' '_' '_' '_' '_']
 ['_' '_' '_' '_' 'Q' '_' '_' '_']
 ['_' '_' '_' '_' '_' '_' '_' 'Q']
 ['_' '_' '_' '_' '_' 'Q' '_' '_']
 ['_' '_' 'Q' '_' '_' '_' '_' '_']
 ['_' '_' '_' '_' '_' '_' 'Q' '_']
 ['_' 'Q' '_' '_' '_' '_' '_' '_']
 ['_' '_' '_' 'Q' '_' '_' '_' '_']]
Puzzle Solved
completed in 57.57128691673279s

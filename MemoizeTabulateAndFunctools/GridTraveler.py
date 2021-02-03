from functools import lru_cache
import numpy as np

"""
How many ways can a "person" travel from 0,0 to m, n in a grid, using only down and right moves?

    m = 4, n = 4 (s is Start, F is Finish)
         0
       0[S, 0, 0, 0]
        [0, 0, 0, 0]
        [0, 0, 0, 0]
        [0, 0, 0, F]4
                  4

Starting with our recursive function below, we define our base cases for our traveler in a 1,1 grid,
    and in a grid with an m or n value of 0.
Rather than use a matrix and try and count the number of ways to possible move through the matrix following the rules,
    instead it is more efficient to imagine each possible move as stepping onto a new, smaller game board.
The recursion function thus returns the sum of the number of possible moves as you decrement down m and n.
1,1 is the bottom viable branch node for a move, because anytime the value of m or n is 0, we don't have a move to count.

We have a binary search tree which is created as we decrement from m and n in separate branches,
    and our two inputs inform the exponent of our complexity
    O(2^m+n)
    And our space complexity is just the max depth (height) of the tree:
    O(m+n)

"""
def grid_recursive(m, n):
    # Base Cases
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    # Recursive return
    return grid_recursive(m - 1, n) + grid_recursive(m, n - 1)

##########################################################################################

"""
First, we can use lru_cache from functools to cheat...
"""

@lru_cache
def grid_recursive_functools(m, n):
    # Base Cases
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    # Recursive return
    return grid_recursive_functools(m - 1, n) + grid_recursive_functools(m, n - 1)

"""
But to better understand how the memoization is working, we can first investigate the number of steps 
    within the same grid sizes, for example m = 2, n = 3
                 2,3
        1,3               1,3
    0,3    1,2        1,2      2,1
        0,2   1,1  0,2  1,1  1,1  2,0
        
The number of nodes at the bottom of the branch are our valid or invalid moves - 1,1s return a valid move, a 0 is invalid.
We see that nodes with the value 1,2 and 2,1 each have 1 sub step of 1,1 which returns a valid incrementing move, 
    so we can memoize and equate 1,2 and 2,1 as key values for 1 ~
    further, any key value of (m,n) is also equal to (n,m)

"""
def grid_memo(m, n, memo={}):
    key = f'({m},{n})'
    if key in memo:
        return memo[key]
    # Base Cases
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = grid_memo(m - 1, n, memo) + grid_memo(m, n - 1, memo)
    return memo[key]

"""
  
To deduce the complexity of the memoized problem, we know that the maximum number of nodes is the product of
    of n*m - as our maximum number of inputs for m is m... and n is n... 
This simplifies our exponential time complexity from the recursive function, bringing this down to an 
O(m*n) time complexity,
while our space complexity remains the same at 
O(m+n) space complexity
"""


##########################################################################################

"""
To solve this problem with tabulation, each index will be iterated over multiple times 
    as we increment positively (take steps right or down) in our graph, with our base cases
    which pass values down from our valid step seed of 1,1 = 1
 
 [0 0 0 0 0 0]
 [0 1 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 0 0 0]
 
 We iterate right and down for each possible move, adding the possible move value 
    from the "home" index to the the next incrementing m and n (or y and x) indices:
    
 first move      several moves    even further  
 [0 0 0 0 0 0]   [0 0 0 0 0 0]    [0 0 0 0 0 0]
 [0 1 1 0 0 0]   [0 1 1 1 1 1]    [0 1 1 1 1 1]
 [0 1 0 0 0 0]   [0 1 1 1 1 0]    [0 1 2 3 4 5]
 [0 0 0 0 0 0]   [0 0 0 0 0 0]    [0 1 2 3 4 5]
 [0 0 0 0 0 0]   [0 0 0 0 0 0]    [0 0 0 0 0 0]
 [0 0 0 0 0 0]   [0 0 0 0 0 0]    [0 0 0 0 0 0]

All the way down to the finished matrix

 [ 0  0  0  0  0  0]
 [ 0  1  1  1  1  1]
 [ 0  1  2  3  4  5]
 [ 0  1  3  6 10 15]
 [ 0  1  4 10 20 35]
 [ 0  1  5 15 35 70]
 
O(m*n) time
O(m*n) space

I love a good numpy ndarray visualization.
"""

def grid_tab(m, n, tab = []):
    if tab == []:
        # dtype int is not large enough to store exceedingly big numbers, switched to float for scale
        tab = (np.zeros(shape=(m + 1, n + 1), dtype=float))
        tab[1,1] = 1
        # print(tab)
    for y in range(m + 1):
        for x in range(n + 1):
            if (y + 1 <=  n):
                tab[y + 1][x] += tab[y][x]
            if (x + 1 <= n):
                tab[y][x + 1] += tab[y][x]
            # print(tab)
    # print(tab)

    # Base Cases
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    # Recursive return
    return tab[m,n]




if __name__ == '__main__':
    m = 18
    n = 18
    # solution_recursive = grid_recursive(m, n)
    solution_functools = grid_recursive_functools(m, n)
    solution_memo = grid_memo(m, n)
    solution_tab = grid_tab(m, n)

    print(f'Example outputs for m = {m}, n = {n}')
    print(f'lru_cache solution   : {solution_functools}')
    print(f'Memoization solution : {solution_memo}')
    print(f'Tabulation solution  : {int(solution_tab)}')

"""
Example outputs for m = 18, n = 18
lru_cache solution   : 2333606220
Memoization solution : 2333606220
Tabulation solution  : 2333606220
"""



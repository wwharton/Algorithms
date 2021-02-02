from functools import lru_cache

"""
The following functions are examples of dynamic programming, starting with a recursive function, then improving
the function with hard-coded memoization and tabulation, and python library tools.


The Problem: FibonnaciSequence
    Return the nth value of Fib (starting with the 1 first position == 0, 2 position == 1, 3 position == 1)


The recursive fib function has exponential complexity.
From the top, each node has two branches, and nodes are repeated down the tree.
:
O(2^n) time
O(n) space (tree max depth)
"""


def fib_recursive(n):
    if n == 2:
        return 1
    if n == 1:
        return 0
    return fib_memo_functools(n - 1) + fib_memo_functools(n - 2)


######################################################################

"""
Memoizing the function improves the complexity from the original recursive function:
O(n) time
O(n) space 
"""


def fib_memo(n, memo={}):
    if n == 2:
        return 1
    if n == 1:
        return 0
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


######################################################################


"""
Tabulation allows us to solve the problem within a single iterating loop, yielding
O(n) time 
O(n) space 
because we only use the space of the dictionary (array)
"""


def fib_tab_sub(n):
    tab = [0] * n
    tab.append(0)  # Append an additional index to prevent stepping out of bounds as we iterate
    tab[1] = 1  # Starting value
    for i in range(2, n + 1):
        tab[i] = tab[i - 1] + tab[i - 2]
        # print(f' {i} : {tab[i]}')
    # Return tab n - 1 to solve for off by 1 due to 0 index
    return tab[n - 1]


######################################################################


"""
Alternative to the above function which solves for N by looking back as it steps forward,
we can plus equals
"""


def fib_tab_add(n):
    tab = [0] * n
    tab.append(0)
    tab.append(0)
    tab.append(0)
    # appended indices prevent us from stepping out of bounds of the list
    tab[1] = 1
    for i in range(n + 1):
        tab[i + 1] += tab[i]
        # print(tab)
        tab[i + 2] += tab[i]
        # print(tab)

    # return the value for n - 1 to account for the 0 index
    return tab[n - 1]


"""
    I find this above "additive" solution to be much less intuitive than the previous "subtraction" solution.
    In order to better understand it, I manually iterated several steps and then drew out the lists as the function ran

    for visual reference, tab[i + 1] = tab[i + 1] + tab[i]

                          tab[0] = 0
                          tab[1] = 1

                          i = 0
                          tab[i + 1] = tab[i + 1] + tab[i]
                              tab[1] =     tab[1] + tab[0]
                              tab[1] =         1  +     0
                              tab[1] =         0
                          tab[i + 2] = tab[i + 2] + tab[i]
                              tab[2] =     tab[2] + tab[0]
                              tab[2] =         0  +     0
                              tab[2] =         0

                          i = 1
                          tab[i + 1] = tab[i + 1] + tab[i]
                              tab[2] =     tab[2] + tab[1]
                              tab[2] =         0  +     1
                              tab[2] =         1
                          tab[i + 2] = tab[i + 2] + tab[i]
                              tab[3] =     tab[3] + tab[1]
                              tab[3] =         0  +     1
                              tab[3] =         1

                          i = 2
                          tab[i + 1] = tab[i + 1] + tab[i]
                              tab[3] =     tab[3] + tab[2]
                              tab[3] =         1  +     1
                              tab[3] =         2
                          tab[i + 2] = tab[i + 2] + tab[i]
                              tab[4] =     tab[4] + tab[2]
                              tab[4] =         0  +     1
                              tab[4] =         1

                          i = 3
                          tab[i + 1] = tab[i + 1] + tab[i]
                              tab[4] =     tab[4] + tab[3]
                              tab[4] =         1  +     2
                              tab[4] =         3
                          tab[i + 2] = tab[i + 2] + tab[i]
                              tab[5] =     tab[5] + tab[3]
                              tab[5] =         0  +     2
                              tab[5] =         2

                              This final value of tab[5] is not correct yet, it must be iterated again to add the tab[4] value of 3
                              This is a consequence of the loop structure, we must perform 2(n + 1) calculations to solve for n
                              But the constants are of little concern for Big Oh notation, we are still left of O(n)

    The continuing pattern, as each index is iterated over twice, 
        updates its value relative to the newly generated preceding and following values.
    It can be further visualized as you look at the progressively iterating list

    [0, 1, 0, 0, 0, 0, 0, 0]
    [0, 1, 0, 0, 0, 0, 0, 0]
    [0, 1, 1, 0, 0, 0, 0, 0]
    [0, 1, 1, 1, 0, 0, 0, 0]
    [0, 1, 1, 2, 0, 0, 0, 0]
    [0, 1, 1, 2, 1, 0, 0, 0]
    [0, 1, 1, 2, 3, 0, 0, 0]
    [0, 1, 1, 2, 3, 2, 0, 0]
    [0, 1, 1, 2, 3, 5, 0, 0]
    [0, 1, 1, 2, 3, 5, 3, 0]
    [0, 1, 1, 2, 3, 5, 8, 0]
    [0, 1, 1, 2, 3, 5, 8, 5]

"""

######################################################################

"""
Finally, the functools library in python gives us access to lru_cache which automatically caches
    results from function calls into a dictionary, to be referred to for future calls. Thanks Guido + Co.
"""


@lru_cache(maxsize=1000)
def fib_memo_functools(n):
    if n == 2:
        return 1
    if n == 1:
        return 0
    return fib_memo_functools(n - 1) + fib_memo_functools(n - 2)


if __name__ == '__main__':
    n = 60
    solution_memo = fib_memo(n)
    solution_memo_functools = fib_memo_functools(n)
    solution_tabulation_add = fib_tab_add(n)
    solution_tabulation_sub = fib_tab_sub(n)

    print(f'The {n}th number in the Fibonnaci sequence, starting with 0')
    print(f'Printed with hard-coded memoization: {solution_memo}')
    print(f'Printed with Lru_cache memoization: {solution_memo_functools}')
    print(f'Printed with subtracting tabulation: {solution_tabulation_sub}')
    print(f'Printed with additive tabulation: {solution_tabulation_add}')

"""
    Output:
    The 60th number in the Fibonnaci sequence, starting with 0
    Printed with hard-coded memoization: 956722026041
    Printed with Lru_cache memoization: 956722026041
    Printed with subtracting tabulation: 956722026041
    Printed with additive tabulation: 956722026041

"""







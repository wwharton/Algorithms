from functools import lru_cache

"""
Our recursive solution has inputs:
    m = target sum
    n = array length

The maximum height of our tree is m, because given a value of 1 in the list,
    subtracting 1 from m, m times, leaves us at 0.

    m = height

For each n in our array length, we multiply by the height,
    which equals the target sum, giving us:

    O(n^m) time complexity
    O(m) space complexity

The value of targetSum changes during recursive function calls, as the remainder value is passed in place 
    for the targetSum argument.
We subtract from these targetSum/remainders the values of the n array, until we either go negative, or hit zero exactly,
    then passing a boolean value up the chain.


"""


def can_sum_recursive(targetSum, numbers):
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for i in numbers:
        remainder = targetSum - i
        if can_sum_recursive(remainder, numbers) == True:
            return True
    return False

"""

@lru_cache doesn't work as neatly here. It requires the list to be a tuple to be passed in.
Max Size must be upped from default 128 for this func.

"""

@lru_cache(maxsize=1000)
def can_sum_functools(targetSum, numbers):
    numbers_list = list(numbers)
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for i in numbers_list:
        remainder = targetSum - i
        if can_sum_recursive(remainder, numbers) == True:
            return True
    return False

"""

To Memoize this function, we use a dictionary where we pass in targetSum values as the key during recursion.
The recursive calls pass the remainder value in place for the targetSum argument, so our dictionary keys
    are more specifically the starting targetSum and then the possible remainders following the subtraction operations.
As we continue to subtract n array values from the targetSum/remainder values, whenever we reach a base case,
    a key/value pair is entered in the dictionary for that remainder. 
If we ever attempt to solve for that remainder again during recursion, we already have that value cached.

In terms of complexity, with inputs:
    m = target sum
    n = array length
    
Memoizing it brings us down to:
    O(m*n) time (reflected in us only iterating through one branch)
    O(m) space (due to the constant height of the branch we iterate)

"""

def can_sum_memo(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False


    for i in numbers:
        remainder = targetSum - i
        if can_sum_memo(remainder, numbers, memo) == True:
            memo[targetSum] = True
            return True
        memo[targetSum] = False
    return False


"""

For tabulation, we need a list of n + 1 of all values False, then set our seed value of 0 as True, since by "adding nothing"
    we can always reach an answer of 0
Then we step through the list and for each value of true, we check and see if the current index + any value of n is in range.
If it is in range, we set it to true, then check the next value of n.
Then we scan the list for the next value of true, and apply the same math.
Finally when we are done iterating, we check index[targetSum] and return its value.

Our time complexity now is reflected in our loop where for each value of targetSum (m) we iterate len(numbers) (n) times
    and the only space we need is m + 1, or simply m
    
O(m*n) time complexity
O(m) space complexity

"""

def can_sum_tab(targetSum, numbers):


    # tab = [0] * targetSum
    # tab.append(0)
    # for i in range(targetSum + 1):
    #     tab[i] = False
    # tab[0] = True

    # List comprehension is a much better way to init this bool list
    tab = [False for _ in range(targetSum + 1)]
    tab[0] = True

    for i in range(targetSum + 1):
        if tab[i] == True:
            for num in numbers:
                if i + num < len(tab):
                    tab[i + num] = True

    print(tab)

    return tab[targetSum]


if __name__ == '__main__':

    # n = 300
    # m = [7, 14]

    n = 7
    m = [5, 4, 3, 2]

    tuple = tuple(m)

    # recursion_ans = can_sum_recursive(n, m)
    recursion_cache = can_sum_functools(n, tuple)
    memo_ans = can_sum_memo(n, m)
    tab_ans = can_sum_tab(n, m)

    # print(f'Recursion answer is: {recursion_ans}')
    print(f'Functools answer is: {recursion_cache}')
    print(f'Memoization answer is: {memo_ans}')
    print(f'Tabulation answer is: {memo_ans}')




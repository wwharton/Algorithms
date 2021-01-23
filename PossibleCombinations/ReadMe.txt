This problem was given as part of a code screener for a junior developer position.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Given a total, calculate the number of ways to achieve total as a sum of integers from 1 to k.

Example

total = 8
k = 2

To reach 8, there are 5 different ways 0, 1, and 2 can be uniquely combined:
[1, 1, 1, 1, 1, 1, 1, 1]
[2, 1, 1, 1, 1, 1, 1, 0]
[2, 2, 1, 1, 1, 1, 0, 0]
[2, 2, 2, 1, 1, 0, 0, 0]
[2, 2, 2, 2, 0, 0, 0, 0]
5 combinations

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

My first attempts, illustrated in "attempting_formula_solutions.py" fell apart for values of k greater than 2,
because they do not account for combinations involving mixed values of k (example, total=6 k=3 : [3, 2, 1, 0, 0, 0])


I succeeded in writing a brute force backtracking script that generates answers, but is not viable for large values of total and k.

The brute force solution iterates across a list, incrementing the starting index and incrementing the possible k values:

Here is an example with inputs: total = 5, k = 3 - which has 5 combinations which sum to 5

[1, 0, 0, 0, 0]
[1, 1, 0, 0, 0]
[1, 1, 1, 0, 0]
[1, 1, 1, 1, 0]
[1, 1, 1, 1, 1]

[2, 0, 0, 0, 0]
[2, 1, 0, 0, 0]
[2, 1, 1, 0, 0]
[2, 1, 1, 1, 0]
[2, 1, 1, 1, 1]
[2, 2, 0, 0, 0]
[2, 2, 1, 0, 0]
[2, 2, 1, 1, 0]
[2, 2, 1, 1, 1]
[2, 2, 2, 0, 0]
[2, 2, 2, 1, 0]
[2, 2, 2, 1, 1]
[2, 2, 2, 2, 0]
[2, 2, 2, 2, 1]
[2, 2, 2, 2, 2]

[3, 0, 0, 0, 0]
[3, 1, 0, 0, 0]
[3, 1, 1, 0, 0]
[3, 1, 1, 1, 0]
[3, 1, 1, 1, 1]
[3, 2, 0, 0, 0]
[3, 2, 1, 0, 0]
[3, 2, 1, 1, 0]
[3, 2, 1, 1, 1]
[3, 2, 2, 0, 0]
[3, 2, 2, 1, 0]
[3, 2, 2, 1, 1]
[3, 2, 2, 2, 0]
[3, 2, 2, 2, 1]
[3, 2, 2, 2, 2]
[3, 3, 0, 0, 0]
[3, 3, 1, 0, 0]
[3, 3, 1, 1, 0]
[3, 3, 1, 1, 1]
[3, 3, 2, 0, 0]
[3, 3, 2, 1, 0]
[3, 3, 2, 1, 1]
[3, 3, 2, 2, 0]
[3, 3, 2, 2, 1]
[3, 3, 2, 2, 2]
[3, 3, 3, 0, 0]
[3, 3, 3, 1, 0]
[3, 3, 3, 1, 1]
[3, 3, 3, 2, 0]
[3, 3, 3, 2, 1]
[3, 3, 3, 2, 2]
[3, 3, 3, 3, 0]
[3, 3, 3, 3, 1]
[3, 3, 3, 3, 2]
[3, 3, 3, 3, 3]

Here are example solutions for different inputs:
total = 10
k = 5

[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[2, 1, 1, 1, 1, 1, 1, 1, 1, 0]
[2, 2, 1, 1, 1, 1, 1, 1, 0, 0]
[2, 2, 2, 1, 1, 1, 1, 0, 0, 0]
[2, 2, 2, 2, 1, 1, 0, 0, 0, 0]
[2, 2, 2, 2, 2, 0, 0, 0, 0, 0]
[3, 1, 1, 1, 1, 1, 1, 1, 0, 0]
[3, 2, 1, 1, 1, 1, 1, 0, 0, 0]
[3, 2, 2, 1, 1, 1, 0, 0, 0, 0]
[3, 2, 2, 2, 1, 0, 0, 0, 0, 0]
[3, 3, 1, 1, 1, 1, 0, 0, 0, 0]
[3, 3, 2, 1, 1, 0, 0, 0, 0, 0]
[3, 3, 2, 2, 0, 0, 0, 0, 0, 0]
[3, 3, 3, 1, 0, 0, 0, 0, 0, 0]
[4, 1, 1, 1, 1, 1, 1, 0, 0, 0]
[4, 2, 1, 1, 1, 1, 0, 0, 0, 0]
[4, 2, 2, 1, 1, 0, 0, 0, 0, 0]
[4, 2, 2, 2, 0, 0, 0, 0, 0, 0]
[4, 3, 1, 1, 1, 0, 0, 0, 0, 0]
[4, 3, 2, 1, 0, 0, 0, 0, 0, 0]
[4, 3, 3, 0, 0, 0, 0, 0, 0, 0]
[4, 4, 1, 1, 0, 0, 0, 0, 0, 0]
[4, 4, 2, 0, 0, 0, 0, 0, 0, 0]
23 combinations

Ultimately, I succeeded in writing the solution I imagined, but it's time complexity is not suited for larger inputs.

One of the example test cases was:
(total = 56 and k = 23) % 1000000007 = 483076
and while I think my current code could generate a solution given enough time... it is not worth pursuing.

This problem is very similar to any bin packing problem, and
research suggests this is also similar to the kth sum problem, or a dynamic programming problem:
https://www.geeksforgeeks.org/count-ofdifferent-ways-express-n-sum-1-3-4/
https://stackoverflow.com/questions/58486802/find-the-number-of-ways-to-find-the-total-sum-value-using-the-range-1-to-k

The geeks for geeks page addresses a more complex dp solution which I do not understand yet.

The stack overflow answers were similar to the answer which I arrived at (not viable).

Given this research, I do not have the context / knowledge to solve this problem in a way that accounts for time complexity.

I'll return to this later. Very frustrating way to spend 12 hours.


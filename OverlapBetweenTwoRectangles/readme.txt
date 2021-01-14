Find the area of overlapping rectangles given two inputs with this format:
first corner y, first corner x, width, height

example input:
3 4 4 4
5 2 4 4

Output:
[[0 0 1 1 1 1 1]
 [0 0 1 1 1 1 1]
 [1 1 2 2 2 1 1]
 [1 1 2 2 2 1 1]
 [1 1 2 2 2 1 1]
 [1 1 1 1 1 0 0]
 [1 1 1 1 1 0 0]]
The area of overlap is: 4

Input:
20 20 4 7
21 22 5 8

Output:
[[1 1 1 1 1 0 0 0]
 [1 1 2 2 2 1 1 1]
 [1 1 2 2 2 1 1 1]
 [1 1 2 2 2 1 1 1]
 [1 1 2 2 2 1 1 1]
 [1 1 2 2 2 1 1 1]
 [1 1 2 2 2 1 1 1]
 [1 1 2 2 2 1 1 1]
 [0 0 1 1 1 1 1 1]
 [0 0 1 1 1 1 1 1]]
The area of overlap is: 12


To the point of time complexity, without any optimization we start at O(n) as the complexity scales linearily with the size of the array,
where n = the total area of the array, defined by max_width * max_height
The only optimization I included was to "normalize" the starting rectangle coordinates, which you can see above.
By normalize I mean to say, bring them as far in the negative y and x direction as possible to limit deadspace with an input such as:
20 20 4 4
21 21 4 4
where originally the array may look like
[[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 ...
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 0]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 2 2 2 2 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 2 2 2 2 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 2 2 2 2 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 2 2 2 2 1]
 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1]]

it now looks like
[[1 1 1 1 1 0 0 0]
 [1 1 2 2 2 1 1 1]
 [1 1 2 2 2 1 1 1]
 [1 1 2 2 2 1 1 1]
 [1 1 2 2 2 1 1 1]
 [1 1 2 2 2 1 1 1]
 [1 1 2 2 2 1 1 1]
 [1 1 2 2 2 1 1 1]
 [0 0 1 1 1 1 1 1]
 [0 0 1 1 1 1 1 1]]
 

So instead of starting at 20 20 and 21 21, now we start at 0, 0 and 1, 1
or for examples where the two rectangles overlap leaving a gnomon deadspace in the negative y, x corner, for example
3 4 4 4
5 2 4 4
we now start at 2, 0 and 0, 2 respectively for each rectangle (leaving a necessary deadspace from 0,0 to 1, 1
this doesn't necessarily affect the scaling of the problem, as it could still scale on an infinite linear scale with
larger and larger rectangles being drawn, but it does however address the deadspace problem
so sometimes it will be more efficient!

 The problem can also be solved with a time complexity of O(1) using a formula easily derived from google... 
 But this was more fun, and beautiful, and is straight from my brain.

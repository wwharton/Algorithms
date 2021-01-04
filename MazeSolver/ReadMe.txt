Maze solver using the graph data structure and Dijkstra's path, breadth first search - O(V).
In our case, the time complexity is O(5001), as we have 5001 white pixels (paths), and 5200 black pixels (boundaries).

This cript solves Pixel mazes where a black is boundary, and a white pixel is path.
Maze requires black pixel border, with a white pixel "start" and "end" on the top and bottom rows.
Given example maze is 101x101 pixels


Not optimized for time complexity, an A* search algo optimization could increase efficieny.
For this implementation, I used a list of visited nodes, but this could also be achieved with a boolean mask.


Example black and white Array from OpenCV - compressed for print
       [  0, 255,   0, ...,   0,   0,   0],
       [  0, 255, 255, ..., 255, 255,   0],
       [  0, 255,   0, ...,   0, 255,   0],
       ...,
       [  0, 255,   0, ...,   0, 255,   0],
       [  0, 255, 255, ..., 255, 255,   0],
       [  0,   0,   0, ...,   0, 255,   0]

Example solution = solvedmaze.png

To run on your machine, refactor path "D:/Python Projects/Algorithms/MazeSolver/maze.png" to the location of maze.png in your directory.
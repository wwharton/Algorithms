"""
On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

    "G": go straight 1 unit;
    "L": turn 90 degrees to the left;
    "R": turn 90 degrees to the right.

The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

LRLLL
LLLLL

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

"""


def solution_one():
    starting_string = 'GGLLGG'

    string = starting_string
    for j in range(3):
        starting_string += string

    # The crux for my solution here is a balancing act: For every step North, we need to take one South, East, for West
    # if we are to remain walking within a bounding box.
    # With a dictionary of 4 entries, we adjust our direction by changing our key
    # Starting on 0 (north) an R will take us to 1 (East), etc.,
    # Attempting to step past 3 will bring us back to 0, as will stepping past 0 to 3
    map_dict = {
        0: 0, # North
        1: 0, # East
        2: 0, # South
        3: 0 # West
    }

    n = 0

    for _, step in enumerate(string):
        if step == 'R':
            if n == 3:
                n = 0
            else:
                n = n + 1

        if step == 'L':
            if n == 0:
                n = 3
            else:
                n = n - 1

        if step == 'G':
            map_dict[n] = map_dict[n] + 1

            print(map_dict)

    if map_dict[0] - map_dict[2] == 0 and map_dict[1] - map_dict[3] == 0:
        return True
    else:
        return False

"""
Runtime: 36 ms, faster than 11.57% of Python3 online submissions for Robot Bounded In Circle.
Memory Usage: 14.3 MB, less than 49.30% of Python3 online submissions for Robot Bounded In Circle.

Time complexity is nice at O(N) linear, but we can do better in terms of solving speed

We can do better

"""

def solution_two():
    """
    Thinking on the coordinate plane, and thinking about our directions, if we ever end facing the same direction
    as we started, we will never loop. (NN)

    We can't create a list of directions like [ N, E, S, W ] and step through that left or right very easily, because
    our frame of reference is changing every time we turn.



    steps don't matter, only directions... EXCEPT We need to account for the base case where we end facing north AT 0,0

    Using a graph, we can track direction facing, and new directions
    O(N)

    """

    string = 'GLGLGGLGL' # false
    # string = 'GL' # true
    # string ="GLRLLGLL" # True
    # string = 'GG' # false
    # string = 'GLGR'


    # graph to track which direction we are facing
    # Coding logic into a data structure isn't a best practice, but we're gonna go with it for this one
    facing_dict = {
        'N': ['W', 'E'],
        'E': ['N', 'S'],
        'S': ['E', 'W'],
        'W': ['S', 'N']
    }

    facing = 'N'

    coords = [0,0]

    for i in string:

        # Tracking our turns with the graph
        if i == 'L':
            facing = facing_dict[facing][0]
        if i == 'R':
            facing = facing_dict[facing][1]

        # this keeps track of if we end up back at 0,0 (sum == 0 is a base case for True)
        if i == 'G':
            if facing == 'N':
                coords[1] += 1
            if facing == 'E':
                coords[0] += 1
            if facing == 'S':
                coords[1] -= 1
            if facing == 'W':
                coords[0] -= 1

    if tuple(coords) == (0,0):
        return True
    if facing == 'N':
        return False
    else:
        return True

""" 
Runtime: 32 ms, faster than 55.75% of Python3 online submissions for Robot Bounded In Circle.
Memory Usage: 14.1 MB, less than 92.22% of Python3 online submissions for Robot Bounded In Circle.

Leetcode accepted this, but it is a wrong solution
starting_string = 'GLGR'


Good enough for me. In the right time complexity O(N), pretty readable, and I understand the base cases:
End facing a diff direction
or End at 0,0

For future reference, here is a leetcode user's solution

x, y, dx, dy = 0, 0, 0, 1
for i in instructions:
    if i == 'R': dx, dy = dy, -dx
    if i == 'L': dx, dy = -dy, dx
    if i == 'G': x, y = x + dx, y + dy
return (x, y) == (0, 0) or (dx, dy) != (0,1)

I like that in this one directionality is described with dx, dy - while coords are simply x and y.

"""

    # if sum % 2 == 0:
    #     return True


    # print(facing)

    # if sum == 0 or sum < 0 or sum % 2 == 0:
    #     return True
    # else:
    #     return False







if __name__ == '__main__':
    print(solution_two())
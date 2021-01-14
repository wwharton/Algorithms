import numpy as np


def gen_rect(sx, sy, height, width):
    # Drawing a rectangle into our array is now easy
    # taking the starting x and y, width and height, we can update values in the array

    # Feed height in with '+ 1' again to iterate over our height, accounting for index 0
    for j in range(height + 1):
        # dy, or difference of y, is our starting y position plus our iterator (starting at 0)
        dy = sy + j

        # Now feed in the width, and step through
        for i in range(width + 1):
            # diff of x same as diff of y logic
            dx = sx + i

            # Now at each of our indices, we want to check and see if we've been here before
            # a value of 0 indicates fresh, untouched index, write a 1
            if master_ndarray[dy][dx] == 0:
                master_ndarray[dy][dx] = 1
            # Else, a value other than 0 (so an already written 1!) becomes a 2
            # This way we can recycle this function when we draw the second,
            # delivering the two rectangles and their entire overlapped area
            # represented by 2s
            else:
                master_ndarray[dy][dx] = 2

    # We don't need to return anything here, the changes to master_ndarray are global to the script
    # But let's print to see the payoff of our hardwork
    print(master_ndarray)

def find_overlap(master_ndarray):
    # To find the overlap, we are investigating the occurence of '2's in our master array

    # First we want to know how much distance we need to cover to find our 2s
    # so we grab the h and w of our array to use in for-ranges later
    height, width = master_ndarray.shape

    # We'll want to keep track of the indices where we discover any 2's, so a new list is needed
    seen_overlap_indices = []

    # Now we iterate over height and width, yx scanning the whole array
    for i in range(height):
        for n in range(width):
            # For every two we encounter, we want to add the values to the seen_overlap_indices list
            if master_ndarray[i][n] == 2:
                # Append these values as tuples which we can unpack later
                seen_overlap_indices.append(tuple((i, n)))

    # To find the area of the overlap, we can now simply find the product of the differences between the first and last indices
    first_index = seen_overlap_indices[0]
    last_index = seen_overlap_indices[-1]
    # first y, first x...
    fy, fx = first_index
    ly, lx = last_index

    # The area is the product of the differences between the last and first y x coordinates
    area = (ly-fy)*(lx-fx)
    return area

def optimize_array_scope(y1, y2, x1, x2):
    # First we want to find a value for 'y greater' and 'x greater'
    # these are the larger of the two possible starting y and x coordinates

    if y1 >= y2:
        yg = y1
    else:
        yg = y2

    if x1 >= x2:
        xg = x1
    else:
        xg = x2

    # Then we want to calculate a diff of y and diff of x
    # We do this by grabbing the abs of the difference between the each pair of y coordinates and x coordinates, respectively
    dy = yg - abs((y1-y2))
    dx = xg - abs((x1-x2))

    # Then we can generate our new starting coordinates for each rectangle, minimizing deadspace to in the negative y and x directions
    y1 = y1 - dy
    y2 = y2 - dy
    x1 = x1 - dx
    x2 = x2 - dx

    return y1, y2, x1, x2




if __name__ == '__main__':

    # Okay, this is a bit of a mess, but there is a lot of input data here to parse
    # First capture inputs in the form of Y, X, W, H
    # Y, X are the starting indices for a rectangle
    # W is its width out from there
    # H is its height out from there
    one_rect = input()
    two_rect = input()

    one_rect_list = list(one_rect.split())

    two_rect_list = list(two_rect.split())

    # Here I encountered an issue where I was receiving null values when trying to map my list from its indices...
    # Solved by appending values into a new list.
    # Further work can be done to clean this up ~
    first_rect_values = []
    second_rect_values = []
    for i in range(len(one_rect_list)):
        first_rect_values.append(int(one_rect_list[i]))
    for i in range(len(two_rect_list)):
        second_rect_values.append(int(two_rect_list[i]))

    # Here we map values of our inputs to something more usable
    # sy for starting y, sx for starting x, one_ prefix to indicate rect number
    one_sy = first_rect_values[0]
    one_sx = first_rect_values[1]
    one_width = first_rect_values[2]
    one_height = first_rect_values[3]

    two_sy = second_rect_values[0]
    two_sx = second_rect_values[1]


    two_width = second_rect_values[2]
    two_height = second_rect_values[3]

    # The following function will optimize the scope of our array, minimizing deadspace
    one_sy, two_sy, one_sx, two_sx = optimize_array_scope(one_sy, two_sy, one_sx, two_sx)

    # To generate our starting array, I want to know the max shape of the array
    # Get the max possible height and width of each rectangle by adding sx with w, sy with H
    one_max_height = one_sy + one_height

    two_max_height = int(two_sy) + int(two_height)

    # Check to see which rectangle has the largest possible height, width, set that as our max
    if one_max_height >= two_max_height:
        max_height = one_max_height
    else:
        max_height = two_max_height

    one_max_width = int(one_sx) + int(one_width)

    two_max_width = int(two_sx) + int(two_width)

    if one_max_width >= two_max_width:
        max_width = one_max_width
    else:
        max_width = two_max_width


    # Finally we can get to the fun stuff, draw an array with the shape max_h by max_w
    # '+ 1' added in order to counter index 0
    master_ndarray = np.zeros(shape=(max_height + 1, max_width + 1), dtype=np.int)

    # Print to see our initial results
    print(master_ndarray)

    #


    # See functions for further comments
    gen_rect(one_sx, one_sy, one_height, one_width)
    print(master_ndarray)

    gen_rect(two_sx, two_sy, two_height, two_width)
    print(master_ndarray)

    area_of_overlap = find_overlap(master_ndarray)
    print(f'The area of overlap is: {area_of_overlap}')

    # To the point of time complexity, without any optimization we start at O(n) as the complexity scales linearily with the size of the array,
    # where n = the total area of the array, defined by max_width * max_height
    # The only optimization I included was to "normalize" the starting rectangle coordinates, that is to say
    # bring them as far in the negative y and x direction as possible to limit deadspace with an input such as:
    # 20 20 4 4
    # 21 21 4 4
    # Instead of starting at 20 20 and 21 21, now we start at 0, 0 and 1, 1
    # or for examples where the two rectangles overlap leaving a gnomon shaped deadspace in the negative y, x corner, for example
    # 3 4 4 4
    # 5 2 4 4
    # we now start at 2, 0 and 0, 2 respectively for each rectangle (leaving a deadspace from 0,0 to 1, 1
    # this doesn't necessarily affect the scaling of the problem, as it could still scale on an infinite linear scale with
    # larger and larger rectangles being drawn, but it does however address the deadspace problem
    # so sometimes it will be more efficient!

    # The problem can also be solved with a time complexity of O(1) using a formula easily derived from google...
    # But this was more fun, and beautiful, and is straight from my brain.







"""
Given a rectangular cake with height h and width w,
and two arrays of integers horizontalCuts and verticalCuts where
horizontalCuts[i] is the distance from the top of the rectangular
cake to the ith horizontal cut and similarly, verticalCuts[j]
is the distance from the left of the rectangular cake to the
jth vertical cut.

Return the maximum area of a piece of cake after you cut at
each horizontal and vertical position provided in the arrays
horizontalCuts and verticalCuts. Since the answer can be a
huge number, return this modulo 10^9 + 7.


Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4
Explanation: The figure above represents the given rectangular cake.
Red lines are the horizontal and vertical cuts.
After you cut the cake, the green piece of cake has the maximum area.

"""
def solution_one():
    # h = 5
    # w = 4
    # # horizontalCuts = [1,2,4]
    # # verticalCuts = [1,3]
    #
    # # horizontalCuts = [3, 1]
    # # verticalCuts = [1]
    # horizontalCuts = [3]
    # verticalCuts = [3]

    h = 50
    w =15
    horizontalCuts = [37,40,41,30,27,10,31]
    verticalCuts = [2,1,9,5,4,12,6,13,11]


    adjHzCuts = horizontalCuts + [h]
    adjVCuts = verticalCuts + [w]

    adjHzCuts.sort()
    adjVCuts.sort()

    largest_diff_h = 0
    try:
        # 2n - as we step through each list almost in full
        for i in range(len(adjHzCuts)):
            diff = adjHzCuts[i + 1] - adjHzCuts[i]
            if largest_diff_h < diff:
                largest_diff_h = diff
    except:
        pass

    largest_diff_w = 0
    try:
        # 2n - as we step through each list almost in full
        for i in range(len(adjVCuts)):
            diff = adjVCuts[i + 1] - adjVCuts[i]
            if largest_diff_w < diff:
                largest_diff_w = diff
    except:
        pass

    mod = (10**9) + 7
    ans = int((largest_diff_h * largest_diff_w)) % mod

    return ans



if __name__ == '__main__':
    h = 5
    w = 4
    horizontalCuts = [1, 2, 4]
    verticalCuts = [1, 3]
    print(solution_one())
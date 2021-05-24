
import heapq

def solution_one():
    boxTypes = [[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]]
    truckSize = 35

    # heapq.heapify(boxTypes)
    # print(boxTypes)
    #
    # boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]


    boxTypes.sort(key=lambda x: x[1], reverse=True)

    print(boxTypes)

    count = 0
    sum = 0
    for i in range(len(boxTypes)):
        for j in range(boxTypes[i][0]):
            count += 1
            sum += boxTypes[i][1]
            if count == truckSize:
                return sum
    return sum

def solution_two():

    boxTypes = [[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]]
    truckSize = 35

    # heapq.heapify(boxTypes)
    # print(boxTypes)
    #
    # boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]

    # Python sort complexity is O(n log(n))
    boxTypes.sort(key=lambda x: x[1], reverse=True)

    # import heapq
    # # Heapify sort complexity is O(N)
    # heapq.heapify(boxTypes)
    # reversed(boxTypes)

    print(boxTypes)

    count = 0
    sum = 0
    for i in range(len(boxTypes)):
        boxCount = min(boxTypes[i][0], truckSize)
        count += boxCount
        sum += (boxCount * boxTypes[i][1])
        truckSize -= boxCount

        if truckSize == 0:
            return sum
    return sum


def solution_three():

    boxTypes = [[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]]
    truckSize = 35

    boxTypes = [[5,10],[2,5],[4,7],[3,9]]
    truckSize = 10
    # expected 91

    sum = 0
    big = 0
    for i in range(len(boxTypes)):
        test_big = boxTypes[i][1]
        if test_big > big:
            big = test_big

    bucket = [0 for x in range(big+1)]


    for pair in boxTypes:
        qty = pair[0]
        val = pair[1]
        bucket[val] += qty

    boxCount = truckSize
    # bucket.reverse()
    #
    # for units, boxes in enumerate(bucket):
    #     units = big - units
    #     remaining = min(boxCount, boxes)
    #     sum += remaining * units
    #     boxCount -= remaining
    #     if boxCount == 0:
    #         return sum
    # return sum

    for units in range(big,0,-1):
        print(units)
        remaining = min(boxCount, bucket[units])
        print(remaining)
        sum += units * remaining
        boxCount -= remaining
        if boxCount == 0:
            return sum
    return sum



    #     idx = big - index
    #     min_val = min(idx, boxCount)
    #     sum += (min_val * val)
    #
    #     boxCount -= val
    #     if boxCount == 0:
    #         return sum
    #
    # print(sum)
    #
    # return sum

    # print(bucket)
    # print(big)


    #     boxCount = min(boxTypes[i][0], truckSize)
    #     count += boxCount
    #     sum += (boxCount * boxTypes[i][1])
    #     truckSize -= boxCount
    #
    #     if truckSize == 0:
    #         return sum
    # return sum




if __name__ == '__main__':
    print(solution_three())
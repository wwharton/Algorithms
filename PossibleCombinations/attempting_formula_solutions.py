import math



def possible_sums(total, k):
    sum = 1
    adder = 0
    loops = 0
    if k == 1:
        print('k = 1')
        return sum
    else:
        # print(f'1 : 1 : 1')
        for i in range(2, k + 1):
            sum += math.floor(total/i)
            if i > 2:
                # loop through and perform the same as above for every i - 1 down to 3
                _, adder = recursion_loop(i, adder)
                sum += adder

    return sum

def recursion_loop(i, adder):
    while i > 2:
        for j in range(1, i):
            print(j)
            adder += math.floor(total/j)
        i = i - 1
        i, adder = recursion_loop(i, adder)
    return i, adder




def sums(total, k):
    sum = 1
    adder = 0
    if k == 1:
        print('k = 1')
        return sum
    else:
        # print(f'1 : 1 : 1')
        for i in range(2, k + 1):
            sum += math.floor(total/i)
           # print(f'{i} : {math.floor(total/i)} : {sum}')
            if i > 2:

                def closure_func(i, sum):
                    adder = 0
                    for j in range(1, i):
                        # adder += (j * (j + 1)) / 2
                        adder += math.floor(total / j)
                        sum += adder
                    return sum
                sum += closure_func(i, sum)

    return sum

def possible_sums_triangle(total, k):
    sum = 1
    adder = 0
    if k == 1:
        print('k = 1')
        return sum
    else:
        # print(f'1 : 1 : 1')
        for j in range(2, k + 1):
            n = math.floor(total / k)
            sum += (n * (n+1))/2


    return sum




if __name__ == '__main__':
    total = 56
    k = 23
    solution = sums(total, k)

    solution_2 = possible_sums_triangle(total, k)


   # print(solution)
    #print((solution%1000000007))

    print(solution_2)

    # (total = 56 / k = 23) %1000000007 = 483076


import itertools
import time

def list_to_set(array):
    # first convert list to tuple
    #array.sort(reverse=True)
    final_set.add(tuple(array))
    return final_set



def brute_force(total, k, start_index, array, break_val, final_set, sums):
    first_loop = False
    sum_array = sum(array)

    if sum_array != break_val:
        for k_val in range(1, k + 1):



            if array[-1] != k_val and first_loop == True:
                for n in range(start_index + 1, total):
                    array[n] = 0
                    # final_set = list_to_set(array)

                try:
                    array[start_index] = k_val
                    # final_set = list_to_set(array)
                    print(array)
                    if sum(array) == total:
                        sums += 1
                        #print(sums)
                        #print(array)
                except:
                    pass

                #print(array)

                start_index += 1

                #print(f'k_val passed as {k_val}')
                #final_set = list_to_set(array)
                array, start_index, final_set, sums = brute_force(total, k_val, start_index, array, break_val, final_set, sums)

                start_index -= 1

            if first_loop == False:
                for j in range(start_index, total):
                    array[j] = k_val
                    print(array)
                    # final_set = list_to_set(array)
                    if sum(array) == total:
                        sums += 1
                        #print(array)
                        #print(sums)


                    #print(array)
                    first_loop = True

    return array, start_index, final_set, sums



if __name__ == '__main__':
    total = 5
    k = 3
    start_index = 0
    sums = 0
    array = []
    final_set = set({})
    for i in range(total):
        array.append(0)

    break_val = (total * k)

    array, _, final_set, sums = brute_force(total, k, start_index, array, break_val, final_set, sums)

    print(sums)





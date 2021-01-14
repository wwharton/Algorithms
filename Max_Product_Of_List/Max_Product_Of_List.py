# First input is the number of queries to take
# Following inputs add values to a list

# take the list and return the highest possible product of three numbers from the list

def max_product(list_nums):
    product_list = []
    # Buckle in for ugly time complexity.
    # Loops will iterate through every index key
    for x in range(len(list_nums)):
        for y in range(len(list_nums)):
            for z in range(len(list_nums)):
                # d of index holds the value of each index key
                dx = int(list_nums[x])
                dy = int(list_nums[y])
                dz = int(list_nums[z])
                # Then we must ensure we aren't calculating the product of any duplicate index key values
                # Room for improvement here, this is dirty
                if x != y and y != z and x != z:
                    new_product = dx * dy * dz
                    # And we generate a list of every possible product
                    product_list.append(new_product)

    # And finally return the max product of the generated list
    return max(product_list)

if __name__ == '__main__':
    size_of_list = int(input())
    list_nums = []

    for i in range(size_of_list):
        new_val = input()
        list_nums.append(new_val)

    answer = max_product(list_nums)
    print(answer)
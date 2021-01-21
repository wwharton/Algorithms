# First input is the number of queries to take
# Following inputs add values to a list

# take the list and return the highest possible product of three numbers from the list

def max_product_bad(list_nums):
    product_list = []
    # Ugly time complexity answer, but it's cool!
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


def max_product_good(list_nums):
    list_nums.sort(reverse=True)
    answer = list_nums[0] * list_nums[1] * list_nums[2]
    return answer

if __name__ == '__main__':
    # first input
    size_of_list = int(input())
    list_nums = []

    for i in range(size_of_list):
        # recurring inputs
        new_val = input()
        list_nums.append(int(new_val))

    # So my first algo was cool, it works, but it has an awful time complexity.
    # I made it unnecessarily complex, I realized later.
    answer_complex = max_product_bad(list_nums)

    # While driving in the car, I was thinking about the problem,
    #   and had a light-bulb moment. I realized how dumb my original answer was.
    answer_simple = max_product_good(list_nums)
    print(answer_simple)

    # In retrospect, the complex solution would be applicable if the problem were such that
    #   I was attempting to find numbers whose product was an exact number - similar to the
    #   numbers challenge in the British TV show Countdown.



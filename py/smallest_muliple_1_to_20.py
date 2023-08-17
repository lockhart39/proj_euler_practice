# 2,520 is the smallest number that can be divided by each of the numbers from 1 to 10 without a remainder.
# What is the smallest, positive number that is evenly divisible by all of the numbers from 1 to 20?

def create_number_list(up_to_num):
    custom_num_list = []
    # since range will stop at the number before the 2nd arg
    # add 1 to up_to_num
    for i in range(1, up_to_num + 1):
        custom_num_list.append(i)

    return custom_num_list

# starting at 1, keep iterating up to ___ 
# if every number from 1 to 20 can be divided into i then print the i and break the loop 

def divisible_number_check(divisible_nbrs, max_num):
    for i in range(1, max_num):
        div_bool = True
        for num in divisible_nbrs:
            if i % num != 0:
                div_bool = False
        if div_bool == True:
            print(i, divisible_nbrs)
            break

numbers_1_to_20 = create_number_list(up_to_num = 20)

divisible_number_check(divisible_nbrs = numbers_1_to_20, max_num = 500000000)

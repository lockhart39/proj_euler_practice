# 1) Find the sum of all the multiples of 3 or 5 below 1000.

# create a list/array of numbers 1 - 1000

def create_list_to_1000():
    list_1_1000 = []

    for i in range(1, 1000):
        list_1_1000.append(i)

    return list_1_1000

# extract numbers that are multiples of 3 or 5


def extract_multiples_3_to_5(arg_list):
    list_3_5_multiples = []

    for num in arg_list:
        # use the modulo operator to determine if a number is divisible by 3 or 5
        if num % 3 == 0 or num % 5 == 0:
            list_3_5_multiples.append(num)

    return list_3_5_multiples

# sum the multiples of 3 or 5

list_to_1000 = create_list_to_1000()

list_of_3_5_multiples =  extract_multiples_3_to_5(list_to_1000)

print('The sum of all multiples of 3 or 5 below 1,000: ' + str(sum(list_of_3_5_multiples)))

#!/usr/bin/python3
def max_integer(my_list=[]):
    # Find the biggest integer in a list (max)
    if len(my_list) == 0:
        return None

    big_value = my_list[0]
    for num in my_list:
        if num > big_value:
            big_value = num

    return big_value

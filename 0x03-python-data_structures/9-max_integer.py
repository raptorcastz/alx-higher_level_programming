#!/usr/bin/python3

def max_integer(my_list=[]):
    #Find the biggest integer of a list.(max)
    if len(my_list) == 0:
        return (None)
    max= my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > max:
            max = my_list[i]

    return (max)

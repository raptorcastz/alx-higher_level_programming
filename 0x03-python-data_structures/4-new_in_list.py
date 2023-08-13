#!/usr/bin/python3
# 4-new_in_list.py


def new_in_list(my_list, idx, element):
    # make a copy of the original list.
    # We'll use list slicing [:] as an easy way to make a copy.
    # Check if the index is in range. If it's not, return the original list.
    # Otherwise, replace the specified element and return the new list.
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    copy = [x for x in my_list]
    copy[idx] = element
    return (copy)

#!/usr/bin/python3
# 4-new_in_list.py


def new_in_list(my_list, idx, element):
    # Try make a copy of the original list.
    # then use list slicing [:] as an easy way to make a copy.
    copy_my_list = my_list[:]

    # Check if the index is in range. If it's not, return the original list.
    if idx < 0 or idx >= len(copy_my_list):
        return copy_my_list

    # Otherwise, replace the specified element and return the new list.
    copy_my_list[idx] = element
    return copy_my_list

#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # Delete an item at a specific position in a list.
    if idx < 0 or idx >= len(my_list):
        return my_list[:]  # Return a copy of the original list

    # Create a copy of the original list
    new_list = my_list[:]

    # Delete the item at the specified index
    del newm_list[idx]

    return new_list

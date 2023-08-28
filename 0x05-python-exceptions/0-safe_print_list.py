#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        val = 0
        for i in my_list:
            if val < x:
                print(i, end="")
                val += 1
        print()
        return val
    except Exception as e:
        print("An error occurred", e)
        return val
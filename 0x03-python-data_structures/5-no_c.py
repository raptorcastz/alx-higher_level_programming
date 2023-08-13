#!/usr/bin/python3
def no_c(my_string):
    # Initialize an empty string to store the result
    result = ""
    for charl in my_string:
        # Only add the character to the result if it's not 'c' or 'C'
        if charl != 'c' and charl != 'C':
            result += charl
    return result

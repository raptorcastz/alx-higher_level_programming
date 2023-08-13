#!/usr/bin/python3

import sys
from calculator_1 import add, subtract, multiply, divide

if __name__ == "__main__":
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": subtract, "*": multiply, "/": divide}
    if sys.argv[2] not in set(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
    

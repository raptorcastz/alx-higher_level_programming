#!/usr/bin/python3

import sys

if __name__ == "__main__":
    num = len(sys.argv) - 1
    if num == 0:
        print("0 arguments.")
    elif num == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(num))
        for i in range(num):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
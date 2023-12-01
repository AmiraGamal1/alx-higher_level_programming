#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv_length = len(argv)
    argn = "argument" if argv_length == 2 else "arguments"
    delm = "." if argv_length == 1 else ":"
    print("{:d} {:s}{:s}".format(argv_length - 1, argn, delm))
    for i, arg in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, arg))

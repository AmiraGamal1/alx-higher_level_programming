#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv_length = len(argv)
    argn = "argument" if argv_length == 2 else "arguments"
    delm = "." if argv_length == 1 else ":"
    print("{} {:s}{:s}".format(argv_length - 1, argn, delm))
    for i in range(1, argv_length):
        print("{}: {}".format(i, argv[i]))

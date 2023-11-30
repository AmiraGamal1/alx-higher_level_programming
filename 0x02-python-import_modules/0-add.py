#!/usr/bin/python3
""" make the add function called by __main__ only """
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 1
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

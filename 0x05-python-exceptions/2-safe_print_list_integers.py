#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """print integer

    Args:
        my_list (list): list

        x (int): number of values to print
    Returns:
         number of integer values printed
    """
    ret = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (TypeError, ValueError):
            continue
    print("")
    return (ret)

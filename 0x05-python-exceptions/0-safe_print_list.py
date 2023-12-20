#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elements from list

    Args:
         my_list (list): the list
         x (int): the number of elements

    Returns:
         The number of the elements to print
    """
    i = 0
    for elem in range(x):
        try:
            print("{}".format(my_list[elem]), end="")
            i += 1
        except IndexError:
            break
    print("")
    return (i)

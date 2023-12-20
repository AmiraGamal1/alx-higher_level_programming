#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """function that divides element by element 2 lists

    Args:
        my_list_1 (list): list
        my_list_2 (list): list
        list_length: length of the list
    Returns:
        list of divided elements
    """
    res = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            res.append(div)
    return (res)

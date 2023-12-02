#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)
    if length == 0:
        return ([])
    divisible = [False if i % 2 != 0 else True for i in range(length)]
    return (divisible)

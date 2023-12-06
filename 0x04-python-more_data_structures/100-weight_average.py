#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        res = 0
        weight = 0
        for item in my_list:
            res += item[0] * item[1]
            weight += item[1]
        return (res / weight)
    return (0)

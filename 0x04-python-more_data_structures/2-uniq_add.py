#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqe = set(my_list)
    sum = 0
    for i in uniqe:
        sum += i
    return (sum)

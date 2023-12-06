#!/usr/bin/python3
def weight_average(my_list=[]):
    """ returns the weighted average"""
    if not my_list:
        return 0

    ints = 0
    tot = 0

    for i in my_list:
        ints += i[0] * i[1]
        tot += i[1]

    return (ints / tot)

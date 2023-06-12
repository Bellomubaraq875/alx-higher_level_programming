#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    # index = 0
    largest = my_list[0]
    for value in my_list:
        if value < largest:
            continue
        else:
            largest = value

    return largest

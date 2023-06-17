#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list = list(set(my_list))
    new_list = []
    new_list = sum(map(lambda x: x, my_list))
    return new_list

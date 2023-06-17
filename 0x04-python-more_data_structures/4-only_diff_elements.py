#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    newList = []
    for element in set_1 ^ set_2:
        newList.append(element)
    return newList

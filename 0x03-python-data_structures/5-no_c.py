#!/usr/bin/python3
def no_c(my_string):
    newString = ""
    for each_letter in my_string:
        if each_letter == 'c' or each_letter == 'C':
            continue
        newString += each_letter
    return newString

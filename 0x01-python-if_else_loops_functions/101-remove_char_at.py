#!/usr/bin/python3
def remove_char_at(str, n):
    strc = str
    if n < 0:
        y = n
    else:
        y = n + 1
    strc = strc[:n] + strc[(y):]
    return strc

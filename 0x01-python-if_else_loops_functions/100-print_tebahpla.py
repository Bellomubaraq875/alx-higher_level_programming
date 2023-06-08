#!/usr/bin/python3
change = -33
letter = 122

while letter >= 65:
    x = chr(letter)
    print("{}".format(x), end="")
    letter += change

    if change == -33:
        change = 31
    else:
        change = -33

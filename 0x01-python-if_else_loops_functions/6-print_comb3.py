#!/usr/bin/python3
for number in range(0, 10):
    for x in range(number, 10):
        if x != number and number != 8:
            print("{}{}".format(number, x), end=", ")
print("89")

#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    digit = number % 10
    print("{}".format(digit), end="")
    return digit

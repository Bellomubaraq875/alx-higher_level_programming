#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    numb = abs(number)
    dig = -(numb % 10)
    if dig == 0:
        print(f"Last digit of {number} is {dig} and is 0")
    elif dig < 6 and dig != 0:
        print(f"Last digit of {number} is {dig} and is less than 6 and not 0")
else:
    dig = number % 10
    if dig > 5:
        print(f"Last digit of {number} is {dig} and is greater than 5")
    elif dig == 0:
        print(f"Last digit of {number} is {dig} and is 0")
    elif dig < 6 and dig != 0:
        print(f"Last digit of {number} is {dig} and is less than 6 and not 0")

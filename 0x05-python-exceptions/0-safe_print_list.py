#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    coubt = 0
    for element in range(x):
        try:
            print("{}".format(my_list[element]), end="")
            coubt += 1
        except IndexError:
            print()
            return coubt
    print()
    return coubt

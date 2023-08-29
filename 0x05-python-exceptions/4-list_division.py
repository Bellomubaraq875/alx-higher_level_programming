#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for number in range(list_length):
        try:
            c = my_list_1[number] / my_list_2[number]
        except ZeroDivisionError:
            print("division by 0")
            c = 0
        except TypeError:
            print("wrong type")
            c = 0
        except IndexError:
            print("out of range")
            c = 0
        finally:
            newlist.append(c)
    return newlist

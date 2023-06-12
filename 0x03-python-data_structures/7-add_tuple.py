#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # new_tuple = ()
    if len(tuple_a) < 1:
        tuple_a = (0, 0)
    elif len(tuple_a) < 2:
        tuple_a = (tuple_a[0], 0)

    # a shorter way to handle the if and elif statement above
    tuple_b += (0, 0)

    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    len1 = len(tuple_a)
    len2 = len(tuple_b)

    if len1 == 0:
        a1 = 0
        a2 = 0
    elif len1 == 1:
        a1 = tuple_a[0]
        a2 = 0
    else:
        a1 = tuple_a[0]
        a2 = tuple_a[1]

    if len2 == 0:
        b1 = 0
        b2 = 0
    elif len2 == 1:
        b1 = tuple_b[0]
        b2 = 0
    else:
        b1 = tuple_b[0]
        b2 = tuple_b[1]

    new_tuple = (a1 + b1, a2 + b2)
    return new_tuple

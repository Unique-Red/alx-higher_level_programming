#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_a = list(a_dictionary.keys())
    list_a.sort()
    for i in list_a:
        print("{}: {}".format(i, a_dictionary.get(i)))

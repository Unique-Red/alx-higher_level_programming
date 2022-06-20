#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ab = 0
    for z in range(x):
        try:
            print(my_list[z], end='')
            ab += 1
        except IndexError:
            break
    print()
    return ab

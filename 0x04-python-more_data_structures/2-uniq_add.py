#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    sum_up = 0
    for i in range(len(my_list)):
        x = my_list[i]
        [unique.append(x) for x in my_list if x not in unique]
    for j in range(len(unique)):
        sum_up += unique[j]
    return sum_up

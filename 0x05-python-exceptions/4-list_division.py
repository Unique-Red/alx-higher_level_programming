#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    # A function that divides element by element 2 lists

    temp_list = []
    for i in range(0, list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            temp_list.append(result)
    return (temp_list)

#!/usr/bin/python3


import sys


def safe_function(fct, *args):

    # a function that executes a function safely

    try:
        result = fct(*args)
        return (result)
    except Exception:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)

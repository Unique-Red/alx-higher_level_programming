#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{} argument".format(len(argv) - 1), end="")
    if len(argv) - 1 == 0:
        print("s.")
    else:
        if len(argv) - 1 == 1:
            print(":")
        else:
            print("s:")
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))

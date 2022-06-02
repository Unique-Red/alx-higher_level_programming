#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for entry in dir(hidden_4):
        if entry[0] != '_':
            print("{}".format(entry))

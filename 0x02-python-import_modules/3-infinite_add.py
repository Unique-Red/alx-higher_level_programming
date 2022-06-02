#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    temp = 0
    numero2 = 0
    for i in range(1, len(argv)):
        numero = int(argv[i])
        resultado = numero + numero2
        numero2 = resultado
        temp = resultado
    print("{}".format(temp))

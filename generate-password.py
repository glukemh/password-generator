import sys
from random import random


def main():
    password = ''
    try:
        n = int(sys.argv[1])
    except:
        n = 15

    for i in range(n):
        password += chr(int(random()*94 + 33))
    print(password)


if __name__ == '__main__':
    main()

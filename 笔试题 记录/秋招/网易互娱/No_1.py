#coding=utf-8
import sys

def func(number):

    bin_number = bin(number)[2: ]
    if bin_number == bin_number[::-1]:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":

    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        number = int(sys.stdin.readline().strip())
        print(func(number))


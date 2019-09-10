#coding=utf-8
import sys

def func(n, values):

    values.sort()

    if n % 2 == 0:
        return values[n // 2 - 1]
    else:
        return values[n // 2]

if __name__ == "__main__":

    n = int(sys.stdin.readline().strip())
    values = list(map(int, sys.stdin.readline().strip().split()))

    print(func(n, values))
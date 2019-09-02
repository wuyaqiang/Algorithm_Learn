#coding=utf-8
import sys

def func(n, values):

    num_count = {}
    for num in values:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    for num, count in num_count.items():
        if count > (n // 2):
            return "NO"
    return "YES"


if __name__ == "__main__":

    T = int(sys.stdin.readline().strip())

    for i in range(T):

        n = int(sys.stdin.readline().strip())
        values = list(map(int, sys.stdin.readline().strip().split()))

        print(func(n, values))
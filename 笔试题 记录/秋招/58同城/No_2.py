#coding=utf-8
import sys

def func(n, scores):

    if n == 1:
        return 1

    i = 0
    l = 0
    increase = False
    decrease = False
    temp_list = []

    return 10


if __name__ == "__main__":

    n = int(sys.stdin.readline().strip())
    scores = []
    for _ in range(n):
        s = int(sys.stdin.readline().strip())
        scores.append(s)

    print(func(n, scores))
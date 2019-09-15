#coding=utf-8
import sys

def func(n, a, b, points):

    return n // 3


if __name__ == "__main__":

    n, a, b = list(map(int, sys.stdin.readline().strip().split()))
    points = []

    for _ in range(n):
        point = list(map(int, sys.stdin.readline().strip().split()))
        points.append(point)

    print(func(n, a, b, points))
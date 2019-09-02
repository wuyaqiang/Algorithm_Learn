#coding=utf-8
import sys

def func(n, matrix_list):

    # for matrix in matrix_list:
    #     x1, y1, x2, y2, val = matrix

    x1, y1, x2, y2, val = matrix_list[0]
    return abs(x1 - x2) * abs(y1 - y2) * 4

if __name__ == "__main__":

    n = int(sys.stdin.readline().strip())
    matrix_list = []
    for _ in range(n):
        values = list(map(int, sys.stdin.readline().strip().split()))
        matrix_list.append(values)

    print(func(n, matrix_list))
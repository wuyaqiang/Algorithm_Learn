#coding=utf-8
import sys

if __name__ == "__main__":

    n, m = list(map(int, sys.stdin.readline().strip().split()))
    nums = list(map(int, sys.stdin.readline().strip().split()))

    nums_in = [0] * n
    task_relate_matrix = []

    for i in range(m):
        a, b = list(map(int, sys.stdin.readline().strip().split()))
        task_relate_matrix[a-1][b-1] = 1
        nums_in[b-1] += 1

    for i in range(n):
        for j in range(n):
            if nums_in[]





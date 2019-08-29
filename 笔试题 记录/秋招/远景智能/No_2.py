#coding=utf-8
import sys

def func(limit, distance, fadianliang):

    value = [[0] * (limit + 1) for _ in range(len(distance) + 1)]

    for i in range(1, len(distance) + 1):
        for j in range(1, limit + 1):
            value[i][j] = value[i - 1][j]
            if j >= distance[i - 1] and value[i][j] < value[i - 1][j - distance[i - 1]] + fadianliang[i - 1]:
                value[i][j] = value[i - 1][j - distance[i - 1]] + fadianliang[i - 1]
    return value[-1][-1]

if __name__ == "__main__":

    input_distance = list(map(int, sys.stdin.readline().strip().split()))
    input_fadianliang = list(map(int, sys.stdin.readline().strip().split()))
    input_limit = int(sys.stdin.readline().strip())

    res = func(input_limit, input_distance, input_fadianliang)
    print(res)





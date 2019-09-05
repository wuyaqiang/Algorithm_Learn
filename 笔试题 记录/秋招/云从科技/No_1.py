#coding=utf-8
import sys

def func(values):

    if not values or len(values) == 0:
        return 0
    N = len(values)
    dp = [1] * N
    for i in range(1, N):
        for j in range(i):
            if values[i] > values[j]:
                dp[i] = max(dp[j] + 1, dp[i])

    return max(dp)

if __name__ == "__main__":

    values = list(map(int, sys.stdin.readline().strip().split(",")))
    res = func(values)
    print(res)
#coding=utf-8
import sys

def func(k, m, days):

    if k == 0:
        return 30
    if m == 0:
        return len(range(1, 31, k + 1))
    dp = [1 if i + 1 in days else 0 for i in range(30)]
    # dp[0] = 1
    for i in range(30):
        if dp[i] == 1:
            continue
        if sum(dp[max(0, i - k) : i]) == 0 and sum(dp[i+1 : i+1+k]) == 0:
            dp[i] = 1
    return sum(dp)

if __name__ == "__main__":

    T = int(sys.stdin.readline().strip())

    for _ in range(T):

        k, m = list(map(int, sys.stdin.readline().strip().split()))
        # if m > 0:
        days = list(map(int, sys.stdin.readline().strip().split()))
        # else:
        #     days = []
        print(func(k, m, days))
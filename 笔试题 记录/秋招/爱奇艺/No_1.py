#coding=utf-8
import sys

def func(N, seq):

    left, right = 0, N
    dp = [1 for _ in range(right)]
    for i in seq:
        temp_dp = [0 for _ in range(right)]
        if i == 0:
            left += 1
            for j in range(left, right):
                temp_dp[j] = temp_dp[j - 1] + dp[j - 1]
        elif i == 1:
            right -= 1
            for j in range(right - 1, left - 1, -1):
                temp_dp[j] = temp_dp[j + 1] + dp[j + 1]

        dp = temp_dp

    return dp[left] % (pow(10, 9) + 7)

if __name__ == "__main__":

    N = int(sys.stdin.readline().strip())

    seq = list(map(int, sys.stdin.readline().strip().split()))

    print(func(N, seq))
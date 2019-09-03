#coding=utf-8
import sys

def func(N, input_list):

    input_list.sort(key = lambda x: (x[0], x[1]))

    dp = [1] * N
    for i in range(1, N):
        l, r = 0, i - 1
        if input_list[r][1] <= input_list[i][1]:
            dp[i] = dp[l] + 1
        else:
            while l < r:
                mid = l + (r - l) // 2
                if input_list[mid][1] <= input_list[i][1]:
                    l = mid + 1
                else:
                    r = mid
            dp[i] = dp[l] + 1

    return dp[N - 1]

if __name__ == "__main__":

    N = int(sys.stdin.readline().strip())
    input_list = []
    for _ in range(N):
        X, H = list(map(int, sys.stdin.readline().strip().split()))
        input_list.append([X, H])

    res = func(N, input_list)
    print(res)
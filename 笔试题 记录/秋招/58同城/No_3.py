#coding=utf-8
import sys

def func(m, n, grid):

    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + grid[i][j]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + grid[i][j]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
    return dp[m - 1][n - 1]

if __name__ == "__main__":

    m = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    input_matrix = []
    for _ in range(m):
        row = list(map(int, sys.stdin.readline().strip().split()))
        input_matrix.append(row)

    res = func(m, n, input_matrix)
    print(res)
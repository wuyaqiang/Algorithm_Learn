#coding=utf-8
import sys

def func(k, m, days):

    if k == 0:
        return 30
    if m == 0:
        return len(range(1, 31, k + 1))
    # 初始化：长度为30的列表，将固定喝咖啡的日子置为1，其他为0
    dp = [1 if i + 1 in days else 0 for i in range(30)]
    for i in range(30):
        if dp[i] == 1:
            continue
        # 如果第i天前面k天没喝咖啡，同时后面k天也没喝，那第i天就可以喝，置为1
        if sum(dp[max(0, i - k) : i]) == 0 and sum(dp[i+1 : i+1+k]) == 0:
            dp[i] = 1
    return sum(dp)

if __name__ == "__main__":

    T = int(sys.stdin.readline().strip())

    for _ in range(T):

        k, m = list(map(int, sys.stdin.readline().strip().split()))
        days = list(map(int, sys.stdin.readline().strip().split()))
        print(func(k, m, days))
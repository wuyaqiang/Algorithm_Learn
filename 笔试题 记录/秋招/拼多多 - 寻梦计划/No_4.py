#coding=utf-8
import sys

def top_k_num(n, m, k):

    l, r = 1, n * m + 1
    while l < r:
        mid = (l + r) // 2
        count = 0
        temp = mid - 1
        for i in range(1, n + 1):
            count += min(m, temp // i)
        if count >= k:
            r = mid
        else:
            l = mid + 1
    return l - 1

if __name__ == "__main__":

    n, m, k = list(map(int, sys.stdin.readline().strip().split()))

    print(top_k_num(n, m, k))
import math
import sys

def helper(n, m):

    s1, s2, m = 0, 0, min(m, n - m)

    for index in range(m+1,n+1):
        s1 += math.log10(index)

    for index in range(2,n-m+1):
        s2 += math.log10(index)

    return math.ceil(10 ** ((s1 - s2) % 10))

def func(n, p, q):

    upper, up, down = n - q, 0, 0

    for up in range(p,upper+1):
        tmp_value = helper(n, up)
        up += up * tmp_value
        down += tmp_value

    m = 0
    while m > -1:
        if (1000000007 * m + up) % down == 0:
            return (1000000007 * m + up) // down
        m +=1

if __name__ == "__main__":

    n, p, q = list(map(int, sys.stdin.readline().strip().split()))
    res = func(n, p, q)
    print(res)


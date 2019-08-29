#coding=utf-8
import sys

def func(arr, k, x):

    l, r, n = 0, 0, len(arr)

    while n:
        if r - l + 1 <= k:
            r += 1
        else:
            if abs(arr[r] - x) < abs(arr[l] - x):
                l += 1
                r += 1
            else:
                break
        n -= 1

    return arr[l : r]


if __name__ == "__main__":

    # n = int(sys.stdin.readline().strip())
    input_arr = list(map(int, sys.stdin.readline().strip().split(",")))
    k = int(sys.stdin.readline().strip())
    x = int(sys.stdin.readline().strip())

    res = func(input_arr, k, x)
    print(",".join([str(i) for i in res]))




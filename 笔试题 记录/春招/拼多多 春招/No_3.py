#coding=utf-8
import sys

def func(values, d):
    L = len(values)
    total_num = (L * (L - 1)) // 2
    res = 0.0
    for i in range(L):
        cur_num = values[i]
        sub_L = values[ :i] + values[i+1: ]
        res += len([i for i in sub_L if abs(i-cur_num) <= d])
    return res / total_num / 2


if __name__ == "__main__":

    line = sys.stdin.readline().strip()[1: -1]
    values = list(map(int, line.split(",")))

    d = int(sys.stdin.readline().strip())

    print("%.6f" %func(values, d))
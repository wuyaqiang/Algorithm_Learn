#coding=utf-8
import sys

def func(values):

    cur_sum = 0
    max_sum = -1

    for n in values:
        if cur_sum <= 0:
            cur_sum = n
        else:
            cur_sum += n
        max_sum = max(max_sum, cur_sum)

    return max_sum


if __name__ == "__main__":

    line = sys.stdin.readline().strip().lstrip("[").rstrip("]")
    values = list(map(int, line.split(",")))

    print(func(values))
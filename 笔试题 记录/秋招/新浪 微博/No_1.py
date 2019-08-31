#coding=utf-8
import sys

def min_operation(input_nums):

    input_string.sort()
    res = 0
    for i in range(1, len(input_nums)):
        diff = input_nums[i - 1] - input_nums[i]
        if diff >= 0:
            res += (diff + 1)
            input_nums[i] = input_nums[i - 1] + 1
    return res

if __name__ == "__main__":

    input_string = list(map(int, sys.stdin.readline().strip().split(",")))

    res = min_operation(input_string)

    print(res)



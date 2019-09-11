#coding=utf-8
import sys

def max_sum_subarray(nums):

    cur_sum, max_sum = 0, -1

    for n in nums:
        if cur_sum <= 0:
            cur_sum = n
        else:
            cur_sum += n
        max_sum = max(max_sum, cur_sum)

    return max_sum

if __name__ == "__main__":

    input_prices = list(map(int, sys.stdin.readline().strip().split()))
    res = max_sum_subarray(input_prices)
    print(res)







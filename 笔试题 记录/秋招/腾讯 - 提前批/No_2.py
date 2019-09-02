#coding=utf-8
import sys

def func(a, b, k):

    # res = 0
    # for l in range(a, b + 1):
    #
    #     white_num = 0
    #     while white_num <= l:
    #         if white_num == 0 or white_num == l:
    #             res += 1
    #         else:
    #             red_num = l - white_num
    #             res += red_num + 1
    #         white_num += k
    # return res

    pass



if __name__ == "__main__":

    t, k = list(map(int, sys.stdin.readline().strip().split()))

    for i in range(t):
        a, b = list(map(int, sys.stdin.readline().strip().split()))
        print(func(a, b, k))
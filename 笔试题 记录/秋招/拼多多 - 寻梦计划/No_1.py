#coding=utf-8
import sys

def compare(n1, n2):

    n1_is_even = (n1 % 2 == 0)
    n2_is_even = (n2 % 2 == 0)

    if n1_is_even == n2_is_even:
        return True if n1 > n2 else False
    elif n1_is_even:
        return True
    else:
        return False


def sorted_topN(input_arr, N):

    if not input_arr or len(input_arr) == 0:
        return []

    length = len(input_arr)
    for i in range(length - 1):
        for j in range(length - 1, i, -1):
            if compare(input_arr[j], input_arr[j-1]):
                input_arr[j], input_arr[j-1] = input_arr[j-1], input_arr[j]
    return input_arr[ : N]

if __name__ == "__main__":

    input_arr, N = sys.stdin.readline().strip().split(";")
    input_arr = list(map(int, input_arr.split(",")))
    N = int(N)

    res = sorted_topN(input_arr, N)
    print(",".join([str(i) for i in res]))


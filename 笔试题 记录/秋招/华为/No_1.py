#coding=utf-8
import sys

def bit_find(n):

    n_binary = bin(n)[2: ][::-1]
    n_binary_len = len(n_binary)
    count, first_idx, find_first = 0, -1, False
    for i in range(n_binary_len - 2):
        if n_binary[i : i + 3 ] == "101":
            count += 1
            if not find_first:
                find_first = True
                first_idx = i
    # if not find_first:
    #     first_idx = -1
    return count, first_idx


if __name__ == "__main__":

    n = int(sys.stdin.readline().strip())

    res1, res2 = bit_find(n)

    print(str(res1) + " " + str(res2))
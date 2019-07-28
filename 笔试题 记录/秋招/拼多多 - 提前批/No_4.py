#coding=utf-8
import sys
def max_height(n, lengths, weights):
    if n < 1:
        return 0
    if n == 1:
        return 1
    length_and_weight = list(zip(lengths, weights))
    length_and_weight = sorted(length_and_weight, key=lambda x: x[0])
    cur_weight_sum = 0
    height = 0
    for i in range(n):
        if cur_weight_sum <= length_and_weight[i][1] * 7:
            cur_weight_sum += length_and_weight[i][1]
            height += 1
    return height
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    lengths = list(map(int, sys.stdin.readline().strip().split()))
    weights = list(map(int, sys.stdin.readline().strip().split()))
    print(max_height(n, lengths, weights))


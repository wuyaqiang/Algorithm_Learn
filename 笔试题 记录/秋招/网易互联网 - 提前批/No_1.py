#coding=utf-8
import sys

def last_q_permutation(n, choiced_permutation):

    res = []
    for i in range(n):
        res.append(n - choiced_permutation[i] + 1)
    return res

if __name__ == "__main__":

    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))

    res = last_q_permutation(n, values)
    print(" ".join([str(i) for i in res]))





#coding=utf-8
import sys

def sequence_exchange(n, values):
    if n < 1:
        return []

    return values

if __name__ == "__main__":

    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))

    res = sequence_exchange(n, values)
    print(" ".join([str(i) for i in res]))





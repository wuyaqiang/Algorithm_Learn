#coding=utf-8
import sys


if __name__ == "__main__":

    t = int(sys.stdin.readline().strip())
    for i in range(t):
        n = int(sys.stdin.readline().strip())
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        res = is_number_cycle(values)
        print(res)


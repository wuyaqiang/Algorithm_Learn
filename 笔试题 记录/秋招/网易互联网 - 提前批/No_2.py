#coding=utf-8
import sys

def is_number_cycle(values):
    max_val = max(values)
    sum_of_values = sum(values)
    if max_val > sum_of_values - max_val:
        return "NO"
    return "YES"


if __name__ == "__main__":

    t = int(sys.stdin.readline().strip())
    for i in range(t):
        n = int(sys.stdin.readline().strip())
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        res = is_number_cycle(values)
        print(res)


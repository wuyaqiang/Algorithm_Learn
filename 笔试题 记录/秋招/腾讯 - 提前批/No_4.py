#coding=utf-8
import sys

def func(n, T, m, string_list):

    res = 0
    for s in string_list:
        if len(s) > n:
            temp_T = T * (len(s) // n + 1)
            if s == temp_T[ : len(s)]:
                res += 1
        elif len(s) < n:
            temp_s = s * (n // len(s) + 1)
            if T == temp_s[ : n]:
                res += 1
        else:
            if T == s:
                res += 1
    return res

if __name__ == "__main__":

    n = int(sys.stdin.readline().strip())
    T = sys.stdin.readline().strip()
    m = int(sys.stdin.readline().strip())
    string_list = []
    for _ in range(m):
        line = sys.stdin.readline().strip()
        string_list.append(line)

    print(func(n, T, m, string_list))
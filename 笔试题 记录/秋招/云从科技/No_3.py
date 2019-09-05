#coding=utf-8
import sys

def func(S1, S2):

    i, j = 0, 0
    while i < len(S1) and j < len(S2):
        if S1[i] == S2[j]:
            i += 1
        j += 1
    if i == len(S1):
        return 1
    else:
        return 0

if __name__ == "__main__":

    S1 = sys.stdin.readline().strip()
    S2 = sys.stdin.readline().strip()
    res = func(S2, S1)
    print(res)
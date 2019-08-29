#coding=utf-8
import sys



if __name__ == "__main__":

    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))

    res = last_q_permutation(n, values)
    print(" ".join([str(i) for i in res]))





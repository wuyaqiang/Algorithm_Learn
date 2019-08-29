#coding=utf-8
import sys



if __name__ == "__main__":

    T = int(sys.stdin.readline().strip())
    for i in range(T):
        seq_S = sys.stdin.readline().strip()
        seq_T = sys.stdin.readline().strip()
        res = excellent_01_sequence(seq_S, seq_T)
        print(res)


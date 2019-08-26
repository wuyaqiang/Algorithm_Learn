#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

def func(N, matrix):

    return matrix

if __name__ == "__main__":

    N = int(sys.stdin.readline().strip())
    input_matrix = []

    for i in range(4):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        input_matrix.append(values)

    res = func(N, input_matrix)
    print("\n".join([" ".join([str(i) for i in row]) for row in res]))


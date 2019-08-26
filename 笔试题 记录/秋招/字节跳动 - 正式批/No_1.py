#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

def func(N, matrix):

    return N // 2

if __name__ == "__main__":

    N = int(sys.stdin.readline().strip())
    input_matrix = []

    for i in range(N):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        input_matrix.append(values)

    print(func(N, input_matrix))
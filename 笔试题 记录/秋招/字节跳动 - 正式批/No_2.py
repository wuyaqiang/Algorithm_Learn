#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

def func(n):

    return (n // 2) % 1000000007

if __name__ == "__main__":

    n = int(sys.stdin.readline().strip())

    print(func(n))
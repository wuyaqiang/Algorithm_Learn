#coding=utf-8
import sys

def func(values):

    return len(set(values))

if __name__ == "__main__":

    values = list(map(int, sys.stdin.readline().strip().split(",")))

    print(func(values))
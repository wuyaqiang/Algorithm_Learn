#coding=utf-8
import sys

for line in sys.stdin:
    graph = eval(line)
    n = len(graph)
    rudu = [0] * n
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                rudu[j] += 1
    while True:
        k = -1
        for i in range(n):
            if rudu[i] == 0:
                k = i
                break
        if k == -1:
            break
        else:
            rudu[k] = -1
            for i in range(n):
                if graph[k][i] != 0:
                    rudu[i] -= 1

    has_cycle = True
    for i in range(n):
        if rudu[i] > 0:
            has_cycle = False
            print("1")
            break
    if has_cycle:
        print("0")



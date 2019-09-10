#coding=utf-8
import sys

def func(n, s, values):

    queue, has_buy = [-1], {}
    has_buy[-1] = 0
    res, cur_sum = n + 1, 0

    for i, cost in enumerate(values):

        cur_sum += cost

        while queue and s <= cur_sum - has_buy[queue[0]]:
            res = min(res, i - queue.pop(0))

        while queue and has_buy[queue[-1]] >= cur_sum:
            queue.pop()

        has_buy[i] = cur_sum
        queue.append(i)

    if res >= n + 1:
        return -1
    else:
        return res


if __name__ == "__main__":

    N, S = list(map(int, sys.stdin.readline().strip().split()))
    values = list(map(int, sys.stdin.readline().strip().split()))

    print(func(N, S, values))
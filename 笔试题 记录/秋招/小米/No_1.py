#coding=utf-8
import sys


def max_profit(prices):

    n = len(prices)
    min_price, max_price = prices[0], prices[n - 1]
    cur_max_profit = [0] * n
    res = 0

    for i in range(1, n):
        cur_max_profit[i] = max(prices[i] - min_price, cur_max_profit[i - 1])
        min_price = prices[i] if prices[i] < min_price else min_price

    for i in range(n - 2, -1, -1):
        res = max(res, max_price - prices[i] + cur_max_profit[i])
        max_price = prices[i] if prices[i] > max_price else max_price

    return res

if __name__ == "__main__":

    input_prices = list(map(int, sys.stdin.readline().strip().split()))
    res = max_profit(input_prices)
    print(res)







'''
剑指 Offer 第63题
同 leetcode 121 122 题
'''

def maxProfit(prices):
    if not prices or len(prices) < 2:
        return 0
    max_profit = 0
    min_buy = prices[0]
    for price in prices[1:]:
        if price < min_buy:
            min_buy = price
            continue
        profit = price - min_buy
        max_profit = profit if profit > max_profit else max_profit

    return max_profit


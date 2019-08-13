'''
剑指 Offer 第63题
leetcode 121. Best Time to Buy and Sell Stock
leetcode 122. Best Time to Buy and Sell Stock II
leetcode 123. Best Time to Buy and Sell Stock III
leetcode 188. Best Time to Buy and Sell Stock IV
leetcode 309. Best Time to Buy and Sell Stock with Cooldown
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


'''
剑指 Offer 第10题 斐波那契数列 及其变体
leetcode 509. Fibonacci number
leetcode 70. Climbing Stairs
'''

def fibonacci(n):
    '''
    剑指 Offer 第10题 斐波那契数列
    leetcode 509. Fibonacci number
    '''
    # 解法一：递归
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 1
    # return fibonacci(n - 1) + fibonacci(n - 2)
    
    # # 解法二：bottom-up
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 1
    #
    # pre_pre_fib, pre_fib, cur_fib = 0, 1, 0
    # for _ in range(2, n + 1):
    #     cur_fib = pre_pre_fib + pre_fib
    #     pre_pre_fib = pre_fib
    #     pre_fib = cur_fib
    #
    # return cur_fib

    # 解法三：dp
    if n == 0:
        return 0
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

def jump_floor(n):
    '''
    一只青蛙一次可以跳上 1 级台阶，也可以跳上 2 级。求该青蛙跳上一个 n 级的台阶总共有多少种跳法?
    leetcode 70. Climbing Stairs
    '''
    if n < 3:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

def jump_floor_2(n):
    '''
    一只青蛙一次可以跳上 1 级台阶，也可以跳上 2 级…… 它也可以跳上 n 级。
    求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
    '''
    if n < 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] * 2

    return dp[n]






















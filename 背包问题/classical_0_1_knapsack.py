
def knapsack_1(W, w_list, val_list):
    '''
    递归解法, 时间复杂度较高, 为O(2^n)
    :param W: 背包最大容量限制
    :param w_list: 每个物品的容量列表
    :param val_list: 每个物品的价值列表
    :return: 不超过背包最大容量限制的最大价值
    '''
    if len(w_list) == 0 or W <= 0:
        return 0
    if w_list[0] > W:
        return knapsack_1(W, w_list[1: ], val_list[1: ])
    else:
        return max(knapsack_1(W, w_list[1: ], val_list[1: ]),
                   knapsack_1(W - w_list[0], w_list[1: ], val_list[1: ]) + val_list[0])

def knapsack_2(W, w_list, val_list):
    '''
    二维DP, 时间复杂度为O(nW), 空间复杂度为O(nW)
    '''
    if len(w_list) == 0 or W <= 0:
        return 0

    n = len(w_list)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if w_list[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w_list[i - 1]] + val_list[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][W]

def knapsack_3(W, w_list, val_list):
    '''
    一维DP, 时间复杂度为O(nW), 空间复杂度为O(W)
    '''
    if len(w_list) == 0 or W <= 0:
        return 0

    n = len(w_list)
    dp = [0] * (W + 1)

    for i in range(n):
        for j in range(W, 0, -1):
            if w_list[i] <= j:
                dp[j] = max(dp[j], dp[j - w_list[i]] + val_list[i])

    return dp[W]


if __name__ == '__main__':

    W = 11
    w_list = [1,2,5,6,7]
    val_list = [1,6,18,22,28]

    print(knapsack_1(W, w_list, val_list))
    print(knapsack_2(W, w_list, val_list))
    print(knapsack_3(W, w_list, val_list))

    pass


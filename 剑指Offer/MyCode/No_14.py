'''
剑指 Offer 第14题 剪绳子
'''

def max_product_after_cutting(length):

    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    # 解法一 贪心：
    times_of_3 = length // 3
    if length % 3 == 1:
        times_of_3 -= 1
    times_of_2 = (length - times_of_3 * 3) // 2

    return pow(3, times_of_3) * pow(2, times_of_2)

    # 解法二 动态规划：





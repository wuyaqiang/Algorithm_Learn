'''
剑指 Offer 第16题 数值的整数次方
leetcode 50. Pow(x, n)
leetcode 69. Sqrt(x)
'''

def my_pow(x, n):
    '''
    剑指 Offer 第16题 数值的整数次方
    leetcode 50. Pow(x, n)
    '''
    if x == 0 and n < 0:
        # 无效输入
        return 0

    if n == 0:
        return 1
    if n < 0:
        return 1 / my_pow(x, -n)
    if n % 2 == 0:
        return my_pow(x * x, n // 2)
    return x * my_pow(x, n - 1)

def my_sqrt(x):
    '''
    leetcode 69. Sqrt(x)
    '''
    # 解法一： 二分查找
    # l, r = 0, x
    # while l <= r:
    #     mid = l + (r - l) // 2
    #     if mid * mid == x:
    #         return mid
    #     elif mid * mid < x:
    #         if (mid + 1) * (mid + 1) > x:
    #             return mid
    #         else:
    #             l = mid + 1
    #     else:
    #         r = mid - 1
    # return 0

    # 解法二：
    # 牛顿法：https://www.wikiwand.com/en/Integer_square_root#/Using_only_integer_division
    r = x
    while r * r > x:
        r = int((r + x / r) / 2)
    return r


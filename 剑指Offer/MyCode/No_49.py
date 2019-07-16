'''
剑指 Offer 第49题 及其变体
leetcode 263. Ugly Number
leetcode 264. Ugly Number II
'''

def is_ugly(num):
    '''
    leetcode 263. Ugly Number 判断一个数是不是丑数
    '''
    if num < 1:
        return False
    for i in range(2, 6):
        if num <= 0:
            break
        while num % i == 0:
            num /= i
    return num == 1

def nth_ugly_number(n):
    '''
    求按从小到大顺序的第n个丑数
    剑指Offer 49 题
    leetcode 264. Ugly Number II
    '''
    if n < 1:
        return -1
    if n == 1:
        return 1
    ugly = [1] * n
    p2, p3, p5 = 0, 0, 0
    for i in range(1, n):
        ugly[i] = min(ugly[p2] * 2, ugly[p3] * 3, ugly[p5] * 5)
        if ugly[i] == ugly[p2] * 2:
            p2 += 1
        if ugly[i] == ugly[p3] * 3:
            p3 += 1
        if ugly[i] == ugly[p5] * 5:
            p5 += 1
    return ugly[n-1]


if __name__ == '__main__':

    print(is_ugly(14))
    print(nth_ugly_number(10))


















'''
剑指 Offer 第15题 及位运算相关
leetcode 136. Single Number
leetcode 137. Single Number II
leetcode 260. Single Number III
leetcode 169. Majority Element
leetcode 229. Majority Element II
leetcode 191. Number of 1 Bits
leetcode 268. Missing Number
'''

def single_number_1(nums):
    '''
    leetcode 136. Single Number
    '''
    '''
    见 No_56.py
    '''

def single_number_2(nums):
    '''
    leetcode 137. Single Number II
    '''
    '''
    见 No_56.py
    '''

def single_number_3(nums):
    '''
    leetcode 260. Single Number III
    '''
    '''
    见 No_56.py
    '''

def majority_element_1(nums):
    '''
    leetcode 169. Majority Element
    '''
    '''
    见 No_39.py
    '''

def majority_element_2(nums):
    '''
    leetcode 229. Majority Element II
    '''
    '''
    见 No_39.py
    '''

def number_of_one(n):
    '''
    剑指Offer 15
    leetcode 191. Number of 1 Bits
    '''
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

def missing_number(nums):
    '''
    leetcode 268. Missing Number
    '''
    # 解法一 位运算：
    res = len(nums)
    for i, n in enumerate(nums):
        res = res ^ i ^ n
    return res

    # 解法二 数学：
    # return sum(range(len(nums) + 1)) - sum(nums)















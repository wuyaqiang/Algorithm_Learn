'''
剑指 Offer 第56题 及其变体
同 leetcode 136 137 260题
'''

def one_number_in_two_times(nums):
    '''
    leetcode 136
    整数数组中除了一个数字，其他全部出现两次，找出该数字
    '''
    # 解法一 数学运算：
    # return 2 * sum(set(nums)) - sum(nums)
    # 解法二 位运算：
    res = 0
    for n in nums:
        res ^= n
    return res

def two_number_in_two_times(nums):
    '''
    leetcode 260
    整数数组中除了两个数字，其他全部出现两次，找出这两个数字
    '''
    if not nums or len(nums) < 2:
        return []
    diff = 0
    for n in nums:
        diff ^= n
    # diff = diff & (~diff + 1)   # 得到diff中的最后一位1
    diff = diff & -diff
    n1, n2 = 0, 0
    for n in nums:
        if n & diff == 0:
            n1 ^= n
        else:
            n2 ^= n
    return [n1, n2]

def one_number_in_three_times(nums):
    '''
    leetcode 137
    整数数组中除了一个数字，其他全部出现三次，找出该数字
    '''
    # 解法一 数学运算：
    # return (3 * sum(set(nums)) - sum(nums)) // 2

    # 解法二 位运算：
    res = 0
    for i in range(32):
        cur_bit_sum = 0
        mask = (1 << i)
        for n in nums:
            if n & mask:
                cur_bit_sum += 1

        if cur_bit_sum % 3 == 1:
            res |= mask

    if res & 1 << 31:   # 这一步很重要：If signed bit is set then adjust the number
        res -= 2 ** 32

    return res

    # 解法三 位运算：
    # 链接：https://cloud.tencent.com/developer/article/1131945



if __name__ == '__main__':

    print(one_number_in_two_times([0,1,1]))




















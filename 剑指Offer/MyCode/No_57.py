'''
剑指 Offer 第57题 及其变体
同 leetcode 167 829 题
'''

def two_sum(nums, target):
    '''
    和为 s 的两个数字
    '''
    if not nums or len(nums) < 2:
        return [-1, -1]
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return [l, r]
        elif s < target:
            l += 1
        else:
            r -= 1
    return [-1, -1]

def continuous_positive_sum_1(target):
    '''
    和为 s 的连续正数序列
    剑指 Offer 解法，该解法在 leetcode 上运行超时
    '''
    if target < 3:
        return 1
    count = 1
    l, r, mid = 1, 2, (target + 1) // 2
    cur_sum = l + r
    while l < mid:
        if cur_sum == target:
            count += 1
        while cur_sum > target and l < mid:
            cur_sum -= l
            l += 1
            if cur_sum == target:
                count += 1
        r += 1
        cur_sum += r
    return count

def continuous_positive_sum_2(target):
    '''
    和为 s 的连续正数序列
    运用等差数列的求和公式进行求解，该方法最优，详见 leetcode 829
    '''
    pass

if __name__ == '__main__':
    print(two_sum([2,7,11,15], 9))
    print(continuous_positive_sum_1(15))
















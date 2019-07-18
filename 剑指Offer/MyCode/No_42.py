'''
剑指 Offer 第42题 连续子数组的最大和
leetcode 53. Maximum Subarray
'''


def max_sum_subarray(nums):
    if not nums or len(nums) == 0:
        return 0
    cur_sum = 0
    max_sum = float('-inf')
    for n in nums:
        if cur_sum <= 0:
            cur_sum = n
        else:
            cur_sum += n
        max_sum = max(max_sum, cur_sum)
    return max_sum
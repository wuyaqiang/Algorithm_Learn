'''
剑指 Offer 第3题
leetcode 287. Find the Duplicate Number
'''

def findDuplicate(nums):
    '''
    数组中重复的数字
    '''
    # 解法一：修改了原始数组，时间复杂度为O(n)
    # i = 0
    # while i < len(nums):
    #     if nums[i] == i + 1:
    #         i += 1
    #     else:
    #         if nums[nums[i] - 1] == nums[i]:
    #             return nums[i]
    #         nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    # return -1

    # 解法二：利用二分查找，不修改原始数组，时间复杂度为O(nlogn)
    # low, high = 1, len(nums) - 1
    # while low <= high:
    #     mid = low + (high - low) // 2
    #     count = 0
    #     for n in nums:
    #         if low <= n <= mid:
    #             count += 1
    #     if low == high:
    #         if count > 1:
    #             return low
    #         else:
    #             break
    #     if count > mid - low + 1:
    #         high = mid
    #     else:
    #         low = mid + 1
    # return -1

    # 解法三：利用快慢指针，不修改原始数组，时间复杂度为O(n)
    slow, fast = nums[0], nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    fast = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

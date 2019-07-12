'''
剑指 Offer 第53题 及其变体
同 leetcode
'''

def count_of_number(nums, k):
    '''
    数字在排序数组中出现的次数
    '''
    # 解法一： 顺序遍历一遍即可，时间复杂度为O(n)
    # return nums.count(k)
    # 解法二： 由于数组是排序的，故可用二分查找，时间复杂度为O(logn)
    def get_first_idx(nums, k, l, r):
        # 返回数组中第一个k所在位置
        if l > r:
            return -1
        mid = l + (r - l) // 2
        if nums[mid] == k:
            if mid > 0 and nums[mid - 1] != k:
                return mid
            else:
                r = mid - 1
        elif nums[mid] < k:
            l = mid + 1
        else:
            r = mid - 1
        return get_first_idx(nums, k, l, r)

    def get_last_idx(nums, k, l, r):
        # 返回数组中最后一个k所在位置
        if l > r:
            return -1
        mid = l + (r - l) // 2
        if nums[mid] == k:
            if mid < len(nums) - 1 and nums[mid + 1] != k:
                return mid
            else:
                l = mid + 1
        elif nums[mid] < k:
            l = mid + 1
        else:
            r = mid - 1
        return get_last_idx(nums, k, l, r)

    if not nums or len(nums) == 0:
        return 0
    first_idx = get_first_idx(nums, k, 0, len(nums) - 1)
    last_idx = get_last_idx(nums, k, 0, len(nums) - 1)
    if first_idx != -1 and last_idx != -1:
        return last_idx - first_idx + 1
    return 0

def get_missing_number(nums, length):
    '''
    0到n-1中缺失的数字
    '''



if __name__ == '__main__':
    print(count_of_number([1,2,3,3,3,3,4,5], 3))














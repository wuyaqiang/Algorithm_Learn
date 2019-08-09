'''
剑指 Offer 第11题 旋转数组中的最小数字 及其变体
leetcode 153. Find Minimum in Rotated Sorted Array
leetcode 154. Find Minimum in Rotated Sorted Array II
leetcode 33. Search in Rotated Sorted Array
leetcode 81. Search in Rotated Sorted Array II
'''

def find_min_1(nums):
    '''
    leetcode 153. Find Minimum in Rotated Sorted Array
    数组中没有重复数字
    '''
    if not nums or len(nums) == 0:
        return -1

    l, r = 0, len(nums) - 1
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] > nums[r]:     # 只能与nums[r]判断，不能与nums[l]判断(当l到r一直递增时出错)
            l = mid + 1
        else:
            r = mid

    return nums[l]

def find_min_2(nums):
    '''
    leetcode 154. Find Minimum in Rotated Sorted Array II
    数组中有重复数字
    '''
    if not nums or len(nums) == 0:
        return -1

    l, r = 0, len(nums) - 1
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] > nums[r]:     # 只能与nums[r]判断，不能与nums[l]判断(当l到r一直递增时出错)
            l = mid + 1
        elif nums[mid] < nums[r]:
            r = mid
        else:
            r -= 1

    return nums[l]

def search_in_rotated_1(nums, target):
    '''
    leetcode 33. Search in Rotated Sorted Array
    数组中没有重复数字
    '''
    if not nums or len(nums) == 0:
        return -1

    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        # 注意有等号：
        if nums[mid] >= nums[l]:    # 既可以与nums[l]判断，也可以与nums[r]判断，无所谓
            # 注意有左边等号：
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            # # 注意有右边等号：
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1

def search_in_rotated_2(nums, target):
    '''
    leetcode 81. Search in Rotated Sorted Array II
    数组中有重复数字
    '''
    if not nums or len(nums) == 0:
        return False

    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return True
        if nums[mid] > nums[l]:     # 既可以与nums[l]判断，也可以与nums[r]判断，但是下面要保持一致
            # 注意有左边等号：
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        elif nums[mid] < nums[l]:
            # # 注意有右边等号：
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            l += 1
    return False












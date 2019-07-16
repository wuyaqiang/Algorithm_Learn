'''
剑指 Offer 第51题 及其变体
leetcode 493. Reverse Pairs
leetcode 315. Count of Smaller Numbers After Self
'''

def reverse_pairs_1(nums):
    '''
    剑指Offer 51 数组中的逆序对
    '''
    if not nums or len(nums) == 0:
        return 0

    def helper(l, r):
        if l >= r:
            return 0
        mid = l + (r - l) // 2
        count = helper(l, mid) + helper(mid + 1, r)
        # 这里的 j 不能放到下面 for 循环内部，因为如果前面的 i 满足前面的 j 个值，
        # 则后面的 i 一定也满足（i 递增，值递增），不需要对每个 i 重新遍历 j 。
        j = mid + 1
        for i in range(l, mid + 1):
            while j <= r and nums[i] > nums[j]:
                j += 1
            count += j - mid - 1
        nums[l: r + 1] = sorted(nums[l: r + 1])
        return count

    return helper(0, len(nums) - 1)

def reverse_pairs_2(nums):
    '''
    leetcode 493 Reverse Pairs
    '''
    if not nums or len(nums) == 0:
        return 0

    def helper(l, r):
        if l >= r:
            return 0
        mid = l + (r - l) // 2
        count = helper(l, mid) + helper(mid + 1, r)
        # 这里的 j 不能放到下面 for 循环内部，因为如果前面的 i 满足前面的 j 个值，
        # 则后面的 i 一定也满足（i 递增，值递增），不需要对每个 i 重新遍历 j 。
        j = mid + 1
        for i in range(l, mid + 1):
            while j <= r and nums[i] > 2 * nums[j]:
                j += 1
            count += j - mid - 1
        nums[l: r + 1] = sorted(nums[l: r + 1])
        return count

    return helper(0, len(nums) - 1)

def count_of_smaller_numbers(nums):
    '''
    leetcode 315 Count of Smaller Numbers After Self
    '''




if __name__ == '__main__':

    # print(reverse_pairs_1())
    print(reverse_pairs_2([2,4,3,5,1]))
    # print(count_of_smaller_numbers())




















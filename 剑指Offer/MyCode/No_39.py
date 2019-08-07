'''
剑指 Offer 第39题 及其变体
leetcode 169. Majority Element
leetcode 229. Majority Element II
'''

def major_num_1(nums):
    '''
    剑指Offer 39 / leetcode 169
    找出数组中超过一半的数字，即 major number
    '''
    # 解法一： O(n)
    major, count = 0, 0
    for num in nums:
        if count == 0:
            major = num
            count = 1
        elif num == major:
            count += 1
        else:
            count -= 1
    return major

    # 解法二： O(nlogn)
    # nums.sort()
    # return nums[len(nums) // 2]

def major_num_2(nums):
    '''
    leetcode 229
    找出数组中超过三分之一的数字，即 major number
    '''
    # 解法一 哈希表： 略

    # 解法二 Boyer-Moore Majority Vote algorithm：
    count_1, count_2, major_1, major_2 = 0, 0, 0, 1 #注意major_1和major_2初始化为不同值
    for n in nums:
        if n == major_1:    # 注意与major_num_1不同，这里不能先判断count_1和count_2等于0
            count_1 += 1
        elif n == major_2:
            count_2 += 1
        elif count_1 == 0:
            count_1, major_1 = 1, n
        elif count_2 == 0:
            count_2, major_2 = 1, n
        else:
            count_1 -= 1
            count_2 -= 1
    return [n for n in [major_1, major_2] if nums.count(n) > len(nums) // 3]


if __name__ == '__main__':

    print(major_num_1([1,1,1,1,2,4,5,6,7]))











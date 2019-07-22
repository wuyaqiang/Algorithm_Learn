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
    major, count = nums[0], 1
    for n in nums[1: ]:
        if n == major:
            count += 1
        else:
            count -= 1
        if count == 0:
            major = n
            count = 1
    return major

    # 解法二： O(nlogn)
    # nums.sort()
    # return nums[len(nums) // 2]

def major_num_2(nums):
    '''
    leetcode 229
    找出数组中超过三分之一的数字，即 major number
    '''
    pass

if __name__ == '__main__':

    print(major_num_1([1,1,1,1,2,4,5,6,7]))











'''
剑指 Offer 第45题 及其变体
leetcode 179. Largest Number
'''

def arrange_min_number(nums):
    '''
    剑指 Offer 45：把数组排成最小的数
    '''
    # 解法一： 利用冒泡排序实现
    if not nums:
        return ""
    nums = [str(n) for n in nums]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            num1 = nums[i] + nums[j]
            num2 = nums[j] + nums[i]
            if num1 > num2: # 排成最小
                nums[i], nums[j] = nums[j], nums[i]
    res = "".join(nums).lstrip("0")   # 处理特殊情况：[0, 0, 0]
    return "0" if res == "" else res
    # 解法二： 利用python内置排序sort，通过lambda自定义排序规则
    # 见leetcode 179 解析

def arrange_max_number(nums):
    '''
    leetcode 179: 把数组排成最大的数
    '''
    # 解法一： 利用冒泡排序实现
    if not nums:
        return ""
    nums = [str(n) for n in nums]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            num1 = nums[i] + nums[j]
            num2 = nums[j] + nums[i]
            if num1 < num2: # 排成最大
                nums[i], nums[j] = nums[j], nums[i]
    res = "".join(nums).lstrip("0")   # 处理特殊情况：[0, 0, 0]
    return "0" if res == "" else res
    # 解法二： 利用python内置排序sort，通过lambda自定义排序规则
    # 见leetcode 179 解析

if __name__ == '__main__':

    print(arrange_max_number([3, 30,34,5,9]))
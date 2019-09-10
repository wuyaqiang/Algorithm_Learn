#coding=utf-8
import sys

def permutation_to_max_number(nums):

    if not nums:
        return ""

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            num1 = nums[i] + nums[j]
            num2 = nums[j] + nums[i]
            if num1 < num2:
                nums[i], nums[j] = nums[j], nums[i]

    res = "".join(nums).lstrip("0")
    if res == "":
        return "0"
    else:
        return res


if __name__ == '__main__':

    values = sys.stdin.readline().strip().split(",")

    res = permutation_to_max_number(values)

    print(res)
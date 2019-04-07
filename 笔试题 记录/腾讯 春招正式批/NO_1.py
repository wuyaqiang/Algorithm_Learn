#coding=utf-8
import sys

def func(n, k, nums):
    for i in range(k):
        min_num = min([i for i in nums if i != 0])
        print(min_num)
        temp_nums = []
        count_0 = 0
        for x in nums:
            if x is 0:
                temp_nums.append(x)
                count_0 += 1
            else:
                sub = x - min_num
                temp_nums.append(sub)
                if sub == 0:
                    count_0 += 1

        nums = temp_nums
        if count_0 == len(temp_nums):
            print("0")
            return


if __name__ == "__main__":
    # 读取第一行的n, k
    line = sys.stdin.readline().strip()
    n, k = list(map(int, line.split()))

    nums_line = sys.stdin.readline().strip()
    nums = list(map(int, nums_line.split()))

    func(n, k, nums)


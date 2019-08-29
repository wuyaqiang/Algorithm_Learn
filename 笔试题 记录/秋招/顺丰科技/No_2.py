import sys

def longest_special_subsequence(n, nums):

    if not nums or n == 0:
        return 0

    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if nums[i] >= nums[j]:
                dp[i] = max(dp[j] + 1, dp[i])
    return max(dp)

if __name__ == '__main__':

    n = int(sys.stdin.readline().strip())
    input_arr = list(map(int, sys.stdin.readline().strip().split()))
    res = longest_special_subsequence(n, input_arr)
    print(res)


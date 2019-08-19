'''
剑指 Offer 第46题 把数字翻译成字符串
leetcode 91. Decode Ways
'''

def trans_int_to_string(num):
    if num < 0:
        return ""
    num = str(num)
    length = len(num)
    dp = [0] * length
    for i in range(length - 1, -1, -1):
        count = 0
        if i == length - 1:
            count += 1
        else:
            count += dp[i + 1]
            if 10 <= int(num[i] + num[i + 1]) <= 25:
                if i < length - 2:
                    count += dp[i + 2]
                else:
                    count += 1
        dp[i] = count

    return dp[0]

if __name__ == '__main__':

    print(trans_int_to_string(12258))
'''
剑指 Offer 第46题 把数字翻译成字符串
leetcode 91. Decode Ways （与剑指Offer原题略有不同）
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

def trans_int_to_string_2(s):
    '''
    leetcode 91. Decode Ways （与剑指Offer原题略有不同）
    此题数字'0'没有对应的字母.
    '''
    if not s or len(s) < 1:
        return 0
    length = len(s)
    dp = [0] * length
    dp[0] = 1 if s[0] != '0' else 0
    for i in range(1, length):
        first = int(s[i])
        second = int(s[i - 1] + s[i])
        if 1 <= first <= 9:
            dp[i] += dp[i - 1]
        if 10 <= second <= 26:
            dp[i] += dp[i - 2] if i >= 2 else 1
    return dp[-1]



if __name__ == '__main__':

    print(trans_int_to_string(12258))
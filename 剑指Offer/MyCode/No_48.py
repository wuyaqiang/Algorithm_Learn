'''
剑指 Offer 第48题 及其变体
leetcode 3. Longest Substring Without Repeating Characters
'''

def longest_substring_without_dup(s):
    '''
    最长不含重复字符的子字符串
    '''
    if len(s) < 2:
        return len(s)
    exist_char = {}
    start, res = 0, 0
    for cur, c in enumerate(s):
        if c in exist_char and start <= exist_char[c]:
            start = exist_char[c] + 1
        else:
            res = max(res, cur - start + 1)
        exist_char[c] = cur

    return res



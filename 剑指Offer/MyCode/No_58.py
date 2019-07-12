'''
剑指 Offer 第58题 及其变体
同 leetcode 151 189 796 题
'''

def rotate_string_1(s, k):
    '''
    左旋转字符串
    '''
    k = k % len(s)
    s = [c for c in s]
    reverse(s, 0, len(s) - 1)
    reverse(s, 0, k - 1)
    reverse(s, k, len(s) - 1)
    return ''.join(s)

def reverse(s, l, r):
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

def rotate_string_2(s, k):
    '''
    左旋转字符串
    '''
    k = k % len(s)
    return s[-k : ] + s[ : -k]

if __name__ == '__main__':
    print(rotate_string_1('abcde', 2))
    print(rotate_string_2('abcde', 2))
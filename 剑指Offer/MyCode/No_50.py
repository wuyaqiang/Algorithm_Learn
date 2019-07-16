'''
剑指 Offer 第50题
leetcode 387. First Unique Character in a String
'''
import string

def first_uniq_char(s):
    '''
    第一个只出现一次的字符
    '''
    # 解法一：遍历两遍字符串s，第一遍统计次数，第二遍取出第一个只出现一次的字符
    # count_dict = {}
    # for i in range(len(s)):
    #     count_dict[s[i]] = count_dict.get(s[i], 0) + 1
    #
    # for i in range(len(s)):
    #     if count_dict[s[i]] == 1:
    #         return i
    # return -1

    # 解法二：
    uniq_index = [s.index(c) for c in string.ascii_lowercase if s.count(c) == 1]
    return min(uniq_index) if len(uniq_index) > 0 else -1


if __name__ == '__main__':

    print(first_uniq_char('loveleetcode'))













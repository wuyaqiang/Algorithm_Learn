'''
剑指 Offer 第62题
'''

def last_remaining_1(n, m):
    '''
    经典解法，用环形链表模拟圆圈
    每删除一个数字需要 m 步运算，共有 n 个数字，时间复杂度为O(mn)
    需要辅助链表，空间复杂度为O(n)
    '''
    if n < 1 or m < 1:
        return -1
    numbers = [i for i in range(n)]
    count, idx = 0, 0
    while len(numbers) > 1:
        count += 1
        if idx == len(numbers):
            idx = 0
        if count % m == 0:
            numbers.pop(idx)
            idx -= 1
        idx += 1
    return numbers[0]

def last_remaining_2(n, m):
    '''
    创新解法
    '''



if __name__ == '__main__':

    print(last_remaining_1(5, 3))















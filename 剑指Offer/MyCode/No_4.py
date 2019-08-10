'''
剑指 Offer 第4题 二维数组的查找 及其变体
leetcode 74. Search a 2D Matrix
leetcode 240. Search a 2D Matrix II
'''


def search_matrix_1(matrix, target):
    '''
    leetcode 74. Search a 2D Matrix
    '''
    if not matrix or len(matrix) == 0:
        return False
    if len(matrix[0]) == 0:
        return False

    # 解法一：二分查找
    # m, n = len(matrix), len(matrix[0])
    # l, r = 0, m * n - 1
    # while l <= r:
    #     mid = l + (r - l) // 2
    #     if matrix[mid // n][mid % n] == target:
    #         return True
    #     if matrix[mid // n][mid % n] < target:
    #         l = mid + 1
    #     else:
    #         r = mid - 1
    # return False

    # 解法二：
    rows, columns = len(matrix), len(matrix[0])
    row, column = 0, columns - 1
    while row < rows:
        if target > matrix[row][column]:
            row += 1
        else:
            try:
                matrix[row].index(target)
                return True
            except:
                return False
    return False

def search_matrix_2(matrix, target):
    '''
    剑指 Offer 第4题
    leetcode 240. Search a 2D Matrix II
    '''
    if not matrix or len(matrix) == 0:
        return False
    if len(matrix[0]) == 0:
        return False

    m, n = len(matrix), len(matrix[0])
    row, col = 0, n - 1
    while row < m and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return False

















'''
剑指 Offer 第29题 顺时针打印矩阵
leetcode 54. Spiral Matrix
leetcode 59. Spiral Matrix II
'''

def spiral_order(matrix):
    '''
    剑指 Offer 第29题 顺时针打印矩阵
    leetcode 54. Spiral Matrix
    '''
    if not matrix or len(matrix) == 0:
        return []
    if len(matrix[0]) == 0:
        return []

    res = []
    m, n = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, m - 1, 0, n - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

    return res


def generate_matrix(n):
    '''
    leetcode 59. Spiral Matrix II
    '''
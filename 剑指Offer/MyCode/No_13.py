'''
剑指 Offer 第13题 机器人的运动范围
'''

def moving_count(rows, cols, k):

    def count_helper(k, rows, cols, row, col, visited):
        count = 0
        if row >= 0 and row < rows and col >= 0 and col < cols and \
           visited[row][col] == False and \
           sum([int(n) for n in str(row)+str(col)]) <= k:

            visited[row][col] = True
            count = 1 + count_helper(k, rows, cols, row - 1, col, visited)\
                      + count_helper(k, rows, cols, row + 1, col, visited)\
                      + count_helper(k, rows, cols, row, col - 1, visited)\
                      + count_helper(k, rows, cols, row, col + 1, visited)
        return count

    if rows < 1 or cols < 1 or k < 0:
        return 0

    visited = [[False] * cols for _ in range(rows)]

    res = count_helper(k, rows, cols, 0, 0, visited)

    return res


if __name__ == '__main__':

     print(moving_count(4,5,3))
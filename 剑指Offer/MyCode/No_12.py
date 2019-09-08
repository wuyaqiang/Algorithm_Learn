'''
剑指 Offer 第12题
leetcode 79. Word Search
leetcode 212. Word Search II
'''

def has_path(board, word):
    '''
    剑指Offer 12
    leetcode 79. Word Search
    '''
    # 解法一 剑指Offer解法，使用 visited 矩阵：
    # if not board or len(board) == 0 or not board[0] or len(board[0]) == 0:
    #     return False
    #
    # def judge(board, rows, cols, row, col, pos, word, visited):
    #     if pos == len(word):
    #         return True
    #
    #     has_path = False
    #
    #     if row >= 0 and row < rows and col >= 0 and \
    #        col < cols and board[row][col] == word[pos] and \
    #        visited[row][col] == False:
    #
    #         pos += 1
    #         visited[row][col] = True
    #         has_path = judge(board, rows, cols, row - 1, col, pos, word, visited) or \
    #                    judge(board, rows, cols, row, col - 1, pos, word, visited) or \
    #                    judge(board, rows, cols, row + 1, col, pos, word, visited) or \
    #                    judge(board, rows, cols, row, col + 1, pos, word, visited)
    #
    #         if not has_path:
    #             pos -= 1
    #             visited[row][col] = False
    #
    #     return has_path
    #
    # rows, cols = len(board), len(board[0])
    # visited = [[False] * cols for _ in range(rows)]
    #
    # for row in range(rows):
    #     for col in range(cols):
    #         if judge(board, rows, cols, row, col, 0, word, visited):
    #             return True
    #
    # return False

    # 解法二 不使用 visited 矩阵，更加简洁
    if not board or len(board) == 0 or len(board[0]) == 0:
        return False

    def judge(board, rows, cols, row, col, word):
        if len(word) == 0:
            return True
        if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[0]:
            return False
        cur_char = board[row][col]
        board[row][col] = "#"   # 访问过的字符置为“#”，与 visited 矩阵起到相同作用，更加节省空间
        res = judge(board, rows, cols, row - 1, col, word[1:]) or \
              judge(board, rows, cols, row + 1, col, word[1:]) or \
              judge(board, rows, cols, row, col - 1, word[1:]) or \
              judge(board, rows, cols, row, col + 1, word[1:])
        board[row][col] = cur_char
        return res

    rows, cols = len(board), len(board[0])
    for row in range(rows):
        for col in range(cols):
            if judge(board, rows, cols, row, col, word):
                return True
    return False

def find_words(board, words):
    '''
    较难，暂略
    '''
    pass
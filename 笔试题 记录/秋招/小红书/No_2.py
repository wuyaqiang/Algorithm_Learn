#coding=utf-8
import sys

def func(N, string_matrix, start_pos):

    res = N * N + 1
    queue = [(start_pos, 0)]
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while queue:
        cur = queue.pop(0)
        cur_pos, cur_num = cur[0], cur[1]
        for i in range(4):
            x = (cur_pos[0] + move[i][0] + N ) % N
            y = (cur_pos[1] + move[i][1] + N ) % N
            if string_matrix[x][y] == "E":
                res = cur_num + 1 if cur_num + 1 < res else res
            elif string_matrix[x][y] == ".":
                string_matrix[x][y] = "S"
                queue.append(([x, y], cur_num + 1))

    if res == N * N + 1:
        return -1
    return res

if __name__ == "__main__":

    N = int(sys.stdin.readline().strip())
    string_matrix = []
    start_pos = [0, 0]
    for i in range(N):
        cur_string = sys.stdin.readline().strip()
        if "S" in cur_string:
            start_pos[0], start_pos[1] = i, cur_string.find("S")
        string_matrix.append([c for c in cur_string])

    res = func(N, string_matrix, start_pos)
    print(res)
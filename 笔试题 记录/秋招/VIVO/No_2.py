# #coding=utf-8
import sys

def max_user_number(total_disk, total_memory, app_list):

    dp = [[0] * (total_memory + 1) for _ in range(total_disk + 1)]
    for i in range(len(app_list)):
        for j in range(total_disk, app_list[i][0] - 1, -1):
            for k in range(total_memory, app_list[i][1] - 1, -1):
                dp[j][k] = max(dp[j][k], dp[j - app_list[i][0]][k - app_list[i][1]] + app_list[i][2])

    return dp[total_disk][total_memory]


if __name__ == "__main__":

    input_string = sys.stdin.readline().strip().split(" ")
    disk = int(input_string[0])
    memory = int(input_string[1])
    app = []
    for item in input_string[2].split("#"):
        item_list = item.split(",")
        app.append([int(item_list[0]), int(item_list[1]), int(item_list[2])])

    res = max_user_number(disk, memory, app)
    print(res)











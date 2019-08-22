#coding=utf-8
import sys

def longest_common_prefix(string_list, n, a, b):

    if a < 1 or b < 1 or a > n or b > n:
        return ""
    str_a = string_list[a - 1]
    str_b = string_list[b - 1]
    idx = 0
    while str_a[idx] == str_b[idx]:
        idx += 1
    return str(idx)

if __name__ == "__main__":

    n = int(sys.stdin.readline().strip())
    string_list = []
    for i in range(n):
        cur_str = sys.stdin.readline().strip()
        string_list.append(cur_str)
    while True:
        cur_check = sys.stdin.readline().strip()
        # if cur_check == "":
        #     break
        a, b = list(map(int, cur_check.split()))
        res = longest_common_prefix(string_list, n, a, b)
        # if res == "":
        #     continue
        print(res)





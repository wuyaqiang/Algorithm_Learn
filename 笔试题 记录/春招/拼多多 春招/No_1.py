#coding=utf-8
import sys

def min_diff(arr, n):
    arr_sorted = sorted(arr)
    sum_list = []
    for i in range(int(n/2)):
        sum_list.append(arr_sorted[i] + arr_sorted[n-1-i])
    return max(sum_list) - min(sum_list)

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    print(min_diff(values, n))
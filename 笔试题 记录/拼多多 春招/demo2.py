#coding=utf-8
import sys

def min_mul(use_num, A_n, B_n):
    if (use_num[0] >= min(A_n, B_n)):
        return 0
    use_num_seq = []
    for num, count in enumerate(use_num):
        # num是0-9的整数, count为其对应的可使用次数
        use_num_seq += [num] * count
    # B_n = B_n - use_num[0]  # 将0全部放到位数大的数字前面
    if A_n > B_n:
        temp = B_n
        B_n = A_n
        A_n = temp
    diff = B_n - A_n
    A = ""
    B = ""
    if diff > 0:
        for i in range(diff):
            B += str(use_num_seq[i])
    use_num_seq = use_num_seq[diff: ]
    for i in range(0, A_n * 2, 2):
        A += str(use_num_seq[i])
        B += str(use_num_seq[i+1])

    return int(A) * int(B)

if __name__ == "__main__":

    line = sys.stdin.readline().strip()
    # 0-9的使用次数：
    use_num = list(map(int, line.split()))
    # A的位数：
    A_n = int(sys.stdin.readline().strip())
    # B的位数：
    B_n = int(sys.stdin.readline().strip())

    print(min_mul(use_num, A_n, B_n))
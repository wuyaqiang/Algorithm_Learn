#coding=utf-8
import sys

def transfer(num):
    if num >= 10 and num <= 31:
        replace_dict = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
                        'P','Q','R','S','T','U','V']
        return replace_dict[num-10]
    else:
        return str(num)

def encoder(num):
    num_len = len(num)

    step_1 = []
    step_1_num = '0'*(3-num_len%3) + num
    for i in range(0, len(step_1_num), 3):
        step_1.append(step_1_num[i:i+3])

    step_2 = [bin(int(i))[2: ] for i in step_1]
    step_2_0_len = len(step_2[0])
    step_2 = ['0'*(10-len(i))+i for i in step_2]
    step_2[0] = step_2[0][10-step_2_0_len: ]
    step_2 = "".join(step_2)

    step_3 = '0'*(5-len(step_2)%5) + step_2
    step_3_list = []
    for i in range(0, len(step_3), 5):
        step_3_list.append(step_3[i:i+5])

    step_4 = [int(i, 2) for i in step_3_list]
    step_4 = [transfer(i) for i in step_4]

    step_5 = "".join(step_4)

    return step_5

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = []
    for i in range(n):
        num = sys.stdin.readline().strip()
        ans.append(encoder(num))

    for i in ans:
        print(i)
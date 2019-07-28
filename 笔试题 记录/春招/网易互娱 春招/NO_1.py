#coding=utf-8
import sys

def card(card_seq, card_num):
    count = 0
    num_count = {}
    card_seq.sort()
    if card_num < 5 or card_seq[-1] - card_seq[0] < 4:
        return count
    for num in card_seq:
        if num not in num_count:
            num_count[num] = 1
        else:
            num_count[num] += 1

    card_seq = sorted(list(set(card_seq)))
    if len(card_seq) < 5:
        return count

    all_combine = []
    for idx, num in enumerate(card_seq):
        if card_seq[idx+1]==num+1 and card_seq[idx+2]==num+2 and card_seq[idx+3]==num+3 and card_seq[idx+4]==num+4:
            combine = [card_seq[idx], card_seq[idx+1], card_seq[idx+2], card_seq[idx+3], card_seq[idx+4]]
            if combine not in all_combine:
                all_combine.append(combine)
        if (idx+5)==len(card_seq):
            break
    multi = 1
    for key, value in num_count.items():
        multi *= value

    count = multi * len(all_combine)

    return count


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        # 读取每一行
        card_num = int(sys.stdin.readline().strip())
        line = sys.stdin.readline().strip()
        line = line.replace('A', '1')
        line = line.replace('J', '11')
        line = line.replace('Q', '12')
        line = line.replace('K', '13')
        # 把每一行的数字分隔后转化成int列表
        card_seq = list(map(int, line.split()))
        print(card(card_seq, card_num))
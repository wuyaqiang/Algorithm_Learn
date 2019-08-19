#coding=utf-8
import sys

def max_ice_cream(n, m, w_list, v_list):
    '''
    :param n: 冰淇淋配料的种类数量
    :param m: 小Q的钱数
    :param w_list: 每份原料的储备数量
    :param v_list: 每份配料的售价
    '''
    lower_bound = min(w_list)
    res = lower_bound
    w_list = [w - lower_bound for w in w_list]
    min_idx_list = [idx for idx, w in enumerate(w_list) if w == 0]
    while m >= 0:
        second_min = min([w for w in w_list if w > 0])
        zero_sum = 0
        for idx in min_idx_list:
            zero_sum += v_list[idx]
        if m < zero_sum:
            break
        if m // zero_sum > second_min:
            w_list = [w - second_min if w != 0 else 0 for w in w_list]
            m -= second_min * zero_sum
        else:
            w_list = [w - m // zero_sum if w != 0 else 0 for w in w_list]
            m -= (m // zero_sum) * zero_sum

        if m >= 0:
            res += 1
        min_idx_list = [idx for idx, w in enumerate(w_list) if w == 0]
    return res


if __name__ == "__main__":

    line_1 = sys.stdin.readline().strip()
    n, m = list(map(int, line_1.split()))

    line_2 = sys.stdin.readline().strip()
    w_list = list(map(int, line_2.split()))

    line_3 = sys.stdin.readline().strip()
    v_list = list(map(int, line_3.split()))

    res = max_ice_cream(n, m, w_list, v_list)
    print(res)
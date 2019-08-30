
def fractional_knapsack(W, w_list, val_list):

    if len(w_list) == 0 or W <= 0:
        return 0

    n = len(w_list)
    item_list = []
    for i in range(n):
        item_list.append([w_list[i], val_list[i], val_list[i] / w_list[i]])
    # 按照单位重量的价值排序, 递减:
    item_list.sort(key=lambda x:x[2], reverse=True)

    res = 0
    for cur_w, cur_val, ave_val in item_list:
        if cur_w <= W:
            W -= cur_w
            res += cur_val
        else:
            # res += cur_val * (W / cur_w)
            res += W * ave_val
            break
    return res


if __name__ == '__main__':

    W = 50
    w_list = [10, 40, 20, 30]
    val_list = [60, 40, 100, 120]

    print(fractional_knapsack(W, w_list, val_list))

    pass



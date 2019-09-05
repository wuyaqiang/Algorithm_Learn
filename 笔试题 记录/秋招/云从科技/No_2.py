#coding=utf-8
import sys

def helper_1(p1, p2, p3):

    a = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    b = (p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2
    c = (p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2
    if a == b + c:
        return [2, b, c]
    elif b == a + c:
        return [0, a, c]
    elif c == a + b:
        return [1, a, b]
    else:
        return False


def find_zhijiao(p1, p2, p3, p4):

    combine_list = [p1, p2, p3], [p1, p2, p4], [p1, p3, p4], [p2, p3, p4]
    bianchang = []
    for item in combine_list:
        ret = helper_1(item[0], item[1], item[2])
        if ret != False:
            bianchang.append([ret[1] ** 0.5, ret[2] ** 0.5])

    res = 0
    for i in bianchang:
        res += sum[i]



if __name__ == "__main__":

    points_list = []
    for _ in range(16):
        point = list(map(int, sys.stdin.readline().strip().split(",")))
        points_list.append(point)

    # res = func(points_list)
    # print(res)
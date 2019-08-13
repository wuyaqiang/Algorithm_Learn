#coding=utf-8
import sys

def pool_problem(m, t, m1, t1, m2, t2):
    '''
    :param m:  泳池最大容量 m
    :param t:  经过 t 分钟后，泳池里有多少升水？
    :param m1: 给水管每分钟注入 m1 升水
    :param t1: 每经过 t1 分钟，给水管状态改变
    :param m2: 排水管每分钟排除 m2 升水
    :param t2: 每经过 t2 分钟，排水管状态改变
    :return: 经过 t 分钟后，泳池里有多少升水？
    '''
    water_in, water_out = True, True    # 初始化给水管和排水管都为打开状态
    pool_vol = 0    # 水池中水量
    for i in range(t):
        if i > 0 and i % t1 == 0:
            water_in = not water_in
        if i > 0 and i % t2 == 0:
            water_out = not water_out
        if water_in and water_out:
            pool_vol += m1 - m2
        elif water_in:
            pool_vol += m1
        elif water_out:
            pool_vol -= m2
        if pool_vol > m:
            pool_vol = m
        if pool_vol < 0:
            pool_vol = 0
    return pool_vol


if __name__ == "__main__":

    T = int(sys.stdin.readline().strip())
    for i in range(T):
        data_line = sys.stdin.readline().strip()
        data = list(map(int, data_line.split()))
        res = pool_problem(data[0], data[1], data[2], data[3], data[4], data[5])
        print(res)


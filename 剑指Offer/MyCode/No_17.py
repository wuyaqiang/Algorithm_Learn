'''
剑指 Offer 第17题 打印从 1 到最大的 n 位数
'''

def print_1_to_n(n):
    if n <= 0:
        return
    number = [0] * n
    while not add_one(number, n):
        print("".join([str(i) for i in number]).lstrip("0"))
    return

def add_one(number, n):
    is_overflow = False
    carry = 0
    for i in range(n-1, -1, -1):
        s = number[i] + carry
        if i == n - 1:
            s += 1
        if s >= 10:
            if i == 0:
                is_overflow = True
                break
            else:
                number[i] = s % 10
                carry = s // 10
        else:
            number[i] = s
            break
    return is_overflow

if __name__ == '__main__':

    print_1_to_n(2)
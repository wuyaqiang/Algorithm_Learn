#coding=utf-8
import sys

def func(n):

    roman_label = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    replace_number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    res, i = "", 0
    while i < 13:
        if n >= replace_number[i]:
            res += (n // replace_number[i]) * roman_label[i]
            n %= replace_number[i]
        if n == 0:
            break
        i += 1

    return res


if __name__ == "__main__":

    n = int(sys.stdin.readline().strip())

    print(func(n))
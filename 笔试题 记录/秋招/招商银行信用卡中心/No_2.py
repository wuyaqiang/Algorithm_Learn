#coding=utf-8
import sys

def func(string):

    n = len(string)
    if string.rstrip("?").find("?") == -1:
        largest_num = int(str(int(string.rstrip("?")) + 1) + '0' * string.count("?"))
        num = int(string.replace("?", "0"))
        count = 0
        while num % 13 != 5:
            num += 1
        while num < largest_num:
            count += 1
            num += 13
        return count % (10 ** 9 + 7)

    if string.lstrip("?").find("?") == -1:
        largest_num = int(string.replace("?", "9"))
        smallest_num = int(string.replace("?", "0"))
        count = 0
        while smallest_num % 13 != 5:
            smallest_num += 1
        while smallest_num <= largest_num:
            count += 1
            smallest_num = 0

    return 99

if __name__ == "__main__":

    input_str = sys.stdin.readline().strip()

    print(func(input_str))
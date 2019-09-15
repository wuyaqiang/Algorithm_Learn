#coding=utf-8
import sys

def func(label):

    length = len(label)
    res = []
    for _ in range(length):
        res.append(0)
    for i in range(length):
        if label[i] == "L":
            j = i
            while j - 1 >= 0 and label[j - 1] + label[j] != "RL":
                j -= 1
            if (j - i) % 2:
                res[j - 1] += 1
            else:
                res[j] += 1
        else:
            j = i
            while j + 1 < length and label[j] + label[j + 1] != "RL":
                j += 1
            if (j - i) % 2:
                res[j + 1] += 1
            else:
                res[j] += 1
    return res

if __name__ == "__main__":

    input_label = sys.stdin.readline().strip()
    res = func(input_label)
    print(" ".join([str(n) for n in res]))
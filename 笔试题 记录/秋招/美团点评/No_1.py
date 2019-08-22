#coding=utf-8
import sys

def compare(s1, s2):
    if s1 == "":
        return True
    if s2 == "":
        return False
    if s1 == s2[ : len(s1)]:
        return True
    if s2 == s1[ : len(s2)]:
        return False
    for i in range(min(len(s1), len(s2))):
        if s1[i] > s2[i]:
            return True
        if s1[i] < s2[i]:
            return False
    return True

def string_sort(string_list):

    if not string_list or len(string_list) == 0:
        return []
    for i in range(len(string_list) - 1):
        for j in range(len(string_list) - 1, i, -1):
            if compare(string_list[j], string_list[j-1]):
                string_list[j], string_list[j-1] = string_list[j-1], string_list[j]
    return string_list

if __name__ == "__main__":

    string_list = sys.stdin.readline().strip().split(",")

    res = string_sort(string_list)
    print(",".join(res))


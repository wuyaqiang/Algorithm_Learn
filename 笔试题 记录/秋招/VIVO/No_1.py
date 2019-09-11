#coding=utf-8
import sys

def min_number(input_string):

    temp_stack = []
    for i in range(len(input_string)):
        if input_string[i] == "0":
            break
        elif input_string[i] == "(":
            temp_stack.append(input_string[i])
        else:
            temp_stack.pop()
    return len(temp_stack)


if __name__ == "__main__":

    input_string = sys.stdin.readline().strip()
    res = min_number(input_string)
    print(res)
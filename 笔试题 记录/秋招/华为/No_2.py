#coding=utf-8
import sys

def data_analysis(string):

    n, douhao, shuangyin = len(string), -1, -1
    error, cur_str, i = False, "", 0
    feature_list = []
    while i < n:
        if error:
            break
        if string[i] == "," and shuangyin == -1:
            feature_list.append(cur_str)
            cur_str = ""
            i += 1
            continue
        if string[i] == '"' and i < n - 1 and string[i + 1] == '"':
            cur_str += string[i]
            i += 2
            continue
        if string[i] == '"' and shuangyin == -1:
            shuangyin = i
            i += 1
            continue
        if string[i] == '"' and shuangyin != -1:
            shuangyin = -1
            i += 1
            if i == n:
                feature_list.append(cur_str)
            continue
        cur_str += string[i]
        i += 1

    if shuangyin != -1 or error:
        print("ERROR")
        return

    print(len(feature_list))
    for s in feature_list:
        if s == "":
            print("--")
        else:
            print(s)
    return


if __name__ == "__main__":

    input_string = sys.stdin.readline().strip()

    data_analysis(input_string)

# #coding=utf-8
# import sys
#
#
#
#
# if __name__ == "__main__":
#
#     input_arr, N = sys.stdin.readline().strip().split(";")
#     input_arr = list(map(int, input_arr.split(",")))
#     N = int(N)


def function(strs):

    res = ""
    f = 0
    begin = 0

    for i in range(len(strs)):
        if f == 0:
            if strs[i] == "(":
                f = 1
            elif strs[i] == "<":
                if begin > 0:
                    begin -= 1
                    res = res[:begin]
            else:
                res += strs[i]
                begin += 1



        else:
            if strs[i] == "(":
                f += 1
            elif strs[i] == ")":
                f -= 1
    return res[:begin+1]



if __name__ == "__main__":

    strs = input().strip()
    print(function(strs))

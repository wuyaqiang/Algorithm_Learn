import sys

def func(n, m, k, nums_dict):

    function_list = []
    for _, v in nums_dict.items():
        if len(function_list) == 0:
            function_list.append(set(v))
        f = False
        for i in range(len(function_list)):
            for j in range(len(v)):
                if v[j] in function_list[i]:
                    f = True
                    function_list[i].update(set(v))
                    break
            if f:
                break
        if f == False:
            function_list.append(set(v))

    function_list_2 = []

    for i in range(1, n+1):
        f = False
        for j in function_list:
            if i in j:
                f = True
                break
        if f == False:
            function_list_2.append(i)

    return len(function_list) + len(function_list_2) - 1

if __name__ == '__main__':

    n, m, k = list(map(int, sys.stdin.readline().strip().split()))
    nums_dict = {}
    for i in range(k):
        cur_input = list(map(int, sys.stdin.readline().strip().split()))
        if cur_input[1] in nums_dict:
            nums_dict[cur_input[1]].append(cur_input[0])
        else:
            nums_dict[cur_input[1]] = [cur_input[0]]

    res = func(n, m, k, nums_dict)
    print(res)






#coding=utf-8
import sys

def most_click(n, log_list):

    click_count = {}
    for item in log_list:
        if item[0] in click_count:
            click_count[item[0]] += 1
        else:
            click_count[item[0]] = 1
    max_count = max(click_count.values())
    max_id = []
    for key, value in click_count.items():
        if value == max_count:
            max_id.append(key)

    # return max(max_id)
    return log_list[0][0]

if __name__ == "__main__":

    n = int(sys.stdin.readline().strip())
    log_list = []

    for _ in range(n):
        from_avid, to_avid = list(map(int, sys.stdin.readline().strip().split()))
        log_list.append([from_avid, to_avid])

    print(most_click(n, log_list))
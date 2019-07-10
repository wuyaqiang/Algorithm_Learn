

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    n = nums[0]
    m = nums[1]
    matrix = []
    for i in range(n):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    list1 = []
    list2 = []
    dict1 = {}
    dict2 = {}
    for i in range(n):
        for j in range(m):
            if i % 2 == 0:
                if j % 2 == 0:
                    list1.append(matrix[i][j])
                    try:
                        dict1[matrix[i][j]] += 1
                    except:
                        dict1[matrix[i][j]] = 1
                else:
                    list2.append(matrix[i][j])
                    try:
                        dict2[matrix[i][j]] += 1
                    except:
                        dict2[matrix[i][j]] = 1
            else:
                if j % 2 == 0:
                    list2.append(matrix[i][j])
                    try:
                        dict2[matrix[i][j]] += 1
                    except:
                        dict2[matrix[i][j]] = 1
                else:
                    try:
                        dict1[matrix[i][j]] += 1
                    except:
                        dict1[matrix[i][j]] = 1

    max1 = 0
    sec1 = 0
    max2 = 0
    sec2 = 0
    for i in dict1.keys():
        if dict1[i] > max1:
            max1 = i
        if dict1[i] > sec1 and dict1[i] < max1:
            sec1 = i
    for i in dict2.keys():
        if dict2[i] > max2:
            max2 = i
        if dict2[i] > sec2 and dict2[i] < max2:
            sec2 = i
    if max1 != max2:
        print(len(list1) - dict1[max1] + len(list2) - dict2[max2])
    else:
        print(min(len(list1) - dict1[sec1] + len(list2) - dict2[max2],
                  len(list1) - dict1[max1] + len(list2) - dict2[sec2]))
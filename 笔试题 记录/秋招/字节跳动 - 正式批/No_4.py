def havel_hakimi_algo(degree_list):
    degree_list.sort(reverse=True)
    for degree in degree_list:
        if degree < 0:
            return False
        if degree != 0:
            remove_val = degree_list.pop(0)
            for index in range(remove_val):
                degree_list[index] -= 1
            havel_hakimi_algo(degree_list)
    return True


print(havel_hakimi_algo([4,4,3,3,2,2]))
print(havel_hakimi_algo([3,3,3,1]))
print(havel_hakimi_algo([5,4,3,2,2]))
print(havel_hakimi_algo([6,6,3,2,2,2,1]))
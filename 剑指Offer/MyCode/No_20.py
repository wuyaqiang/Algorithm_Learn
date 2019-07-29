'''
剑指 Offer 第20题 表示数值的字符串
leetcode 65. Valid Number
'''

def is_valid_number(s):
    '''
    判断输入的字符串 s 是否表示一个有效的数字
    '''
    s = s.strip()
    has_point, has_e, has_number = False, False, False
    for i, c in enumerate(s):
        if "0" <= c <= "9":
            has_number = True
        elif c == ".":
            if has_point or has_e:
                return False
            has_point = True
        elif c == "e":
            if has_e or not has_number:
                return False
            has_number = False
            has_e = True
        elif c == "+" or c == "-":
            if i > 0 and s[i-1] != "e":
                return False
        else:
            return False

    return has_number





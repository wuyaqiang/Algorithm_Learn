'''
剑指 Offer 第44题 数字序列中某一位的数字
leetcode 400. Nth Digit
'''

def find_nth_digit(n):
    if n < 0:
        return -1
    digits = 1
    while True:
        numbers = 9 * pow(10, digits - 1)
        if n < digits * numbers:
            num = pow(10, digits - 1) + (n - 1) // digits
            return int(str(num)[n % digits - 1])

        n -= digits * numbers
        digits += 1

if __name__ == '__main__':

    print(find_nth_digit(19))
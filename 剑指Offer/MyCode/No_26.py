'''
剑指 Offer 第26题 树的子结构
leetcode 572. Subtree of Another Tree 树的子树

注意：
树的子结构和树的子树是两个不同的概念，
即上面剑指 Offer 26 和 leetcode 572 题目不同。
'''

def is_sub_structure(s, t):
    '''
    剑指 Offer 第26题 树的子结构
    '''
    def check(n1, n2):
        if not n2:
            return True
        if not n1:
            return False
        if n1.val != n2.val:
            return False
        return check(n1.left, n2.left) and check(n1.right, n2.right)
    res = False
    if s and t:
        if s.val == t.val:
            res = check(s, t)
        if not res:
            is_sub_structure(s.left, t)
        if not res:
            is_sub_structure(s.right, t)
    return res


def is_sub_tree(s, t):
    '''
    leetcode 572. Subtree of Another Tree 树的子树
    '''
    # 解法一：类似剑指Offer的解法
    # def check(n1, n2):
    #     if n1 and n2:
    #         return n1.val == n2.val and check(n1.left, n2.left) and check(n1.right, n2.right)
    #     return True if not n1 and not n2 else False
    # res = False
    # if s and t:
    #     if s.val == t.val:
    #         res = check(s, t)
    #     if not res:
    #         res = is_sub_tree(s.left, t)
    #     if not res:
    #         res = is_sub_tree(s.right, t)
    # return res

    # 解法二：leetcode上解法，更简略
    if not s:
        return t == None

    def check(n1, n2):
        if n1 and n2:
            return n1.val == n2.val and check(n1.left, n2.left) and check(n1.right, n2.right)
        return True if not n1 and not n2 else False

    return check(s, t) or is_sub_tree(s.left, t) or is_sub_tree(s.right, t)















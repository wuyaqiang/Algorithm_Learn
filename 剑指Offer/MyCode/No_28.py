'''
剑指 Offer 第28题 对称的二叉树
leetcode 101. Symmetric Tree
'''

def is_symmetric(root):

    # 解法一：递归
    # def helper(n1, n2):
    #     if n1 and n2:
    #         return n1.val == n2.val and helper(n1.left, n2.right) and helper(n1.right, n2.left)
    #     return True if not n1 and not n2 else False
    # return helper(root, root)

    # 解法二：非递归
    if not root:
        return True
    stack = [(root.left, root.right)]
    while stack:
        n1, n2 = stack.pop()
        if not n1 and not n2:
            continue
        if not n1 or not n2:
            return False
        if n1.val == n2.val:
            stack.append((n1.left, n2.right))
            stack.append((n1.right, n2.left))
        else:
            return False
    return True


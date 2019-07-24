'''
剑指 Offer 第34题 及其变体
leetcode 112. Path Sum
leetcode 113. Path Sum II
'''

def has_path_sum(root, s):
    '''
    leetcode 112. Path Sum  判断是否存在一条和为 s 的路径
    '''
    # 解法一：递归解法
    # if not root:
    #     return False
    # if not root.left and not root.right:
    #     return root.val == s
    # return has_path_sum(root.left, s - root.val) or has_path_sum(root.right, s - root.val)

    # 解法二：循环解法
    if not root:
        return False
    queue = [(root, s - root.val)]
    while queue:
        cur, val = queue.pop(0)
        if not cur.left and not cur.right and val == 0:
            return True
        if cur.left:
            queue.append((cur.left, val - cur.left.val))
        if cur.right:
            queue.append((cur.right, val - cur.right.val))
    return False


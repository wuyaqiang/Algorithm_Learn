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

def path_sum(root, s):
    '''
    找出所有路径，路径上所有结点的和为s
    剑指 Offer 34
    leetcode 113. Path Sum II
    '''
    # 解法一：递归解法
    def dfs(root, s, cur_path, res):
        if not root.left and not root.right and root.val == s:
            cur_path.append(root.val)
            res.append(cur_path)
        if root.left:
            dfs(root.left, s - root.val, cur_path + [root.val], res)
        if root.right:
            dfs(root.right, s - root.val, cur_path + [root.val], res)
    res = []
    if not root:
        return res
    dfs(root, s, [], res)
    return res

    # 解法二：循环解法
    # res = []
    # if not root:
    #     return res
    # queue = [(root, s - root.val, [root.val])]
    # while queue:
    #     node, val, cur_list = queue.pop(0)
    #     if not node.left and not node.right and val == 0:
    #         res.append(cur_list)
    #     if node.left:
    #         queue.append((node.left, val - node.left.val, cur_list + [node.left.val]))
    #     if node.right:
    #         queue.append((node.right, val - node.right.val, cur_list + [node.right.val]))
    # return res

























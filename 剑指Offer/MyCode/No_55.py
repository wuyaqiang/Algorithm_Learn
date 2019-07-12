'''
剑指 Offer 第55题 及其变体
同 leetcode 104. Maximum Depth of Binary Tree
同 leetcode 110. Balanced Binary Tree
'''

def max_depth_recursive(root):
    '''
    返回二叉树的高度，递归解法
    '''
    if not root:
        return 0
    return 1 + max(max_depth_recursive(root.left), max_depth_recursive(root.right))

def max_depth_iterative(root):
    '''
    返回二叉树的高度，循环解法
    '''
    if not root:
        return 0
    level = [root]
    depth = 0
    while level:
        depth += 1
        next_level = []
        for node in level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = next_level
    return depth

def is_balanced(root):
    '''
    判断二叉树是否为平衡二叉树
    '''
    if not root:
        return True
    return helper(root) != -1

def helper(root):
    if not root:
        return 0
    left = helper(root.left)
    right = helper(root.right)
    if left == -1 or right == -1 or abs(left - right) > 1:
        return -1
    return 1 + max(left, right)























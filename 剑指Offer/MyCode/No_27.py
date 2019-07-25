'''
剑指 Offer 第27题 二叉树的镜像
leetcode 226. Invert Binary Tree
'''

def invert_tree(root):
    '''
    将二叉树转换为它的镜像二叉树
    '''
    # 解法一：递归
    # if not root:
    #     return None
    # root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    # return root

    # 解法二：非递归
    # if not root:
    #     return None
    # stack = [root]
    # while stack:
    #     cur = stack.pop()
    #     if cur:
    #         cur.left, cur.right = cur.right, cur.left
    #     if cur.left:
    #         stack.append(cur.left)
    #     if cur.right:
    #         stack.append(cur.right)
    # return root

    # 解法二精简代码：
    stack = [root]
    while stack:
        cur = stack.pop()
        if cur:
            cur.left, cur.right = cur.right, cur.left
            stack.append(cur.left)
            stack.append(cur.right)
    return root
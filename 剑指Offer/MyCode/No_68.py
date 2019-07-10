'''
剑指 Offer 第68题 及其变体
同 leetcode 235 236 题
235 二叉搜索树的最低公共祖先
236 二叉树的最低公共祖先
Lowest Common Ancestor：LCA
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def LCA_of_BST_iterative(root, p, q):
    '''
    二叉搜索树的最低公共祖先，循环解法
    '''
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
    return None

def LCA_of_BST_recursive(root, p, q):
    '''
    二叉搜索树的最低公共祖先，递归解法
    '''
    if p.val < root.val and q.val < root.val:
        return LCA_of_BST_recursive(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return LCA_of_BST_recursive(root.right, p, q)
    return root

def LCA_of_BT_iterative(root, p, q):
    '''
    二叉树的最低公共祖先，循环解法
    '''
    if not root or not p or not q:
        return None
    stack = [root]
    parent_dict = {root: None}
    while p not in parent_dict or q not in parent_dict:
        cur = stack.pop()
        if cur.left:
            stack.append(cur.left)
            parent_dict[cur.left] = cur
        if cur.right:
            stack.append(cur.right)
            parent_dict[cur.right] = cur
    ancestor = []
    while p:
        ancestor.append(p)
        p = parent_dict[p]
    while q not in ancestor:
        q = parent_dict[q]
    return q

def LCA_of_BT_recursive(root, p, q):
    '''
    二叉树的最低公共祖先，递归解法
    '''
    if root == None or root == p or root == q:
        return root
    left = LCA_of_BT_recursive(root.left, p, q)
    right = LCA_of_BT_recursive(root.right, p, q)
    if left and right:
        return root
    return left or right




